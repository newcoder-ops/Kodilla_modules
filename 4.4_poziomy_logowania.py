import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
# 2020-03-14 17:39:45,488 The program was called with this parameters ['1']

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
