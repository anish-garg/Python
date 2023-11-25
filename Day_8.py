# def greet():
#     print("Hello")
#     print("Hello World")
#     print("Hello Anish")
    
# greet() 

# Function with one param
# def greet_with_name(name):
#     print(f"Hello {name}")  
#     print(f"How do you do {name}?") 

# greet_with_name("Anish")  

# Function with two param
# def greet_with(name,place):
#     print(f"Hello {name} from {place}")  

# # greet_with("Anish","Delhi")
# greet_with(name="Anish",place="Delhi")

# Challenge 1 Area Calc
# import math
# test_h = int(input("Height of the wall: "))
# test_w = int(input("Width of the wall: "))

# coverage = 5

# def cans_required(h,w,coverage):
#     number_of_cans = math.ceil(h * w / coverage)
#     print(f"The cans required for the paints are {number_of_cans}")

# cans_required(test_h,test_w,coverage)

# Challenge 2 Prime number checker
# number = int(input("Check this number: "))
# def prime_checker(n):
#     is_prime = True
#     for i in range(2,n):
#         if n % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print("It is a prime number")
#     else:
#         print("It is not a prime number")        
            
# prime_checker(number)   

# Challenge 3 Caesar Cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)  
            new_position = position + shift_amount
            new_letter = alphabet[new_position]  
            cipher_text += new_letter
        else:
            cipher_text += letter    
    print(f"The encoded text is {cipher_text}")    
    
def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += letter       
    print(f"The decoded text is {plain_text}")
    
if direction == "encode":
    text = (input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 32:
        shift = shift % 26
    encrypt(text,shift)
elif direction == "decode":
    text = (input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 32:
        shift = shift % 26
    decrypt(text,shift)     
else:
    print("Wrong input")    