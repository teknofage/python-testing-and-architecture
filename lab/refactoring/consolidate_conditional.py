# by Kami Bigdely
# Consolidate conditional expressions
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def lacks_ingredients(ingredients):
    if 'cucumber' not in ingredients or 'tomato' not in ingredients or 'onion' not in ingredients or 'lemon juice' not in ingredients:
        print('lacks ingredients.')
        return True
    else: 
        print ('You have all the ingredients.')
        return False
    
def make_shirazi_salad(ingredients):
    if lacks_ingredients(ingredients) == True:
        print('lacks ingredients.')
    else: 
        dice(ingredients)
        mix_all(ingredients)
        add_salt()
        pour('lemon juice')
        print('Your yummy shirazi salad is ready!')
    return

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])