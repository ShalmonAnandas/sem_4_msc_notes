class StringMethods:
    def __init__(self):
        in_string = ""
    def get_String(self):
        self.in_string = input("Enter a string:")
    def print_String(self):
        print(self.in_string)

obj = StringMethods()
obj.get_String()
obj.print_String()
