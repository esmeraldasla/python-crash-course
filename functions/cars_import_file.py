def car(manufacturer, model, **options):
    print("\nCar information:")
    car_info = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_info[option] = value

    return car_info