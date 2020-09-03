# -*- coding: utf-8 -*-
from opencc import OpenCC
import logging
import sys

def main():
    '''
        convert simplified Chinese file to traditional Chinese file line by line
    :return:
    '''
    if len(sys.argv) != 3:
        print("Usage: python " + sys.argv[0] + " input.txt output.txt")
        exit()

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    cc = OpenCC('s2tw')
    output = open(sys.argv[2], "w+", encoding='utf-8')  # w+: write to file and create if not exist
    logging.info("Start converting!")
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            line_num += 1
            output.write(cc.convert(line))
            if line_num % 10000 == 0:
                logging.info("已處理 %d 行" % line_num)
        output.close()
        f.close()

if __name__ == "__main__":
    main()
