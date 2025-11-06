class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if (self.a > other.a):
            return "A is greater than B"
        else:
            return "A is less than B"
    def __eq__(self, other):
        if (self.a == other.a):
            return "A is equal to B"
        else:
            return "A is not equal to B"
        
ob1 = A(2)
ob2 = A(3)
print("Passed Values:", ob1.a, ob2.a)
print(ob1 > ob2)
print(ob1 == ob2)

ob3 = A(9)
ob4 = A(5)
print("Passed Values:", ob1.a, ob2.a)
print(ob3 > ob4)
print(ob3 == ob4)