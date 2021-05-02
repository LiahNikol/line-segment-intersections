# Superclass for Endpoint and Intersection object types
from functools import total_ordering

@total_ordering
class Event:
    def __init__(self, x, y):
        self.x = x # x coordinate of the intersection
        self.y = y # y coordinate of the intersection
        
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")" 
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
  
    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        return False

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
    
    
    def coords(self):
        return (self.x, self.y)
    