'''

@author: Jimmy John

Given a list of space separated words, reverse the order of the words. Each 
line of text contains L letters and W words. A line will only consist of letters 
and space characters. There will be exactly one space character between each pair 
of consecutive words.

More details at:

http://code.google.com/codejam/contest/351101/dashboard#s=p1

'''

import sys

def helper_reverse(line):
    rev_line = list(line)
    rev_iterator = len(line) - 1

    for i in range(len(line)):
        if i >= rev_iterator:
            break
        rev_line[i], rev_line[rev_iterator] = rev_line[rev_iterator], rev_line[i]
        rev_iterator -= 1

    return ''.join(rev_line)

def reverse(line):

    second_pass = []
    first_pass = helper_reverse(line)
    for word in first_pass.split(' '):
        second_pass.append(helper_reverse(word))

    return ' '.join(second_pass)


def main():
    f = open(sys.argv[1], 'r')
    data = f.read().split('\n')

    num_of_test_cases = int(data[0])
    line_index = 1


    for i in range(num_of_test_cases):
        rev = reverse(data[line_index])
        print 'Case #%d: %s' % (line_index, rev)
        line_index += 1

if __name__ == '__main__':
    main()

