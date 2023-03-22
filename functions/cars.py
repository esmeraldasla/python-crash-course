"""Write a function that stores information about a car in a dictionary. The function should always receive a
manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with
the required information and two other name-value pairs, such as a color or an optional feature. """

def car(manufacturer, model, **options):
    print("\nCar information:")
    car_info = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_info[option] = value

    return car_info

my_new_car = car('porshe', 'moon', color='black', year=2019)
print(my_new_car)

old_car = car('audi', "A4", category='sedan', year=2019)
print(old_car)
