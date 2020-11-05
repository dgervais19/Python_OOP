# using __name__ and __main__

print("This is mod_1 name -->" + __name__)

def main():
    return " From mod 1 function"
   # pass # key word pass helps you to pass data without an error

# Syntax if __name__ == "__main__":
if __name__ == '__main__': # it checks whether the code is run from current file or not
    main()