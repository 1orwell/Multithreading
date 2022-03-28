class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2*(self.width + self.length)

    def what_am_i(self):
        return 'Rectangle'

class Square(Rectangle):
    def __init__(self, length):
        super.__init__(self, length, length)

    # Overide parent method
    def what_am_i(self):
        return 'Square'

class Cube(Square):
    # Same paratemter as square, no need to redefine __init__

    def surface_area(self):
        # when python doesn't find the area function in Cube, it will check Square, then Rectangle
        face = self.area()
        return 6*face

    def volume(self):
        # Here, python doesn't check Cube for the method area, it goes straight to Sqaure, then Rectangle
        face = super.area()
        return face * self.length

    # Overide parent method
    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return self.what_am_i + ' child of ' + super().what_am_i

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'

# Multiple inheretence
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return 'Right Pyramid'