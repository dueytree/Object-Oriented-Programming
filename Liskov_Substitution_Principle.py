# 'A는 B다' 라는 상속관계에서 A가 B의 행동규약을 지키는 것까지 생각해야한다.

# class Rectangle:
#     """직사각형 클래스"""
#
#     def __init__(self, width, height):
#         """세로와 가로"""
#         self.width = width
#         self.height = height
#
#     def area(self):
#         """넓이 계산 메소드"""
#         return self.width * self.height
#
#     @property
#     def width(self):
#         """가로 변수 getter 메소드"""
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         """가로 변수 setter 메소드"""
#         self._width = value if value > 0 else 1
#
#     @property
#     def height(self):
#         """세로 변수 getter 메소드"""
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         """세로 변수 setter 메소드"""
#         self._height = value if value > 0 else 1
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     @property
#     def width(self):
#         """가로 변수 getter 메소드"""
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         """가로 변수 setter 메소드"""
#         self._width = value if value > 0 else 1
#         self._height = value if value > 0 else 1
#
#     @property
#     def height(self):
#         """세로 변수 getter 메소드"""
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         """세로 변수 setter 메소드"""
#         self._width = value if value > 0 else 1
#         self._height = value if value > 0 else 1
#
# rectangle_1 = Rectangle(4, 6)
# rectangle_2 = Square(2)
# rectangle_1.width = 3
# rectangle_1.height = 7
# print(rectangle_1.area())
# rectangle_2.width = 3
# rectangle_2.height = 7
# print(rectangle_2.area())


class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        """정사각형 넓이 계산 메소드"""
        return self.side * self.side
    @property
    def side(self):
        """한 변 getter 메소드"""
        return self._side
    @side.setter
    def side(self, value):
        """한 변 setter 메소드"""
        self._side = value if value > 0 else 1

rectangle_1 = Rectangle(4, 6)
square = Square(2)
rectangle_1.width = 3
rectangle_1.height = 7
print(rectangle_1.area())
square.side = 10
print(square.area())
