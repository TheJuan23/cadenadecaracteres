#String Concatenation
text1 = "Fundamentos con "
text2 = "python "
#text3 = str(5)
result = text1 + text2
print(result)

name = "juan"
lastName = "carmona"
fullName = name + " " + lastName
print(fullName)

#Format String
price = 97
text3 = f"El precion es {price: .2f} dolares"
print(text3)

#math operation
text4 = f"La multiplicacion es {20*59} "
print(text4)

#String capataliza()
text5 = "cualquier cosa aqui"
result1 = text5.capitalize()
print(result1)

#String casefold()
title = "CIEN AñOS dE SoleDAD"
titleConvert = title.casefold()
print(titleConvert)

#String center()
fruit = "Banana"
textCenter = fruit.center(20,"-")
print(textCenter)

#String count()
title1 = "yo amo las manzanas, la manzana es mi fruta favorita"
result2 = title1.count("manzana")
print(result2)

#String endswith
text6 = "curso, fundamentos con Python."
result3 = text6.endswith(".")
print(result3)

#String expandtabs
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#String find
text7 = "Hola, bienvenidos a Polombia"
result4 = text7.find("bienvenidos")
print(result4)

#funcion title
text8 = "welcome to my world"
result5 = text8.title()
print(result5)

#Funcion isalnum
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

#Funcion isalpha
letters = "space x"
result7 = letters.isalpha()
print(result7)