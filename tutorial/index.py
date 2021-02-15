
class MyClass:
    def __init__(self):
        self.data = []

    i = 12345
    def f(self):
        return 'helloword'

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

a = MyClass()
b = MyClass()

a.i = 5
print(a.i, b.i)