#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    
    min_ = 0
    
    for line in sys.stdin:
        key, val = line.split('\t')
        val = int(val)

        if min_ > val:
            min_ = val
            sys.stdout.write('{}\t{}\n'.format(key, min_))
        min_ = 0
    