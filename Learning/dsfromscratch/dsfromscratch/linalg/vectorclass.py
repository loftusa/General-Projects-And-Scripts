# Make list of numbers
height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]

class VList(list):
    """ Normal list, but addition and multiplication works vector-wise. 
        TODO:  __add__, __mul__, inherit from `list` properly"""

    def __init__(self, *args):
        self.v = [*args]

    def __repr__(self):
        return str(self.v)

    def __add__(self, other):
        """ Elementwise addition. VList(1, 2, 3) + VList(4, 5, 6) should produce VList(5, 7, 9) """
        return [i[0] + i[1] for i in zip(self.v, other.v)]

    def __mul__(self, scalar):
        """ Matrix multiplication by scalar. VList(1, 2, 3) * 5 should produce VList(5, 10, 15) """ 
        pass