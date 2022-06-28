#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from platform import mac_ver
import sys

if __name__ == '__main__':
    curkey = None
    max_ = 0
    min_ = 0
    
    for line in sys.stdin:
            key, val = line.split(',')
            val =float(val)
            key = str(key)

            if curkey == key:
                if max_ < val:
                    max_ = val
                
            else:
                if curkey is not None:
                    if min_ > val:
                        min_ =val
                sys.stdout.write('{}\t{}\t{}\n'.format(curkey, max_, min_))
            curkey = key
            max_ = val
            min_ = val


    sys.stdout.write('{}\t{}\t{}\n'.format(curkey, max_, min_))    
                
   
            
