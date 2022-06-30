#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


import sys

if __name__ == '__main__':

    for line in sys.stdin:
        lista = line.strip()
        lista = line.split()
        sys.stdout.write('{},{},{}\n'.format(lista[0], lista[1], lista[2]))
if __name__ == '__main__':
    
    for line in sys.stdin:
        letra = line.split(' ')[0]
        #fecha = line.split(' ')[3]
        val = line.split(' ')[-1]
        sys.stdout.write('{}\t{}\n'.format(letra,val))
