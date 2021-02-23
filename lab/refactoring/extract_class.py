class Food:
    def __init__(self):
  
        foods = {'butternut squash soup':[45, True, 'soup','North African',\
            ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
                ,'1. Grill the butter squash, onion, carrot and garlic in the oven until'
                  'they get soft and golden on top 2. Put all in blender with'
                  'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
                      '. Add coconut milk. Simmer for 5 mintues.'],
                'shirazi salad':[5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
                    '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                        '4. Mixed them thoroughly'],
                'Home-made Beef Sausage': [60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
                    'corriander seeds','black pepper seeds','fennel seed','paprika'],'1. In a blender,'
                        ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                        'the seasonings 2. In a bowl, mix ground beef with the'
                        'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                        "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

class DecodeRecipe(Food):
    def __init__():
      self.name = food.key
      self.prep_time = food.value[0]
      self.is_vegetarian = food.value[1]
      self.food_type =  food.value[2]
      self.cuisine = food.value[3]
      self.ingredients = food.value[4]
      self.recipe = food.value[5]
    
class PrintRecipe(Food):
    def __init__():
      for key, value in foods.items():
          print("Name:", self.name)
          print("Prep time:",self.prep_time, "mins")
          print("Is Veggie?", 'Yes' if self.is_vegetarian  else "No")
          print("Food Type:", self.food_type)
          print("Cuisine:", self.cuisine)
          for item in self.ingredients:
              print(item, end=', ')
          print()
          print("recipe", self.recipe)
          print("***")
      return
