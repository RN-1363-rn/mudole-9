##################     example 1       ######################
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed, "km/h")
print("Current speed:", car.current_speed, "km/h")
print("Travelled distance:", car.travelled_distance, "km")


####################      example 2     ####################

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print("Current speed after accelerations:", car.current_speed, "km/h")

car1.accelerate(-200)

print("Final speed after emergency brake:", car.current_speed, "km/h")


#######################      example 3  ######################

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):

        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed:", car.current_speed, "km/h")
car.drive(1.5)

print("Travelled distance:", car.travelled_distance, "km")
car.accelerate(-200)

print("Final speed:", car.current_speed, "km/h")


####################### example 4   ##################

import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg, max_speed))

race_finished = False

while not race_finished:
    for car in cars:

        change = random.randint(-10, 15)
        car.accelerate(change)

        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
            break

# Print results
print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':<15}{'Distance':<12}")
print("-" * 50)

for car in cars:
    print(f"{car.registration_number:<10}{car.maximum_speed:<12}{car.current_speed:<15}{car.travelled_distance:<12.1f}")

    #######################################