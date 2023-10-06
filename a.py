import re       #Importar biblioteca de Expresiones Regulares
def expresion(nombre):          #Definir función: Expresión donde servirá para establecer la ER del nombre de la variable, recibiendo el mismo nombre
    expresion_regular =re.compile('[a-zA-Z_][\w_$]*[\w_$]*')    #Guardamos la expresión a revisar en la variable
    return re.match(expresion_regular, nombre) is not None      #Regresa si cumplió la coincidencia
def numero(da):                 #Definir función numero, recibiendo dato
    expresion_regular =re.compile('[0-9]*[0-9]$')   #Se guarda la ER a revisar en la variable
    return re.match(expresion_regular, da) is not None  #Si hubo coincidencia, la devuelve
def booleano(da):               #Definir funcion booleano, recibiendo dato
    expresion_regular =re.compile('[Verdadero|Falso]')  #Se guarda en la variable la ER a revisar
    return re.match(expresion_regular, da) is not None  #Si hay coincidencia, la devuelve

def Cadena(da):             #Definir función Cadena, recibiendo dato
    expresion_regular =re.compile('["][/w ]*["]$]') #Se guarda en variable la ER a revisar
    return re.match(expresion_regular, da) is not None  #Si hay coincidencia, se devuelve


def imprimir(tipo,nombre,dato,ide):         #Definir función imprimir, recibiendo los cuatro parámetros de la tabla palres
    print('Tipos       : ', tipo)       #Imprime
    print('Nombres     : ', nombre)     #Imprime
    print('Datos       : ', dato)       #Imprime
    print('Ides        : ', ide)        #Imprime
    print("\n")                         #Imprime



def main():     #Definimos clase main
    tipo = []       #Declaramos variable tipo lista
    nombre = []     #Declaramos variable tipo lista
    dato = []       #Declaramos variable tipo lista
    ide = []        #Declaramos variable tipo lista

    

    id = 1          #Declaramos variable tipo int
    ban=False       #Declaramos variable tipo booleano con FALSE
    filename = 'codigo.ikc'  # Abrimos el archivo creado con nuestra extensión
    x = 0  # contador de linea
    file = open("codigo.dep", "w")  # crea el archivo .dep
    tipoDatos = ['ent', 'cad', 'bool']      #Variable donde contiene las declaraciones de nuestro lenguaje
    operadores = ['*', '+', '-', '/']  # Variable donde contiene las declaraciones de nuestro lenguaje
    pesos = "$"

    datoBooleano=['Verdadero', 'Falso']     #Variable donde contiene los valores validos para nuestra declaración bool
    palres = ['Imprimir', 'Escribe', 'Ciclo', "Si"] #Variable donde contiene las palabras reservadas
    comentario = "**"               #Comentario donde guarda la declaración de como es un comentario
    comillas='"'                    #Guarda comillas
    imprecion="Imprimir ( "
    leer='Escribe'
    finleer = '()'
    finimp=' )'
    buscar=None

    with open(filename) as arch:        #Abrirá el documento para una variable arch
        b=True                  #Guarda TRUE
        for linea in arch:      #Ciclo donde linea esté en arch
            x = x + 1               #Variable que se guarda así misma más uno
            linea=linea.replace(' "' , '"')
            linea = linea.replace('" ', '"')
            linea = linea.replace(')', ' )')
            linea = linea.replace('( )', ' ()')
            linea = linea.replace("=", " = ")
            if linea.startswith("Imprimir( "):
                linea= linea.replace("Imprimir( ", "Imprimir ( ",1)
            if linea.startswith("Escribe. "):
                linea = linea.replace("Escribe. ", "Escribe . ",1)
            if linea.startswith("Imprimir ("):
                linea = linea.replace("Imprimir (", "Imprimir ( ",1)
            if linea.startswith("cad"):
                linea = linea.replace("cad", " cad ",1)
            if linea.startswith("bool"):
                linea = linea.replace("bool", " bool ", 1)
            if linea.startswith("ent"):
                linea = linea.replace("ent", " ent ",1)
            if linea.startswith("Escribe."):
                linea = linea.replace("Escribe.", "Escribe . ",1)
            linea = linea.rstrip()  #Remueve espacios sobrantes al final de la cadena
            linea = " ".join(linea.split()) #Une el contenido de linea con espacios luego de separarlo
            if (linea.startswith(comentario)):  #Decisión donde si linea inicia como en comentario
                linea = ""                  #La linea se le guarda nada
            else:           #Sino
                arreglolinea = linea.split()    #Separa la linea y el contenido lo guarda en arreglolinea
                #Declaracion
                
                ti = arreglolinea[0]            #ti guarda la palabra de declaración
                da=''                           #da guarda nada de momento
                if (ti in tipoDatos):           #Si ti está en tipoDatos, accede
                    no = arreglolinea[1]            #no guarda el nombre de la variable pocisionada en 1
                    if da in nombre:
                        posicion = nombre.index(da)
                        da = dato[posicion]
                        #print(da)
                    elif no in nombre:                #Si no está en nombre, accede
                        ban = True                      #ban es verdadero
                    else:                           #Sino
                        ban = False                     #ban es falso
                    asd=len(arreglolinea)           #asd contiene el contenido de arreglolinea
                    #print(asd)                      #Imprime asd
                    if ban == False:
                        if asd <=2:                     #Sí asd es menor igual a 2 (SOLO DECLARACIÓN)
                            parseo = str(id)                #parseo guardará ID como string
                            ides = "Id" + parseo            #ides almacena el texto ID y el numero del id
                            ide.append(ides)                #Agrega a lista ide, el ides
                            dato.append('')                 #Agrega a lista dato nada
                            nombre.append(no)               #Agrega a lista el nombre de la variable
                            tipo.append(ti)                 #Agrega a lista el tipo de la variable
                            id = id + 1                     #Aumenta ID
                            file.write(linea + "\n")  # Se escribe en el doc
                        else:                           #Sino
                            no = arreglolinea[1]            #no igual al nombre de la variable
                            if no in nombre:                #Si no está en nombre
                                ban = True                      #ban es VERDADERO
                            else:                           #Sino
                                ban = False                     #ban es FALSO
                            signo = arreglolinea[2]         #signo guarda el signo de la declaración para dar un valor
                            b = expresion(no)               #b guarda la coincidencia mandando no a revisar
                            if (no in tipoDatos or no in palres or no in datoBooleano): #Si el no es palabra reservada, imprime error
                                print("\n\nError uso una palabra reservada   " + no + " en la linea ", x)
                                print(SystemError)

                            else:                                                       #Sino
                                if (b == False):                                            #Si b es Falso, la variable no es valida e imprime error
                                    print("\n\nError nombre de variable no valida: " + no + " en la linea ", x)
                                    print(SystemError)

                                elif (ban == True):                             #Si ban es verdadero, es que ya está declarada
                                    print("\n\nError Volvio a declarar la variable: " + no + " en la linea ", x)
                                    print(SystemError)

                                elif (signo != "="):                            #Si signo es distinto al igual, imprime error dado que no es una asignación
                                    print("\n\nError expresion invalida en la linea: ", x)
                                    print(SystemError)

                                else:                                           #Sino
                                    da = arreglolinea[3]        #Se guarda a partir del dato de la línea en la pos 3 del arreglo
                                    if ti == "cad":             #Si ti es igual a cad
                                        # print("cadena")
                                        if da in nombre:
                                            posicion2 = nombre.index(da)
                                            da = dato[posicion2]
                                            print(da)

                                        c = 3                       #c guarda 4
                                        m = len(arreglolinea)       #m guarda lo largo del arreglolinea
                                        if c <= m:                   #Si c < m
                                            while (c != m):             #Mientras sea distinto
                                                da = da + " " + arreglolinea[c] #da se le suma su propio contenido más el próximo
                                                c = c + 1                       #Aumenta para el recorrido de guardarlo en da
                                        if (da.startswith(comillas) and da.endswith(comillas)): #Si da empieza y termina con comillas
                                            file.write(linea + "\n")  # Se escribe en el doc
                                            parseo = str(id)            #parseo guarda en formato string el ID
                                            ides = "Id" + parseo        #ides guarda el string Id y el número del ID al que van
                                            nombre.append(no)           #Se manda el no a la función nombre
                                            tipo.append(ti)             #Se manda el ti a la función tipo
                                            ide.append(ides)            #Se manda el ides a la función ide
                                            id = id + 1                 #Se suma en uno el id

                                        else:                       #Sino
                                            print("\n\nError dato incompatible en la linea ", x)    #Imprime error
                                            print(SystemError)

                                    elif (ti == "bool"):        #Si ti es igual a la declaración bool
                                        # print("booleano")
                                        if da in nombre:
                                            posicion2 = nombre.index(da)
                                            da = dato[posicion2]
                                            print(da)

                                        nv = booleano(da)  # nv guarda en booleano da
                                        # print(nv)
                                        if (nv == True):  # Si es TRUE
                                            file.write(linea + "\n")  # Se escribe en el doc
                                            dato.append(da)  # Se manda da a  la función dato
                                            parseo = str(id)  # parseo guarda en string el id
                                            ides = "Id" + parseo  # Guarda el string más el parseo
                                            nombre.append(no)  # Manda no a la función nombre
                                            tipo.append(ti)  # Se manda el ti a la función tipo
                                            ide.append(ides)  # Se manda el ides a la función ide
                                            id = id + 1  # Se suma en uno el id
                                        else:  # Sino, imprime error
                                            print("\n\nError dato incompatible en la linea ", x)
                                            print(SystemError)

                                    elif (ti == "ent"):         #Si ti es igual a ent
                                        # print("entero")
                                        if da in nombre:
                                            posicion2 = nombre.index(da)
                                            da = dato[posicion2]
                                            print(da)

                                        nv = True  # Se hace VERDADERO
                                        nv = numero(da)  # Guarda la validación de un numero
                                        # print(nv)
                                        if (nv == True):  # Si es igual a TRUE
                                            file.write(linea + "\n")  # Se escribe en el doc
                                            dato.append(da)  # Se manda da a  la función dato
                                            parseo = str(id)  # parseo guarda en string el id
                                            ides = "Id" + parseo  # Guarda el string más el parseo
                                            nombre.append(no)  # Manda no a la función nombre
                                            tipo.append(ti)  # Se manda el ti a la función tipo
                                            ide.append(ides)  # Se manda el ides a la función ide
                                            id = id + 1  # Se suma en uno el id
                                        else:  # Sino, imprime error
                                            print("\n\nError dato incompatible en la linea: ", x)
                                            print(SystemError)

                                    else:  # Sino, imprime error
                                        print("\n\nError dato incompatible en la linea: ", x)
                                        print(SystemError, "\n\n\n")
                    else:  # Sino, imprime error
                        print("\n\nError la variable ya esta declarada en la linea: ", x)
                        print(SystemError)


            

                #palabras reservadas
                elif (arreglolinea[0] in palres):           #Si la primera palabra es palres
                    y = 0
                    print("linea: ", x, "Es palabra una palabra reservada")     #Imprime confirmación
                    if (linea.startswith(imprecion) and linea.endswith(finimp)):
                        c = 2  # c guarda 3
                        m = len(arreglolinea)-1  # m guarda lo largo del arreglolinea
                        a=False
                        if arreglolinea[2] in nombre:  # Si esa parte pertenece a nombre
                            a = True  # Guarda verdadero
                        else:  # Sino
                            a = False  # Guarda falso
                        if a == True:  # Si a es verdadero
                            print("es imprecion")
                            linea = linea.replace("Imprimir ( ", "Imprimir( ")
                            file.write(linea + "\n")
                        elif(arreglolinea[2].startswith(comillas) and arreglolinea[2].endswith(comillas)):
                            if c <= m:  # Si c < m
                                while (c != m):  # Mientras sea distinto
                                    #   msj = msj + " " + arreglolinea[c]  # da se le suma su propio contenido más el próximo
                                    c = c + 1  # Aumenta para el recorrido de guardarlo en da
                                    buscar=re.findall(r'"[\w]*"', linea)
                           #print (buscar)
                            #print(buscar1)
                            if ( buscar[0]  in linea):
                                print("es imprecion")
                                linea = linea.replace("Imprimir (  ", "Imprimir(")
                                file.write(linea + "\n")
                            else:
                                print("\n\nError de codigo en la linea ", x,"\n\n")
                                print(SystemError)
                        else:
                            print("\n\nError de codigo en la linea ", x,"\n\n")
                            print(SystemError)

                    elif(linea.startswith(leer)):
                        buscador = arreglolinea[2]  # Guarda la declaración de la variable
                        if buscador in nombre:  # Si esa parte pertenece a nombre
                            if(linea.endswith(buscador)):
                                print("Es lectura","\n\n\n")
                                linea = linea.replace("Escribe . ", "Escribe.")
                                file.write(linea + "\n")
                            else:  # Sino
                                print("\n\nError de codigo en la linea:  ", x)
                                print(SystemError,"\n\n")
                        else:  # Sino
                            print("\n\nError la variable no existe en la linea:  ", x)
                            print(SystemError, "\n\n")
                    else:
                        print("\n\nError de codigo en la linea ", x,"\n\n")
                        print(SystemError)

                ##asignacion
                elif (arreglolinea[1] != '='):              #Si la segunda parte es un simbolo, imprime error
                    print("\n\nError de codigo en la linea ", x,"\n\n")
                    print(SystemError)
                else:                               #Sino
                    da=''                               #da guarda nada
                    buscador = arreglolinea[0]          #Guarda la declaración de la variable
                    if arreglolinea[0] in nombre:       #Si esa parte pertenece a nombre
                        posicion = nombre.index(buscador)   #Guarda la posición
                        a = True                            #Guarda verdadero
                    else:                               #Sino
                        a = False                           #Guarda falso
                    if a == True:                       #Si a es verdadero
                        #print("\nLa variable existe")
                        tip=tipo[posicion]                  #tip guarda la posición de tipo
                        if tip == "cad":                    #Si tip es igual a cad
                            #print(da)
                            da=arreglolinea[2]                  #da guarda la información de arreglolineazz
                            if da in nombre:
                                posicion2 = nombre.index(da)
                                da=dato[posicion2]
                            #print(da)
                            c = 3  # Guarda un 3
                            m = len(arreglolinea)  # m guarda lo largo del arreglolinea
                            if c <= m:  # Si c es menor que m
                                while (c != m):  # Mientras sean distintos
                                    da = da + " " + arreglolinea[c]  # da suma su contenido más lo nuevo
                                    c = c + 1  # Aumenta nuestro apuntador
                                #print(da)
                            if (da.startswith(comillas) and da.endswith(comillas)):  # Si inicia y termina con comillas
                                dato[posicion] = da  # Se guarda lo de da en pato y pósición
                                file.write(linea + "\n")  # Se escribe en el doc
                            else:  # Sino, imprime error
                                print("\n\nError dato incompatible linea: ", x)
                                print(SystemError)


                        elif(tip=="bool"):          #Si tip es igual a bool
                            da = arreglolinea[2]        #da guarda el dato
                            if da in nombre:
                                posicion2 = nombre.index(da)
                                da=dato[posicion2]
                               # print(da)
                                #print("booleano")
                            nv = booleano(da)  # Manda da a booleano y lo guarda en nv
                            # print(nv)
                            if (nv == True):  # Si nv es TRUE
                                dato[posicion] = da  # Se guarda da
                                file.write(linea + "\n")  # Se escribe en el doc
                            else:  # Sino, imprime error
                                print("\n\nError dato incompatible en la linea ", x)
                                print(SystemError)

                        elif(tip=="ent"):           #Si tip es igual a ent
                            a = arreglolinea[2]  # Guarda la info
                            asad = len(arreglolinea)
                            print(asad)
                            if (asad == 5) :
                                isInt = numero(arreglolinea[2])
                                isInt2 = numero(arreglolinea[4])
                                posicion3 = nombre.index(arreglolinea[0])
                                arreglolinea[0] = ide[posicion3]
                                if (arreglolinea[3] in operadores):

                                    if (isInt == True ):
                                        ide1 = arreglolinea[2]  # Guarda la info

                                    else:
                                        if (arreglolinea[2] in nombre):
                                            posicion3 = nombre.index(arreglolinea[2])
                                            ide1 = ide[posicion3]
                                        else:
                                            print("\n\nError dato incompatible en la linea", x)
                                            print(SystemError)
                                    if (isInt2 == True):
                                        ide2 = arreglolinea[4]  # Guarda la info

                                    else:
                                        if (arreglolinea[4] in nombre):
                                            posicion3 = nombre.index(arreglolinea[4])
                                            ide2 = ide[posicion3]
                                        else:
                                            print("\n\nError dato incompatible en la linea", x)
                                            print(SystemError)
                                    linea = arreglolinea[0] + arreglolinea[1] + ide1 + arreglolinea[3] + ide2   #Da forma de la linea | id = id + id
                                    file.write(linea + "\n")  # Se escribe en el doc

                            else:
                                da = arreglolinea[2]  # Guarda la info
                                if da in nombre:
                                    posicion2 = nombre.index(da)
                                    da = dato[posicion2]
                                # print (da)
                                nv = True  # nv se hace TRUE
                                nv = numero(da)  # Guarda la coincidencia del ER
                                # print (nv)
                                if (nv == True):  # Si nv es TRUE
                                    dato[posicion] = da  # Se guarda a dato el da
                                    file.write(linea + "\n")  # Se escribe en el doc
                                else:  # Sino, imprime error
                                    print("\n\nError dato incompatible en la linea", x)
                                    print(SystemError)

                            if da in nombre:  # Verifica que la variable exista para tomar el valor
                                posicion2 = nombre.index(da)
                                da = dato[posicion2]
                                nv = True  # nv se hace TRUE




                    elif a == False:        #Si a es falso, imprime error
                        print("\n\nError de codigo en la linea ",x)
                        print(SystemError)
        imprimir(tipo, nombre, dato, ide)   #Se hace la impresión de la tabla
    file.close      #El documento se cierra
main()          #Termina el main