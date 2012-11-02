'''

@author: Jimmy John

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). 
The scalar product of these vectors is a single number, 
calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish. 
Choose two permutations such that the scalar product of your two new vectors is 
the smallest possible, and output that minimum scalar product.

More details at:

http://code.google.com/codejam/contest/dashboard?c=32016#s=p0

'''

import sys

def main():
    f = open(sys.argv[1], 'r')
    data = f.read().split('\n')

    num_of_test_cases = int(data[0])
    line_index = 1


    for i in range(num_of_test_cases):
        n = int(data[line_index])

        #sort one by increasing and the other by decreasing...
        #then the sum of their products will be minimum
        x_data = data[line_index + 1].split()
        x_data = map(lambda x: int(x), x_data)
        y_data = data[line_index + 2].split()
        y_data = map(lambda y: int(y), y_data)

        x_data.sort()
        y_data.sort()
        y_data.reverse()

        products = map(lambda a,b: a * b, x_data, y_data)
        print 'Case #%d: %d' % (i + 1, reduce(lambda x,y: x + y, products))

        line_index += 3

if __name__ == '__main__':
    main()

