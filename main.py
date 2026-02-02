class Car:
    def __init__(self, number):
        self.number = number
        self.hours = 0


class Parking:
    def __init__(self, price_per_hour):
        self.price = price_per_hour
        self.cars = []
        self.cash = 0

    def enter(self, car):
        self.cars.append(car)

    def exit(self, index, hours):
        car = self.cars.pop(index)
        car.hours = hours
        cost = hours * self.price
        self.cash += cost
        print(f"{car.number} chiqdi. Narx: {cost}")

    def show(self):
        for i, c in enumerate(self.cars):
            print(i, c.number)

    def report(self):
        print("Daromad:", self.cash)


park = Parking(5000)

while True:
    print("\n1.Kirish 2.Chiqish 3.Mashinalar 4.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        park.enter(Car(input("Mashina raqami: ")))
    elif c == "2":
        park.exit(int(input("Index: ")), int(input("Soat: ")))
    elif c == "3":
        park.show()
    elif c == "4":
        park.report()
    elif c == "0":
        break
