# Dictionaries or objects in python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary)
print(programming_dictionary["Bug"])

# To add new new key in the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A mosquito in your laptop"
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Challenge 1 Grading system
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# grade1 = "outstanding"
# grade2 = "Exceeds Expectation"
# grade3 = "Acceptable"
# grade4 = "Fail"

# student_grades = {}

# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = grade1
#     elif score >80:
#         student_grades[key] = grade2    
#     elif score > 70:    
#         student_grades[key] = grade3
#     else:
#         student_grades[key] = grade4    

# print(student_grades) 

# Nesting lists and dictionaries
travel_log = [
    {
    "country":"France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits":12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg"], 
    "total_visits":10
    },
]   

# Challenge 2 Dictionary in list
# travel_log = [
#     {
#     "country":"France",
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits":12
#     },
#     {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg"], 
#     "total_visits":10
#     },
# ]   
# def add_new_country(country,visits,cities):
#     new_country = {}   
#     new_country["country"] = country
#     new_country["cities_visited"] = cities
#     new_country["total_visits"] = visits
#     travel_log.append(new_country)
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Challenge 3 Secret Auction
import os
print("Welcome to secret auction program")
bidders_data = {}
bidding_finished = False

def result(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
       bid_amount =  bids[bidder]
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}.")       
    
while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders_data[name] = bid
    any_bid = input("Is there any one else who want to bid.Type 'yes' or 'no'. ") 
    if any_bid == "no":
        bidding_finished = True
        result(bidders_data)
    elif any_bid == "yes":
        os.system('cls')
    else:
        print("Incorrect data")    
        

        
    
        

    