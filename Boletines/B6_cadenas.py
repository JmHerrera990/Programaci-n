# """Ejercicio 1"""
# def acronimar (palabra):
#     acronimo=""
#     for i in range(len(palabra)):
#         if (palabra[i]==palabra[i].upper()) and not (palabra[i]==" "):
#             acronimo+=palabra[i]
#     return acronimo
# assert(acronimar("Elden Ring") == "ER")
# assert(acronimar("Hola muy Buneas") == "HB")
# assert(not (acronimar("Mbappe Dictateur mason") == "MDm"))
# print(acronimar("Elden Ring"))

# """Ejercicio 2"""
# def camel_Case_Converter (input):
#     output=""
#     for i in range(len(input)):
#         if input[i] != " " :
#             if input[i-1]==" ":
#                 output+=input[i].upper()
#             else:
#                 output+=input[i]
    
#     return output

# print(camel_Case_Converter("Mbappe dictador mason"))
# assert(camel_Case_Converter("Mbappe dictador mason") == "MbappeDictadorMason")
# assert(camel_Case_Converter("hola mundo cruel") == "holaMundoCruel")
# assert not(camel_Case_Converter("tu nombre empieza por la letra p") == "holaMundoCruel")

# """Ejercicio 3"""
# def calcular_suma(input):
#     numero=0
#     contador=0
#     for i in range(len(input)):
#         if input[i].isdigit() and i<len(input)-1:
#             if input[i+1].isdigit():
#                 numero=numero*10+int(input[i])
#             else:
#                 numero+=int(input[i])
#         else:
#             contador+=numero
#             numero=0
                 
#     return contador
# print(calcular_suma("abc12x3y450"))



# """Ejercicio 4"""

# def rotar_cadena(cadena,rotacion): 
#     return cadena[-rotacion:] + cadena[:-rotacion]

# assert(rotar_cadena("Mbappe" , 1) == "eMbapp")
# assert(rotar_cadena("Mbappe" , 2) == "peMbap")
# assert(rotar_cadena("Mbappe" , 3) == "ppeMba")
# assert(not rotar_cadena("Mbappe" , 3) == )

# """Ejercicio 5"""
# def charaterInString(input, caracter):
#     contador=0
#     for i in range(len(input)):
#         if caracter.upper()==input[i].upper():
#             contador+=1
#     return contador

# assert(charaterInString("MbapeeaaAa","a")==5)
# assert(charaterInString("MbapeeaaAa","e")==2)
# assert(charaterInString("Mbappe al madrid este verano","a")==4)
# assert (not charaterInString("Mbappe al madrid este verano","e")==0)

# """Ejercicio 6 """
# def lowCaselnString(cadena):
#     contador=0
#     for i in range(len(cadena)):
#         if cadena[i].islower():
#             contador+=1
#     return contador

# assert(lowCaselnString("Mbappe") == 5)
# assert(lowCaselnString("Mbappeeeeee") == 10)
# assert(lowCaselnString("MBAPEEEEE") == 0)
# assert(lowCaselnString("MBAPEEEEe") == 1)

# """Ejercicio 7"""
# def numberlnString (cadena):
#     contador=0
#     for i in range(len(cadena)):
#         if cadena[i].isdigit():
#             contador+=1
#     return contador

# assert(numberlnString("Mbappe") == 0)
# assert(numberlnString("Mbappee4eee9") == 2)
# assert(numberlnString("12345678") == 8)
# assert(numberlnString(" ") == 0)

# """Ejercicio 8"""
# def palindrome(cadena):
#     cadena_Inversa=""
#     auxiliar=""
#     for i in cadena:
#         if i!=" ": auxiliar+=i
#     for i in range(len(auxiliar)-1,-1,-1):
#         if auxiliar[i]!=" ":
#             cadena_Inversa+=auxiliar[i].lower()
#     return cadena_Inversa==auxiliar.lower()

# assert(palindrome("reconocer"))
# assert(palindrome("se es o no se es"))
# assert(palindrome("Sé verlas al revés"))
# assert(not palindrome("Mbappe"))

# """Ejercicio 9"""

# def encontrar_palabra_escondida (cadena,palabra_escondida):
#     j=0
#     contador=0
#     for i in range(len(palabra_escondida)):
#         encontrada=False
#         while (j<=len(cadena)) and encontrada==False : 
#             if palabra_escondida[i].upper()==cadena[j].upper():
#                encontrada=True
#                contador+=1
#             else: j+=1
#     return contador==len(palabra_escondida)

# assert(encontrar_palabra_escondida("supercalifragilisticoespialidoso","rapido"))
# assert(encontrar_palabra_escondida("supercalifragilisticoespialidoso","palicoss"))
# assert(not encontrar_palabra_escondida("MbapeeMadrileño","Maep"))

# """Ejercicio10"""
# def check_Amstrong_Number(numero):
#     cantidad=0
#     for i in range(len(numero)):
#         if numero[i].isdigit():
#             cantidad+=int(numero[i])**len(numero)

#     return cantidad==int(numero)


# assert(check_Amstrong_Number("153"))
# assert(check_Amstrong_Number("371"))
# assert(check_Amstrong_Number("93084"))
# assert(check_Amstrong_Number("407"))
# assert(not check_Amstrong_Number("12"))

# """Ejercicio11"""    
# def check_Amstrong_Number(numero):
#     cantidad=0
#     resultado=""
#     for i in range(len(numero)):
#         if numero[i].isdigit():
#             cantidad+=int(numero[i])**len(numero)
#     if cantidad==int(numero):
#         resultado=numero
#     return resultado

# def Amstrong_Numbrer_0_999():
#     cadena=""
#     for i in range(0,999):
#         if check_Amstrong_Number(str(i)) !="":
#             print (cadena)

# Amstrong_Numbrer_0_999()


# """Ejercicio12"""    
# def check_Amstrong_Number(numero):
#     cantidad=0
#     resultado=""
#     for i in range(len(numero)):
#         if numero[i].isdigit():
#             cantidad+=int(numero[i])**len(numero)
#     if cantidad==int(numero):
#         resultado=numero
#     return resultado

# def Amstrong_Numbrer_0_999(start,end):
#     cadena=""
#     for i in range(start,end):
#         if check_Amstrong_Number(str(i)) !="":
#             print (cadena)

# starting = int(input("Input starting number of range: "))
# ending = int(input("Input ending number of range: "))
# Amstrong_Numbrer_0_999(starting,ending)

# """Ejercicio13"""
# def replace_word(frase,contenido,remplazo):
#     mensaje=f"No existe |{contenido}| en |{frase}|"
#     if contenido.upper() in frase.upper():
#         mensaje=frase[:frase.upper().find(contenido.upper())]+remplazo+frase[frase.upper().find(contenido.upper())+len(contenido):]
#     return mensaje


# assert(replace_word("sueprcalifragilisticoespialidoso","lido","Eseba") == "sueprcalifragilisticoespiaEsebaso")
# assert(replace_word("Esternocleidomastoideo","cleido","EldenRing") == "EsternoEldenRingmastoideo")
# assert(replace_word("Quien es el mensajero de Dios","mensajero","goated") == "Quien es el goated de Dios")

"""Ejercicio14 TERMINAR"""
def replace_word(frase,contenido,remplazo):
    numero_sustituciones=0
    mensaje=f"No existe |{contenido}| en |{frase}|"
    mensaje=frase
    auxiliar=""
    letraActual=0
    while contenido.upper() in frase.upper()[letraActual:]:

    return mensaje


# assert(replace_word("sueprcalifragilisticoespialidoso","lido","Eseba") == "sueprcalifragilisticoespiaEsebaso")
# assert(replace_word("Esternocleidomastoideo","cleido","EldenRing") == "EsternoEldenRingmastoideo")
# assert(replace_word("Quien es el mensajero de Dios","mensajero","goated") == "Quien es el goated de Dios")

# """Ejercicio15"""
# def contar_vocales(cadena):
#     contador=0
#     for i in range(len("AEIOU")):
#         if "AEIOU"[i] in cadena.upper(): contador+=1
#     return contador

# assert (contar_vocales("Mbappe")==2)
# assert (contar_vocales("Mbappeu")==3)
# assert (contar_vocales("Mbappeuoooua")==4)
# assert (contar_vocales("Mbpp")==0)

# """Ejercicio16"""
# def contar_vocales(cadena):
#     contador=0
#     letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#     for i in range(len(letras)):
#         if letras[i] in cadena.upper(): contador+=1
#     return contador

# assert (contar_vocales("Mbappe")==5)
# assert (contar_vocales("Mbappeu")==6)
# assert (contar_vocales("Mbappeuoooua")==7)
# assert (contar_vocales("Mbpp")==3)

# """Ejercicio17"""
# def reconstruir_cadena(input):
#     vocales="AEIOU"
#     consonantes="BCDFGHJKLMNÑPQRSTVWXYZ"
#     frase_consonantes=""
#     frase_vocales=""
#     for i in input:
#         if i.upper() in consonantes: frase_consonantes+=i
#         elif i.upper() in vocales: frase_vocales+=i
#     return frase_consonantes+frase_vocales

# assert(reconstruir_cadena("curso de programacion")=="crsdprgrmcnuoeoaaio")
# assert(reconstruir_cadena("hola muy buenas tardes")=="hlmybnstrdsoauueaae")

# """Ejercicio 18"""
# def contar_palabras(input):
#     contador=0
#     inicio_palabra=False
#     for i in range(len(input)):
#         if input[i] !=" " and inicio_palabra==False : inicio_palabra=True
#         elif input[i] ==" " and inicio_palabra==True : 
#             inicio_palabra=False
#             contador+=1
#     if inicio_palabra==True : contador+=1
#     return contador

# assert(contar_palabras("He estudiado mucho")==3)
# assert(contar_palabras("No te lo crees ni tu")==6)
# assert(contar_palabras(" Elden ring es el goty game of the year del año ")==11)
# assert(contar_palabras("Eldenringeselgotygameoftheyeardelaño")==1)
