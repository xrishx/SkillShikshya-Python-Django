# Method Overriding

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract Method"
        return
    
class circle(shape):
    def draw(self):
        super().draw()      # Using super() to call the parent method
        print("Draw a circle")
        return
    
class rectangle(shape):
    def draw(self):
        super().draw()      # Using super() to call the parent method
        print("Draw a rectangle")
        return
    
shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()
