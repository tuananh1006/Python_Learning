class Vechicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Move along..!')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vechicle('Telsa', 'Model_3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vechicle('Caddillac', 'Escaladae')
your_car.get_make_model()


class Airplane(Vechicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along')


class Truck(Vechicle):
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vechicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mask = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.moves()
cessna.get_make_model()

mask.moves()
mask.get_make_model()

golfwagon.moves()
golfwagon.get_make_model()

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
