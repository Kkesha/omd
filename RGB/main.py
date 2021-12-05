from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __rmul__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass


class Color(ComputerColor):
    """
    Класс реализует операции с цветами в формате RGB:
    сравнение, сложение, уменьшение контрастности
    """

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):

        if not(isinstance(red, int) and isinstance(green, int) and isinstance(blue, int)):
            raise TypeError('red, green, blue must be integer')

        if not(0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ValueError('red, green, blue must be between 0 and 255')

        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __add__(self, other):
        r = min(self.red + other.red, 255)
        g = min(self.green + other.green, 255)
        b = min(self.blue + other.blue, 255)
        return Color(r, g, b)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, ratio):
        cl = -256 * (1 - ratio)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        return Color(int(f * (self.red - 128) + 128), int(f * (self.green - 128) + 128),
                     int(f * (self.blue - 128) + 128))

    __rmul__ = __mul__


class HSLColor(Color):
    """
    Класс переводит цвет в формате HSL в формат RGB
    """

    def __init__(self, h, s, l):

        if not(0 <= h <= 360 and 0 <= s <= 1 and 0 <= l <= 1):
            raise ValueError('h must be between 0 and 360, l,s must be between 0 and 1')

        if s == 0:
            self.red = int(l)
            self.green = int(l)
            self.blue = int(l)

        else:
            h, s, l = [float(x) for x in (h, s, l)]

            if l < 0.5:
                q = l*(1 + s)
            else:
                q = l + s - l*s

            p = 2 * l - q

            def hsl_to_rgb(p, q, t):
                if t < 0:
                    t += 1
                if t > 1:
                    t -= 1
                if t < 1/6:
                    return p + (q - p) * 6 * t
                if t < 1/2:
                    return q
                if t < 2/3:
                    return p + (q - p) * (2/3 - t) * 6
                return p

            self.red = round(hsl_to_rgb(p, q, h/360 + 1/3) * 255)
            self.green = round(hsl_to_rgb(p, q, h/360) * 255)
            self.blue = round(hsl_to_rgb(p, q, h/360 - 1/3) * 255)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    print('Задание 1 и 2: вывод цвета и сравнение цветов')
    red = Color(255, 0, 0)
    print(red)
    green = Color(0, 255, 0)
    print(red == green)

    print('Задание 3: смешивание цветов')
    res = red + green
    print(res)
    print(res.red, res.green, res.blue)

    print('Задание 4: уникальные цвета')
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(*set(color_list))

    print('Задание 5: уменьшение контрастности')
    red = Color(255, 0, 0)
    print(0.5 * red)
    print(red * 0.5)

    print('Задание 6: класс HSL и вывод буквы А')
    red = HSLColor(0, 1, 0.5)
    print(red)

    print_a(red)
