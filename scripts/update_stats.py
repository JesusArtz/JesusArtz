#!/usr/bin/env python3
"""Refresh authored Git diff statistics for accessible non-fork repositories.

GitHub contributor statistics cover default-branch history, excluding merges and
empty commits. Additions/deletions count diff lines (including docs and vendored
files), not the size of the current source tree. Failures preserve the last SVG.
Source: https://docs.github.com/en/rest/metrics/statistics
"""
import concurrent.futures
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
USER = 'JesusArtz'
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])


def api(endpoint):
    try:
        result = subprocess.run(['gh', 'api', '--include', endpoint], capture_output=True,
                                text=True, timeout=60)
    except subprocess.TimeoutExpired:
        raise RuntimeError('GitHub request timed out; previous snapshot preserved') from None
    output = result.stdout.replace('\r\n', '\n')
    match = re.match(r'HTTP/\S+\s+(\d+)', output)
    status = int(match[1]) if match else 0
    if result.returncode or status not in (200, 202, 204):
        raise RuntimeError(f'GitHub API request failed ({status}); previous snapshot preserved')
    body = output.split('\n\n', 1)[1].strip()
    return status, json.loads(body) if body else None


def repositories():
    _, viewer = api('user')
    if viewer['login'].lower() != USER.lower():
        raise RuntimeError('Use a personal token belonging to the profile owner')
    repos = []
    page = 1
    while True:
        _, batch = api(f'user/repos?per_page=100&page={page}&visibility=all&affiliation=owner,collaborator,organization_member')
        repos.extend(r for r in batch if not r['fork'] and r['size'] > 0)
        if len(batch) < 100:
            if not any(r['private'] for r in repos):
                raise RuntimeError('Private repositories are not accessible; previous snapshot preserved')
            return repos
        page += 1


def contributor_totals(data):
    author = next((c for c in data if (c.get('author') or {}).get('login', '').lower()
                   == USER.lower()), None)
    if author is None:
        return (0, 0, 0)
    # GitHub returns zero line counts above this API limit; do not publish them.
    if sum(c['total'] for c in data) >= 10000:
        raise RuntimeError('Contributor line statistics unavailable above 10,000 commits')
    return (author['total'], sum(w['a'] for w in author['weeks']),
            sum(w['d'] for w in author['weeks']))


def collect():
    pending = repositories()
    totals = [0, 0, 0]
    # A 202 triggers GitHub's background calculation. Retry the pending set only.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for attempt in range(9):
            responses = pool.map(lambda r: api(f"repos/{r['full_name']}/stats/contributors"), pending)
            retry = []
            for repo, (status, data) in zip(pending, responses):
                if status == 202:
                    retry.append(repo)
                    continue
                values = (0, 0, 0) if status == 204 else contributor_totals(data)
                totals = [a + b for a, b in zip(totals, values)]
            if not retry:
                return totals
            pending = retry
            print(f'Waiting for GitHub to compute {len(pending)} histories (attempt {attempt + 1})', flush=True)
            if attempt < 8:
                time.sleep(10)
    raise RuntimeError('GitHub is still computing statistics; previous snapshot preserved')


def render(commits, additions, deletions):
    path = ROOT / 'assets/profile.svg'
    tree = ET.parse(path)
    svg = tree.getroot()
    svg.set('height', '580')
    svg.set('viewBox', '0 0 640 580')
    svg.find(NS + 'rect').set('height', '580')
    # Keep the rest of the hand-authored profile and embedded brand icons intact.
    for group in svg.findall(NS + 'g'):
        if group.get('id') == 'github-stats':
            svg.remove(group)
    for text in svg.iter(NS + 'text'):
        if 'Always building' in ''.join(text.itertext()):
            text.set('y', '554')
    group = ET.SubElement(svg, NS + 'g', {'id': 'github-stats', 'font-family': 'monospace',
                                        'font-size': '15', 'fill': '#addaf7'})
    ET.SubElement(group, NS + 'path', {'d': 'M25 401H615', 'stroke': '#30363d'})
    def line(y, content, color='#addaf7', size='15'):
        ET.SubElement(group, NS + 'text', {'x': '25', 'y': str(y), 'fill': color,
                                         'font-size': size}).text = content
    line(426, 'GitHub Stats / all time', '#f0883e', '13')
    line(454, f'Commits ........... {commits:,}')
    line(482, f'Lines of code ..... +{additions:,} / -{deletions:,}')
    line(507, 'Public + private · default branches · no merges', '#8b949e', '11')
    line(525, 'Lines = additions / deletions in Git diffs', '#8b949e', '11')
    ET.indent(tree, space='  ')
    path.write_text(ET.tostring(svg, encoding='unicode') + '\n')
    snapshot = {'updated_at': datetime.now(timezone.utc).isoformat(), 'commits': commits,
                'lines_added': additions, 'lines_deleted': deletions,
                'scope': 'Authored Git diff lines in accessible public/private non-fork repos, including organizations; default branches; excludes merge/empty commits.'}
    (ROOT / 'assets/stats.json').write_text(json.dumps(snapshot, indent=2) + '\n')


if __name__ == '__main__':
    values = collect()
    render(*values)
    print(f'Updated stats: {values[0]:,} commits, +{values[1]:,} / -{values[2]:,} lines')
