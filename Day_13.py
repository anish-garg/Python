# Fixing error
year = int(input("Which year you were born in? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")    

# If caught in very hard error then try to use the debug at- 
# http://www.pythontutor.com/visualize.html#mode=edit