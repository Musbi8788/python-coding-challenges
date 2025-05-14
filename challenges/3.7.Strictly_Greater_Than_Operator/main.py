def strictly_greater_than(value):
    if value > 100:  # Change this line
        return "Greater than 100"
    elif value > 10:  # Change this line
        return "Greater than 10"
    else:
        return "10 or less"

# Change the value 1 below to experiment with different values
print(strictly_greater_than(89))
