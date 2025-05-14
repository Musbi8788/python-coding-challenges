def less_or_equal(value):
    if value <= 25:  # Change this line
        return "25 or less"
    elif value <= 75:  # Change this line
        return "75 or less"
    else:
        return "More than 75"

# Change the value 1 below to experiment with different values
print(less_or_equal(35))
