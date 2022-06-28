#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3
import sys
for line in sys.stdin:
    sys.stdout.write('{}\t1\n'.format(line.split(',')[2]))

