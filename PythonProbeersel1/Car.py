class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm doing {} kph man!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.odometer += self.speed
        self.speed -= 3
        self.time += 1

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time


if __name__ == '__main__':
    my_car = Car()
    print("I'm a car dude!")
    while True:
        action = input("What should I do? [A]ccelarate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know that command")
            continue # ends current iteration, starts next iteration
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
