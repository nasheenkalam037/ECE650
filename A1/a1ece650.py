import sys
import re
import operations


def main():
    while True:
        try:
            line=sys.stdin.readline()
            if line=='':
                break
            else:
                user_input=line.strip()
                check_validity_action(user_input)
        except Exception:
            print ("Error: Sorry. Something went wrong! Please try again.")
    sys.exit(0)


def check_validity_action(x):
    if re.match(r"^a\s+(\"(([\w]+)\s?)+\")\s+(((\(-?\d+,-?\d+\))\s?)\s?)+$", x):
        operations.add(x)
    elif re.match(r"^c\s+(\"(([\w]+)\s?)+\")\s+(((\(-?\d+,-?\d+\))\s?)\s?)+$", x):
        operations.change(x)
    elif re.match(r"^r\s+(\"(([\w]+)\s?)+\")\s?$", x):
        operations.remove(x)
    elif re.match(r"^g\s?$", x):
        operations.generateGraph()
    elif re.match(r"\n",x):
        print ('Error: Please input data.')
    else:
        print ('Error: Input format unrecognised.')


if __name__=='__main__':
    main()