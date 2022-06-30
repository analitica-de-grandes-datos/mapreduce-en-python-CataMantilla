#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
from datetime import datetime

if __name__ == '__main__':
    
    for line in sys.stdin:
        lista = line.split(' ')[3]
        lista = line.split('-')[1]
        sys.stdout.write('{}\t1\n'.format(lista))