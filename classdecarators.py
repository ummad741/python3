
class Vector:
    test=0
    test1=100    
    

    # classmethod class ichidage hamma narsaga dostup olib beradi uni keyi cls 
    # class ichida malumotlani filter va eventla qivotganda classmethod ishlatish kere chunku unda class ozida dostup bor
    @classmethod
    def validate(cls, arg):
        return cls.test <= arg <= cls.test1


    def __init__(self,x,y) -> None:
        self.x = self.y = 0

        if self.validate(x) and self.validate(y): # recomendet code with self
            self.x = x
            self.y = y
        
        #static methodi print qisa boladi obichniy functionlada
        print(self.kvadrat(self.x, self.y))
        
        # if Vector.validate(x) and Vector.validate(y): # bad code
        #     return 

        #! init hardoyim none jonatishi kerak ekan

        #   Traceback (most recent call last):
        #   File "/home/ummad741/Desktop/python3/classdecarators.py", line 31, in <module>
        #   v = Vector(1,1)
        #  TypeError: __init__() should return None, not 'str'
        

        
    def get_coord(self):
        return self.x,  self.y, "good"
    

    # static class bogliq bolmaganda va faqat ozini argumentalrdan tashqariga chiqmagan holda ishlani bajarish uchun qolaniladi
    @staticmethod 
    def kvadrat(x,y):
        return x*x, y*y



v = Vector(2,5)
print(Vector.kvadrat(2,4))
# res =Vector.get_coord(v)
# print(res)
