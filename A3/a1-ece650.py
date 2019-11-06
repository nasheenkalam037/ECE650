import sys
import re
import operations


def main():
    while True:
        try:
            line = sys.stdin.readline()
            if line == '':
                break
            else:
                #for lines in line:
                user_input=line.strip()
                check_validity_action(user_input)
        except Exception:
            sys.stdout.write ("Error: Sorry. Something went wrong! Please try again.")
            #sys.stdout.flush()
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
        sys.stdout.write ('Error: Please input data.'+'\n')
        sys.stdout.flush()
    else:
        sys.stdout.write ('Error: Input format unrecognised.'+'\n')
        sys.stdout.flush()


if __name__=='__main__':
    main()