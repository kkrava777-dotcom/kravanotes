class Printer:
    def __init__(self, name="Невідомий", speed=0, price=0,
                 year=2026, firm="Невідомо"):
        self.__name = name
        self.__speed = speed
        self.__price = price
        self.year = year
        self.firm = firm
    def get_name(self):
        return self.__name
    def get_speed(self):
        return self.__speed
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
    def __add__(self, obj2):
        return self.__speed + obj2.__speed
    def __lt__(self, obj2):
        return self.__speed < obj2.__speed
    def __str__(self):
        return (f"Назва: {self.__name}, швидкість: {self.__speed} "
                f"стор./хв, ціна: {self.__price} грн, "
                f"рік: {self.year}, фірма: {self.firm}")
    def __repr__(self):
        return (f"Printer('{self.__name}', {self.__speed}, "
                f"{self.__price}, {self.year}, '{self.firm}')")
    def __del__(self):
        print("Деструктор: об'єкт принтера видаляється")
def main():
    p1 = Printer()
    p2 = Printer("HP LaserJet", 25, 4500, 2025, "HP")
    p3 = Printer("Canon Pixma", 15, 3200, 2024, "Canon")

    print(p1 < p2)
    p2.set_price(5000)
    ps = [p1, p2, p3]
    print("Сума швидкостей:", p1 + p2)

    for p in ps:
        print(p)
        print("Назва через метод:", p.get_name())
        print("Швидкість через метод:", p.get_speed())
        print("Ціна через метод:", p.get_price())
        print("Публічні поля:", p.year, p.firm)
        print("Представлення об'єкта:", repr(p))
        print("-" * 50)
    p4 = Printer("Epson", 20, 2800, 2023, "Epson")
    print(p4)
    del p4
if __name__ == "__main__":
    main()
