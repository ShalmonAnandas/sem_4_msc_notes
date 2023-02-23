class Area:
    def area(self, x=None, y=None):
        val_area = 0
        if(y==None):
            val_area = x**2
        else:
            val_area = x*y
        return val_area

obj = Area()
print("Area of Square: ",obj.area(6))
print("Area of Rectangle: ",obj.area(6,9))
