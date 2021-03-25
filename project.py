print("Hello world")

def show ():
    x = input('Input number1 : ')
    y = input('Input number2 : ')
    Ans = add(int(x),int(y))
    print(x,'+',y,'=' ,Ans)

def name():
    name = input('Enter your name :')
    print('Your name: '+name)

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def Calculate():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
    # Take input from the user
        choice = input("Enter choice : ")

    # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")

import random, string ,secrets

def Generator():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20)) 
    print(password)
    
def Guessnum():
    number = random.randint(1,10)
    tries = 0

    print("Guess your number 3 times")

    guess = input("Guess number : ")
    guess = int(guess)
    tries+=1

    if guess > number:
        print("Too High")
    if guess < number:
        print("Too Low")

    while guess!=number and tries<3:
        guess = input("Guess number again: ")
        guess = int(guess)
        tries+=1

        if guess > number:
            print("Too High")
        if guess < number:
            print("Too Low")

    if guess == number:
        print("Correct!")
        print(f"You Tries : {tries}")
    else :
        print("Wrong!")
        print("No more chance")

def Grade():

   grade = int(input("Enter score :"))
   name = input("Enter Name :") 

   print("Name: ",name)
   if((grade>=80) and (grade<=100)):
       print("The score is: ",grade,", Grade : A , GPA : 4.00")
   elif((grade>=75) and (grade<80)):
       print("The score is: ",grade,", Grade : B+ , GPA : 3.50")
   elif((grade>=70) and (grade<75)):
       print("The score is: ",grade,", Grade : B , GPA : 3.00")
   elif((grade>=65) and (grade<70)):
        print("The score is: ",grade,", Grade : C , GPA : 2.50")
   elif((grade>=60) and (grade<65)):
        print("The score is: ",grade,", Grade : C+ , GPA : 2.00")
   elif((grade>=55) and (grade<60)):
        print("The score is: ",grade,", Grade : D+ , GPA : 1.5")
   elif((grade>=0) and (grade<55)):
        print("The score is: ",grade,", Grade : F , GPA : 0.00")
   else:
        print("The Score is: ",grade,"No Grade")
    
import requests

# def map():
#     # api-endpoint
#     URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
#     # location given here
#     location = "delhi technological university"
  
#     # defining a params dict for the parameters to be sent to the API
#     PARAMS = {'address':location}
  
#     # sending get request and saving the response as response object
#     r = requests.get(url = URL, params = PARAMS)
  
#     # extracting data in json format
#     data = r.json()
   
  
#     # extracting latitude, longitude and formatted address 
#     # of the first matching location
#     latitude = data['results'][0]['geometry']['location']['lat']
#     longitude = data['results'][0]['geometry']['location']['lng']
#     formatted_address = data['results'][0]['formatted_address']
  
#     # printing the output
#     print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#         %(latitude, longitude,formatted_address))


# class Currency_convertor:
#     # empty dict to store the conversion rates
#     rates = {} 
#     def __init__(self, url):
#         data = requests.get(url).json()
  
#         # Extracting only the rates from the json data
#         self.rates = data["rates"] 
  
#     # function to do a simple cross multiplication between 
#     # the amount and the conversion rates
#     def convert(self, from_currency, to_currency, amount):
#         initial_amount = amount
#         if from_currency != 'EUR' :
#             amount = amount / self.rates[from_currency]
  
#         # limiting the precision to 2 decimal places
#         amount = round(amount * self.rates[to_currency], 2)
#         print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
  
# # Driver code
# if __name__ == "__main__":
  
#     # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
#     url = str.__add__('http://data.fixer.io/api/latest?access_key=be89efa318cf9c4f31921580d6f52d6a')  
#     c = Currency_convertor(url)
#     from_country = input("From Country: ")
#     to_country = input("TO Country: ")
#     amount = int(input("Amount: "))
  
#     c.convert(from_country, to_country, amount)
# #  2038b86a490170cfdd4f