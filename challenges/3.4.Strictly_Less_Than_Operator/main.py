def strictly_less_than(value):
    if value < 10:  
        return "Less than 10"
    elif value < 100 : 
        return "Less than 100"
    else:
        return "100 or more"

# Change the value 1 below to experiment with different values
print(strictly_less_than(4))
