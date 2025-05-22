def positional_argument_example(your_age, *args):
    return your_age, args

### Write your code below this line ###

about_me = positional_argument_example(21, 'musbi', 'jawo')

### Write your code above this line ###

print(about_me)
