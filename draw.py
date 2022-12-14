from abc import ABC, abstractmethod
import numpy as np
from matplotlib import pyplot as plt, patches

class Shape:
        def __init__(self, color, x_position, y_position):
                self.color = color,
                self.x_position = x_position,
                self.y_position = y_position

        @abstractmethod
        def draw(self):
                pass

# Create object Circle
class Circle(Shape):

        def __init__(self, color, x_position, y_position, radius):
                super().__init__(color, x_position, y_position)

                self.__radius = radius

        def Draw(self):
                figure, axes = plt.subplots()
                Drawing_colored_circle = plt.Circle(( self.x_position , self.y_position ), self.__radius, color=self.color)
                axes.set_aspect( 1 )
                axes.add_artist( Drawing_colored_circle )
                plt.show()

# Create object Ellipsis
class Ellipsis(Shape):
        def __init__(self, color, x_position, y_position, Angle, width, height):
                super().__init__(color, x_position, y_position)

                self.__Angle = Angle
                self.__width = width
                self.__height = height

        def Draw(self):
                figure, axes = plt.subplots()
                Drawing_colored_Ellipsis = patches.Ellipse(( self.x_position , self.y_position ), self.__width,  self.__height, self.__Angle, color=self.color)
                axes.set_aspect( 1 )
                axes.add_artist( Drawing_colored_Ellipsis )
                plt.show()

# Create object Rectangle
class Rectangle(Shape):
        def __init__(self, color, x_position, y_position, width, height):
                super().__init__(color, x_position, y_position)

                self.__width = width
                self.__height = height
        
        def Draw(self):
                figure, axes = plt.subplots()
                Drawing_colored_Rectangle = patches.Rectangle((self.x_position, self.y_position), self.__width, self.__height, color=self.color)
                axes.set_aspect( 1 )
                axes.add_artist( Drawing_colored_Rectangle)
                plt.show()

Circle = Circle('blue', 0.6, 0.6, 0.2)
Ellipsis = Ellipsis('red', 0.5, 0.5,0, 0.6, 0.9) 
Rectangle = Rectangle('black', 0.2, 0.2, 0.2, 0.4) 

Circle.Draw()
Ellipsis.Draw()
Rectangle.Draw()


