# Method Overriding

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract Method"
        return
    
class circle(shape):
    def drawa(self):
        super().draw()
        print("Draw a circle")
        return
    
class rectangle(shape):
    def draw(self):
        super().draw()
        print("Draw a rectangle")
        return