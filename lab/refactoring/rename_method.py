# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def find_largest_value_in_list(li):  # TODO: Rename this function to reflect what it's doing.
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(find_largest_value_in_list(li))

############################
def separate_string_into_words(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(separate_string_into_words('If you were a vegetable, you’d be a ‘cute-cumber.'))