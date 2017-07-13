# -*- coding:utf-8 -*-
__author__ = 'SpaceNet'
__status__ = "production"
__version__ = '1.0'
__date__    = '2017/7/12'

import re
import sys
import csv
import os.path

import factor

def main(argv):
    """
    input csvfile, output of kadai_3_2_1.py, whose name is in.csv formatted like 「2\n112\n34\n」
    output csvfile as out.csv formatted like 「2,2\n112,2,2,2,2,7\n2,17\n」
    Returns:
        None
    """
    if check_file('in.csv') == False: return
    try:
        f_in = open('in.csv', 'r')
        sys.stdout = open("mid.csv","w") #stdout to mid.csv
        num_list = []
        input_csvfile(num_list, f_in)

        sys.stdout.close()
        sys.stdout = sys.__stdout__ #stdout to console

        f_mid = open('mid.csv', 'r')
        f_out = open('out.csv', 'w')
        output_file(num_list, f_mid, f_out)

        close_file([f_in,f_mid,f_out])

    except Exception as e:
        print ("エラーが発生しました。")
        print (e)


def input_csvfile(num_list, f_in):
    """
    make mid.csv from input csvfile
    Returns:
        None
    """

    reader = csv.reader(f_in)
    for row in reader:
        num_list.append(row[0])
        row.insert(0,"kadai_3_2_1.py")
        kadai_3_2_1.main(row)

def output_file(num_list, f_mid, f_out):
    """
    make out.csv, formatted like 「2,2\n112,2,2,2,2,7\n2,17\n」, from mid.csv csvfile
    Returns:
        None
    """
    readlines_mid = f_mid.readlines()
    num = 0
    for row in readlines_mid:
        st = num_list[num] + "," + re.sub("\[|\]| ", "", row)
        f_out.writelines(st)
        num += 1
    print("出力ファイル（out.csv）を作成しました。")


def check_file(str):
    """
    input file check
    Returns:
        Boolean
    """
    file_exist = False
    try:
        if os.path.exists(str):
            f_check = open('in.csv', 'r')
            file_exist = True
            reader = csv.reader(f_check)
            for row in reader:
                if not row[0].isdigit() :
                    print("入力ファイル（in.csv）に整数以外の値が記入されておりエラーとなりました。")
                    return False
                if int(row[0]) < 2 :
                    print("入力ファイル（in.csv）に２以下の数字が記入されておりエラーとなりました。")
                    return False
            return True
        else:
            print ("入力ファイル（in.csv）が存在しません。in.csvを作成してください。")
            return False
    finally:
        if file_exist :
            f_check.close()


def close_file(file_list):
    """
    close file pointers
    Returns:
        None
    """
    for f in file_list:
        f.close()


if __name__ == '__main__':
    main(sys.argv)
