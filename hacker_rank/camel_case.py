import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
S : split => plastic cup
C: combine => plasticcup
M => Method => plasticCup()
C => Class
V => Variable
"""
for line in sys.stdin:
    result = ""
    line = line.strip()
    method, type_of, string = line.split(";")
    if method == "S":
        if type_of == "M":
            for character in string:
                if character.isupper():
                    character = " " + character.lower()
                result += character
            sys.stdout.write(result[:-2])
            sys.stdout.write("\n")
        if type_of == "C":
            result += string[0].lower()
            for character in string[1:]:
                if character.isupper():
                    character = " " + character.lower()
                result += character
            sys.stdout.write(result)
            sys.stdout.write("\n")
        if type_of == "V":
            for character in string:
                if character.isupper():
                    character = " " + character.lower()
                result += character
            sys.stdout.write(result)
            sys.stdout.write("\n")
    if method == "C":
        toggle = False
        for character in string:
            if character != " " and not toggle:
                result += character
            elif character != " " and toggle:
                result += character.upper()
                toggle = False
            else:
                toggle = True
        if type_of == "M":
            sys.stdout.write(result + "()")
            sys.stdout.write("\n")
        elif type_of == "V":
            sys.stdout.write(result)
            sys.stdout.write("\n")
        else:
            sys.stdout.write(result.replace(result[0], result[0].upper()))
            sys.stdout.write("\n")
