
import os

print()
# 1. Obtener el directorio Actual
CWD = os.getcwd() # Current Working Directory
print("El directorio actual es: ", CWD)
print()

# 2. Listar
path = "./07_Bibliotecas/"

for file in os.listdir(path):
    print(file)

# 3. Listar con filtros usando Comprehension Lists
textFiles = [file for file in os.listdir(path) if file.endswith('.txt')]
print(textFiles)

# 4. Renombrar un archivo
os.rename(path + "TierraLuna.txt","TierraLunaJulioVerne.txt")
