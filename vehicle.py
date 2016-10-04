

class Vehicle:
    '''A base class from which to inherit methods common to all Vehicles'''

    def maxPassengers(self):
        rows, seats_per_row = self.seat_layout()
        return rows * seats_per_row


class Minivan(Vehicle):
    '''Inherits from base class Vehicle'''

    def __init__(self, modelYear):
        self._modelYear = modelYear

    def model(self):
        return "Sierra"

    def seat_layout(self):
        return 2, 3


class PassengerBus(Vehicle):
    '''Inherits from base class Vehicle'''

    def __init__(self, modelYear):
        self._modelYear = modelYear

    def model(self):
        return "E-5000"

    def seat_layout(self):
        return 8, 6
