from apa102_pi.driver import apa102
from models import *


class Lights:
    def __init__(self, size: int) -> None:
        self.strip = apa102.APA102(num_led=size, bus_speed_hz=1000000)

    def shutdown(self) -> None:
        self.strip.clear_strip()
        self.strip.cleanup()

    def set_pixel_tuple(
        self, pos: int, colors: tuple[int, int, int] | tuple[int, int, int]
    ):
        if len(colors) < 3:
            raise ValueError("Invalid color")

        if len(colors) >= 3:
            r = colors[0]
            g = colors[1]
            b = colors[2]

        if len(colors) >= 4:
            bright = colors[3]
        else:
            bright = 100

        if type(r) is int and type(g) is int and type(b) is int and type(bright) is int:
            self.strip.set_pixel(pos, r, g, b, bright)
        else:
            raise TypeError()

    def set_pixel_color(self, pos: int, color: Color):
        self.set_pixel_tuple(pos, color.to_tuple())

    def set_pixel_int(self, pos: int, color: int):
        self.strip.set_pixel_rgb(pos, color)

    def set_pixel(self, pos: int, color: ColorType):
        if type(color) is tuple:
            self.set_pixel_tuple(pos, color)
        elif type(color) is Color:
            self.set_pixel_color(pos, color)
        elif type(color) is int:
            self.set_pixel_int(pos, color)
        else:
            raise TypeError("Invalid type for color: {}".format(type(color)))

    def set_pixels(self, colors: Colors):
        for i in range(colors.count):
            self.set_pixel(i + colors.offset, colors.color[i % len(colors.color)])

        self.strip.show()
