from restaurant_module import Restaurant


restaurant = Restaurant('temax', 'mexican')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")
restaurant_2 = Restaurant('japa', 'japanese')
restaurant_2.describe_restaurant()

print("\n")
restaurant_3 = Restaurant('masalama','arab')
restaurant_3.describe_restaurant()