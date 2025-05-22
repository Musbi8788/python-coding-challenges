def favorite_python(member=None):
    print(member)
    return member

### Call the favorite_python() function with the default argument changed to
### the name of your favorite Monty Python member, and assign that function
### call to the variable named my_choice.

my_choice = favorite_python(member='Django')
print(my_choice)

### Call the function above this line.
