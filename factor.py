# -*- coding:utf-8 -*-
__author__ = 'SpaceNet'
__status__ = "production"
__version__ = '1.0'
__date__    = '2017/7/13'

import sys

def main(argv):
    """
    print the sum of all divisor of the argv
    Returns:
        None
    """
    try:
        if int(argv[1]) < 2 : raise ValueError("")
        given_num = [int(argv[1])]
        prime_list = [] # the list of prime number
        calcPrime(prime_list, given_num)
        prime_list.append(given_num[0])
        print(prime_list)
    except ValueError:
        argv[1] = input("素因数分解をしたい２以上の整数を入力してください：")
        main(argv)
    except IndexError:
        input_str = input("素因数分解をしたい２以上の整数を入力してください：")
        argv.insert(1,input_str)
        main(argv)


def calcPrime(prime_list, given_num):
    """
    calculate prime number and set to the number to prime_list
    Returns:
        None
    """
    check_num = 2
    while(check_num < given_num[0]):
        if ( given_num[0] % check_num ) == 0: setNumList(check_num, given_num, prime_list)
        check_num += 1


def setNumList(check_num, given_num, prime_list):
    """
    set two num, 'argv' and the result of 'argv / check_num' to list
    Returns:
        None
    """
    prime_list.append( check_num ) # the check_num is a prime number
    calc_result = given_num[0] / check_num
    given_num[0] = int(calc_result) # the result is a divisor
    calcPrime(prime_list, given_num)


if __name__ == '__main__':
    main(sys.argv)
