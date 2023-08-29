from pydantic import BaseModel


class Color(BaseModel):
    r: int = 0
    g: int = 0
    b: int = 0
    bright: int = 100

    def to_tuple(self):
        return (self.r, self.g, self.b, self.bright)


ColorType = tuple[int, int, int] | tuple[int, int, int, int] | int | Color


class Colors(BaseModel):
    offset: int = 0
    count: int = 0
    color: list[ColorType]
