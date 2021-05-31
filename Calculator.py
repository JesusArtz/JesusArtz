while True:
    print("""Elije alguna de las dos opciones

    -> Calculadora de Areas = Areas. 
    -> Calculadora de Perimetros = Perimetros
    -> Calculadora de operaciones basicas = Calculadora""")

    opcion = input('Elije que calculadora quieres usar: ')

#Calculadora de areas

    if opcion == 'areas' or opcion == 'Areas':

        print("""CALCULADORA DE AREAS BY EL YISUS WAPO


            -> Elije "Cuadrado" para sacar el area del cuadrado

            -> Elije "Rectangulo" para sacar el area del rectangulo

            -> Elije "Triangulo" para sacar el area de un triangulo

            -> Elije "Circulo" para sacar el area de un circulo""")

        teclaPresionada = input('Ingresa la forma de la que quieras sacar el area: ') 

        if teclaPresionada == 'Cuadrado' or teclaPresionada == 'cuadrado':
            l1 = float(input('Ingresa la medida del lado: '))
            cuadrado = (l1*l1)
            print('El area de tu cuadrado es de: ',cuadrado)

        elif teclaPresionada == 'Rectangulo' or teclaPresionada == 'rectangulo':
            b = float(input('Ingresa la medida de la base de tu rectangulo: '))
            h = float(input('Ingresa la medida de la altura de tu rectangulo: '))
            rectangulo = (b*h)
            print('El area de tu rectangulo es: ',rectangulo)

        elif teclaPresionada == 'Triangulo' or teclaPresionada == 'triangulo':
            b = float(input('Ingresa la medida de la base de tu triangulo: '))
            h = float(input('Ingresa la medida de la altura de tu triangulo: '))
            triangulo = ((b*h)/2)
            print('El area de de tu triangulo es: ',triangulo)

        elif teclaPresionada == 'Circulo' or teclaPresionada == 'circulo':
            r = float(input('Ingresa la medida del radio de tu circulo: '))
            pi = (3.1416)
            circulo = (((r)**2)*pi)
            print('El area de tu circulo es: ',circulo)

        else:
            print('El valor que introduciste es incorrecto o aun no es agregado al codigo')
        
        #Calculadora operaciones basicas

    elif opcion == 'Calculadora' or opcion == 'calculadora':
        print("""Calculadora en Python wapo by el yisus
    
    Opciones disponibles:
    
    -> Ingrese "+" o "Sumar" para sumar dos numeros.
    
    -> Ingrese "-" o "Restar" para restar dos numeros.
    
    -> Ingrese "*" o "Multiplicar" para multiplicar dos numeros.
    
    -> Ingrese "/" o "Dividir" para dividir dos numeros.
    
    -> Ingrese 'salir' para finalizar.
    
    -> Ingrese 'Repetir' para mostrar el menu de nuevo.""")

        teclaPresionada = input("Presiona o teclea la accion que quieres realizar -> ")

        if teclaPresionada == 'Salir' or teclaPresionada == 'salir':
            print('Has elegido salir del programa')
             
    
        elif teclaPresionada == '+' or teclaPresionada == 'Sumar' or teclaPresionada == 'sumar':
            num1 = float(input('Inserta el valor del primer numero a sumar: '))
            num2 = float(input('Ingresa el valor del segundo numero a sumar: '))
            suma = (num1+num2)
            print('El resultado de tu suma es: ',suma)
            

        elif teclaPresionada == '-' or teclaPresionada == 'Restar' or teclaPresionada == 'restar':
            num1 = float(input('Ingresa el valor del primer numero a restar: '))
            num2 = float(input('Ingresa el valor del segundo numero a restar: '))
            resta = (num1-num2)
            print('El resultado de tu resta es: ',resta)
            

        elif teclaPresionada == '/' or teclaPresionada == 'Dividir' or teclaPresionada == 'dividir':
            try:
                num1 = float(input('Ingresa el valor del primer numero a dividir: '))
                num2 = float(input('Ingresa el valor del segundo numero a dividir: '))
                division = (num1/num2)
                print('El resultado de tu division es: ',division)
            except ZeroDivisionError:
                print("[ERROR] La división entre 0 no se puede realizar.")

        elif teclaPresionada == 'x' or teclaPresionada == 'Multiplicar' or teclaPresionada == 'multiplicar':
            num1 = float(input('Ingresa el valor del primer numero a multiplicar: '))
            num2 = float(input('Ingresa el valor del segundo numero a multiplicar: '))
            multiplicacion = (num1*num2)
            print('El resultado de tu multiplicacion es: ',multiplicacion)

        else:
            print('Lo siento, el valor que usted ingreso es incorrecto.')
            
            #Calculadora de perimetros
         
    elif opcion == "Perimetros" or opcion == "perimetros":
    
    
        print("""CALCULADORA DE PERIMETROS BY EL YISUS WAPO


            -> Elije "Cuadrado" para sacar el perimetro del cuadrado

            -> Elije "Rectangulo" para sacar el perimetro del rectangulo

            -> Elije "Triangulo" para sacar el perimetro de un triangulo

            -> Elije "Circulo" para sacar el perimetro de un circulo""")

        teclaPresionada = input('Ingresa la forma de la que quieras sacar el perimetro: ')

        if teclaPresionada == 'Cuadrado' or teclaPresionada == 'cuadrado':
            lado = float(input('Ingresa la medida del lado del cuadrado: '))
            perimetro = (lado*4)
            print('El perimetro de tu cuadrado es: ',perimetro)

        elif teclaPresionada == 'Rectangulo' or teclaPresionada == 'rectangulo':
            b = float(input('Ingresa el valor de la base de tu rectangulo: '))
            h = float(input('Ingresa el valor de la altura de tu rectangulo: '))
            perimetro = ((b*2)+(h*2))
            print('El perimetro de tu rectangulo es de: ',perimetro)

        elif teclaPresionada == 'Triangulo' or teclaPresionada == 'triangulo':
            a = float(input('Ingresa el valor del primer lado de tu triangulo: '))
            b = float(input('Ingresa el valor del segundo lado de tu triangulo: '))
            c = float(input('Ingresa el valor del tercer lado de tu triangulo: '))
            perimetro = (a+b+c)
            print('El perimetro de tu triangulo es de: ',perimetro)

        elif teclaPresionada == 'Circulo' or teclaPresionada == 'circulo':
            r = float(input('Ingresa el valor del radio de tu circulo: '))
            perimetro = ((r*2)*3.1416)
            print('El perimetro de tu circulo es: ',perimetro)

        else:
            print('No has elegido ninguna opcion valida o aun no es agregada al codigo.')

    else:
        print("Lo siento vuelve a intentarlo.")
