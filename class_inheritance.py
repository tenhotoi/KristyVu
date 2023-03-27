# https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU

"""
The process of removing duplication by putting common code into
a superclass is called factoring out a superclass. This is the most common way that inheritance enters a codebase. Sometimes, opportunities for
inheritance are identified at the design stage, before coding begins.
"""
class Polygon:
    def __init__(self, sides, points):
        self._sides = sides
        self._points = list(points)
        if len(self._points) != self._sides:
            raise ValueError("Wrong number of points.")
    
    def sides(self):
        return self._sides

class Triangle(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 3, points)
    def __str__(self):
        return "I’m a triangle."

class Square(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 4, points)
    def __str__(self):
        return "I’m so square."

s = Square(4)
