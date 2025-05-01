
import asyncio
import random

# Está simulando la descarga de tres archivos (file1.txt, file2.txt, file3.txt) de manera asíncrona, es decir, esperando sin bloquear el programa.
print()
async def donwload_process(file): # define una corutina: una función que puede ser pausada y reactivada más adelante.
    time = random.randint(1,10)
    print(f'Descargando archivo {file} ({time})')
    await asyncio.sleep(time) # await asyncio.sleep(time), espera ese tiempo sin bloquear.
    print(f'{file} downloaded')
    return file

async def main():
    print('Inicio de la descarga')
    results = await asyncio.gather(
        donwload_process('file1.txt'),
        donwload_process('file2.txt'),
        donwload_process('file3.txt')
    )
    print(results)

# El siguiente ejemplo es útil, sin embargo la ejecución no es simultánea
# async def main():
#    print('Inicio de la descarga')
#    result1 = await donwload_process('file1.txt') # pausa aquí, libera el control, y continúa cuando termine
#    result2 = await donwload_process('file2.txt')
#    result3 = await donwload_process('file3.txt')
#    print(f'{result1,result2,result3}')

asyncio.run(main())
