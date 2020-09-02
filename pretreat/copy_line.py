from opencc import OpenCC
import logging
import sys


def main():
    '''
     sys.argv[0] = called pyfile
     sys.argv[1] = be copied file
     sys.argv[2] = copy to
     sys.argv[3] = lines to copy
    :return:
    '''

    if len(sys.argv) != 4:
        print("Usage: python3 " + sys.argv[0] + " D:\python\\nlp_tutorial")
        exit()

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.info("Copy with {0} line".format(sys.argv[3]))
    output = open(sys.argv[2], "w+", encoding='utf-8')  # w+: write to file and create if not exist
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            line_num += 1
            output.write(line)
            logging.info("finish line {0}".format(line_num))
            if line_num == int(sys.argv[3]):
                output.close()
                f.close()
                break

if __name__ == "__main__":
    main()
