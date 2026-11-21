import sys

if len(sys.argv) != 3:
    print("Usage: python CLI_arg_inputs.py <first_name> <second_name>")
    sys.exit(1)

first_name = sys.argv[1]
second_name = sys.argv[2]
print("Hello", first_name, second_name)