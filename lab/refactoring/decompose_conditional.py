# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

def detect_toxins(ingredients):
    return (
        'sodium nitrate' in ingredients or 'sodium benzoate' 
        in ingredients or 'sodium oxide' in ingredients)

ingredients = ['sodium benzoate']
if detect_toxins(ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
        
detect_toxins(ingredients)