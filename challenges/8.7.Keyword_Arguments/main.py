def keyword_argument_example(your_age, **kwargs):
    return your_age, kwargs

### Write your code below this line ###

about_me = keyword_argument_example(21, **{'name': 'musbi', 'surname': 'jawo'}

### Write your code above this line ###

print(about_me)
