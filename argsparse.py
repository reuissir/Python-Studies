# Creating CommandLineInterface with Argsparse


from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.Usage = 'Use it like this. '

parser.add_argument('a', type=int, help='The base value')
parser.add_argument('b', type=int, help='The base value')
parser.add_argument('-v', '--verbose', action = 'count',
                    help='Provides a verbose description. Use -vv for extra verbose')

args: Namespace = parser.parse_args()
result: int = args.a ** args.b

match args.verbose:
    case 1:
        print(f'The result is {result}')
    case 2:
        print(f'{args.a} ** {args.b} = {result}')

"""
parser.add_argument('square', help='Squares a given number', type=int, 
                    default=0, nargs='?')
parser.add_argument('-v', '--verbose',
                    help='Verbose description. Use -vv for extra verbose',
                    action='count')


args: Namespace = parser.parse_args(0)
result: int = args.square ** 2

if args.verbose == 1:
    print(f'The result is: {result}')
elif args.verbose == 2:
    print(f'{args.square} ** {args.square} = {result}')
else:
    print(result)
"""


# add arguments so user can interact with own script

"""
# simple argument where the interface will 'echo' what I type.
# (typing in the word, 'echo', is arbitrary)

parser.add_argument('echo', help='Echos the given string')

print(args.echo)

# type python argsparse.py {single word I want to echo}
# terminal will echo the word I typed 
"""

""" 
parser.add_argument('square', help='Squares a given number', type=int)

# positional arguments
parser.add_argument('-v', '--verbose', help='Provides a verbose desc',
                     type=int, choices=[0, 1, 2])

# creating a way of retrieving argument
args: Namespace = parser.parse_args()

if args.verbose == 0:
    print('Option 1')
elif args.verbose == 1:
    print('Option 2')
elif args.verbose == 2:
    print('Option 3')

print(args.square ** 2)
# you can decide to use -v or --verbose (optional)
# type python argsparse.py -v 2 in script

"""

