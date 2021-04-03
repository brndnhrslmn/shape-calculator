class Rectangle:

    # instance attributes
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, reset) -> float:
        self.width = reset
        return

    def set_height(self, reset) -> float:
        self.height = reset
        return

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self) -> float:
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self) -> str:
        if self.width < 50 and self.height < 50:
            across = self.width * '*'
            picture = (across + '\n') * self.height
            return picture
        else:
            return 'Too big for picture.'

    def get_amount_inside(self, shape):
        if shape.width < self.width and shape.height < self.height:
            width_sq = int(self.width / shape.width)
            height_sq = int(self.height / shape.height)
            return width_sq * height_sq
        else:
            return 0


class Square(Rectangle):

    # instance attributes
    def __init__(self, side) -> None:
        Rectangle.width = side
        Rectangle.height = side

    def __str__(self) -> str:
        return f'Square(side={self.width})'

    def set_side(self, side) -> None:
        self.width = side
        self.height = side
        return

    def set_width(self, reset) -> None:
        self.set_side(reset)
        return

    def set_height(self, reset) -> None:
        self.set_side(reset)
        return
