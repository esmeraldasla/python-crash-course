def make_shirt(size, text):
    """Displays the size and the text of the t-shirt"""
    print(f"\nThe size of my shirt is {size.title()}.")
    print(f"The text I want in my shirt is: {text}")

make_shirt('P', 'Life is a gift.')

make_shirt(size='L', text='Work hard')