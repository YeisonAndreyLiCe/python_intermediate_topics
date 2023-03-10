# Decorators

def upper(func: callable) -> callable:
    def wrapper(text: str) -> str:
        return func(text).upper()
    return wrapper

@upper
def message(text: str):
    return f'{text}, you have received a new message.'


class Car:
    def __init__(self):
        self.__color: str = 'red'
        self.__updateSoftware()

    def drive(self) -> None:
        print('driving')

    def __updateSoftware(self) -> None:
        print('updating software')


class Celsius:
    def __init__(self, temperature: float = 0):
        self.temperature: float = temperature

    def to_fahrenheit(self) -> float:
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self) -> float:
        """Get the current temperature."""
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


if __name__ == '__main__':
    print(message('Valentine')) # VALENTINE, YOU HAVE RECEIVED A NEW MESSAGE.
    red_car = Car()
    red_car.drive()
    red_car._Car__updateSoftware()

    c = Celsius(37)
    print(c.temperature)
    c.temperature = 37
    print(c.to_fahrenheit())
    print(c)
