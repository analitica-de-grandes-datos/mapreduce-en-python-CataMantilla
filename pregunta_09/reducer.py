#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    lista1 = []

    for line in sys.stdin:
        key, val1, val2 = line.split(",")
        val2 = int(val2)

        lista1.append((key, val1, val2))

        lista1.sort(key=lambda i: i[2], reverse=False)

    for elemento in lista1[:6]:
        sys.stdout.write("{}   {}   {}\n".format(elemento[0], elemento[1], elemento[2]))
if __name__ == '__main__':
    
    min_ = 0
    
    for line in sys.stdin:
        key, val = line.split('\t')
        val = int(val)

        if min_ > val:
            min_ = val
            sys.stdout.write('{}\t{}\n'.format(key, min_))
        min_ = 0
    
