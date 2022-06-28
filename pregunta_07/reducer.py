#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    elements =[]

    def take_element(element):
        return(element.split('\t')[-1])

    def take_letter(element):
        return(element.split('\t')[0])
    
    for line in sys.stdin:
        elements.append(line)
    else:
        elements = sorted(elements, key = take_element)
        elements = sorted(elements, key = take_letter)

        for element in elements:
            sys.stdout.write(element)

