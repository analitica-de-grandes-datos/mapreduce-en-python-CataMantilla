#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from statistics import mean
import sys

if __name__ == '__main__':
    
    curkey = None
    total = 0
    suma = 0
    media = 0
    
    
    for line in sys.stdin:

        key, contador, val = line.split('\t')
        contador = int(contador)
        val = float(val)

        if key == curkey:
            total += contador
            suma += val
            media =suma/total

        else:
            if curkey is not None:
                sys.stdout.write('{}\t{}\t{}\n'.format(curkey, suma, media))
            curkey = key
            suma = val
            media = val
            total = contador
            
            
    sys.stdout.write('{}\t{}\t{}\n'.format(curkey, suma, media))