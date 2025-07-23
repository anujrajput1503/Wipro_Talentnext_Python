# Python fundamentals
'''Project: 1
Create a python program that asks the user how far they want to travel. If they want to travel less than
three miles tell them to ride Bicycle. If they want to travel more than three miles, but less than three
hundred miles, tell them to ride Motor-Cycle. If they want to travel three hundred miles or more tell them to
driver Super-Car.

Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination

'''

mil = int(input("How far would you like to travel in miles?"))

if(mil < 3) :
    print("I suggest Bicycle to your destination")
elif(mil<100):
    print("I suggest Moter cycle to your destination")
else : 
    print("I suggest Super-Car to your destination")    


# *******************************************************************************************************************

'''Project: 2
Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
You decide to host your application on servers running in the cloud. You pick a hosting provider
that charges $0.51 per hour. You will launch your service using one server and want to know
how much it will cost to operate per day,per week,per month.

Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?

'''
ph = 0.51
pd = 0.51*24
pw = 0.51*24*7
pm = 0.51*24*30
statement = '''How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?'''

print(f'How much does it cost to operate one server per day? {pd}\nHow much does it cost to operate one server per week? {pw}\nHow much does it cost to operate one server per month? {pm}')

print(f'How many days can I operate one server with $918? {918/pd}')
