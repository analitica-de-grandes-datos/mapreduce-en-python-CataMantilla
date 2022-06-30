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

        lista1.sort(key=lambda i: (i[0], i[2]), reverse=False)

    for elemento in lista1:
        sys.stdout.write("{}   {}   {}\n".format(elemento[0], elemento[1], elemento[2]))
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

