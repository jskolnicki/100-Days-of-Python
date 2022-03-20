def add(*args):
    sum = 0
    for num in args:
        sum += num
    return(sum)


class Car:
    def __init__(self, **kw):
            self.make = kw.get('make')
            self.model = kw.get('model')
            self.color = kw.get('color')
            self.seats = kw.get('seats')


car_dict = {
    'make': 'Mazda',
    'model': 'Mazda6',
    'engine': 'V6',
}

car = Car(**car_dict)



class Human:
    def __init__(self, **kw):
        for key, value in kw.items():
            print(key, value)

human = Human(height = 75)


def test(*args):
    return(args)


print(type(test(1,3,4,5,6)))