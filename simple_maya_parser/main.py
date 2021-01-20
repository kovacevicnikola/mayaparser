import sys
from maya_parser import parse 
def main():
    filepath = sys.argv[1]
    parse(filepath)

        

if __name__ == '__main__':
    main()