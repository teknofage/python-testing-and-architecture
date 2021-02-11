# By Kami Bigdely
"""
PEP8 - Refactor code by removing unnecessary whitespaces, adding docstrings, 
and formalizing variable names.
"""
class pizza:
    """
    Class for creating pizza objects
    """
    def __init__ (self, bread_type, cheese_type, meat_type, pizza_toppings, size):
        self.bread= bread_type
        self.cheese = cheese_type
        self.meat= meat_type
        self.toppings = pizza_toppings
        self.size = size     

    @classmethod
    def create_chicago_pizza (self, class_type, size):
        """creates an instance of a chicago pizza"""
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat = 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return class_type (bread, cheese, meat, toppings, size)  
        
    @classmethod
    def create_california_pizza(self, meat, size):
        """creates aninstance of a california pizza"""
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings =[ 'garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper' ]
        return self (bread, cheese, meat, toppings, size) 

    def print_info(self):
        """prints info about the pizza"""
        print('bread type is: ', self.bread)
        print('cheese type is: ', self.cheese)
        print('meat type is: ', self.meat)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))

    
myPizza = pizza.create_california_pizza('chicken', 'large')
myPizza.print_info()