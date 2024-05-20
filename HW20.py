class House:

    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors
        for i in range(0, 10):
            numberOfFloors += 1
            print("Текущий этаж равен", numberOfFloors)

name = House(10)