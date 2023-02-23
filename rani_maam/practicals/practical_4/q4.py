class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        cir_area = 3.14 * (self.radius**2)
        return cir_area
    def perimeter(self):
        cir_peri = 2 * 3.14 * self.radius
        return cir_peri

obj = Circle(7)
print("Area of circle: ", obj.area())
print("Perimeter of circle: ", obj.perimeter())
