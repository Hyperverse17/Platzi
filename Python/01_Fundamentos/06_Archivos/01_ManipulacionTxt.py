
fPath = "Fundamentos/06_Archivos/"
fName = "TierraLuna.txt"
fPointer = fPath + fName

# Leer archivos
with open(fPointer, 'r') as file: # Funcion 'r' solo para lectura
    for lineas in file:
        print(lineas.strip()) # El Metodo strip() elimina algunos saltos de linea innecesarios y da formato

#Leer todas las líneas en una lista
print("--- Lista ---")
with open(fPointer, 'r') as file:
    fileLines = file.readlines()
    print(fileLines)

#Añadir texto Al final
with open(fPointer, 'a') as file:
    file.write("\nWritten By: ChatGPT")

#Sobreescribir TODO el texto: Borra el texto y sobreescribe, 
with open(fPointer, 'w') as file: # Con laa funcion w, si el archivo no existe, lo crea 
    file.write("\nOh, no!")
