def make_shirt(size='L', text='I love Python'):
    """Displays the size and the text of the t-shirt"""
    print(f"\nThe size of my shirt is {size.title()}.")
    print(f"The text I want in my shirt is: {text}")

make_shirt()
make_shirt(size='M')
make_shirt(size='P', text='Java is hard')