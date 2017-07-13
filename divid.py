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
        if int(argv[1]) < 0 : raise ValueError("")
        given_num = [int(argv[1])]
        divisor_list = [] # the list of divisor
        check_num = 1
        while(check_num <= given_num[0]):
            if ( given_num[0] % check_num ) == 0: setDivisor(check_num, given_num, divisor_list)
            check_num += 1
        print(sum(divisor_list))
    except ValueError:
        argv[1] = input("約数の総和を出したい数字（正の整数）を入力してください：")
        main(argv)
    except IndexError:
        input_str = input("約数の総和を出したい数字（正の整数）を入力してください：")
        argv.insert(1,input_str)
        main(argv)

def setDivisor(check_num, given_num, divisor_list):
    """
    set two num, 'argv' and the result of 'argv / check_num' to list
    Returns:
        None
    """
    calc_result = given_num[0] / check_num
    if (check_num != calc_result and check_num < calc_result) :
        divisor_list.append( check_num )
        divisor_list.append( int(calc_result) ) # the result is a divisor

if __name__ == '__main__':
    main(sys.argv)
