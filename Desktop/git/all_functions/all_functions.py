
class ImplementAbs:
    def __init__(self, string):
        self.string = string
    def __abs__(self):
        return self.string.lower()

custom_obj = ImplementAbs("HELLO")
print(abs(-3))
print(abs(custom_obj))