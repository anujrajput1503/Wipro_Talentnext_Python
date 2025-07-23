
# Exception handling 
'''Project: 1

You had saved the items and their price details in a text file, which you
purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to
handle the possible exceptions.
Note:
. Data is stored in a text file Purchase-1.txt.
. Each line contains one item's details.
. Item name and price is separated by a space.
. You have to enter the file name during run time.

Sample input 1:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5

Sample output 1:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

Sample input 2:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup Free
(blank line)
Discount 80

Sample output 2:
Enter the file name: Purchase-1
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405'''

purchased_items = 0
free_items = 0
total_amount = 0
discount = 0

try:
    file_input = input("Enter the File name ")
    file_name = f'{file_input}.txt'
    
    with open(file_name, 'r') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line :
                continue
            
            parts = clean_line.split()
            
            if len(parts) < 2:
                continue
            item_part = parts[0]
            priceorstatus =parts[1]
            
            
            if item_part.lower() == 'discount':
                
                try :
                    discount = int(priceorstatus)
                except ValueError :
                    print(f"Warning: Invalid discount value '{priceorstatus}'. Setting discount to 0.")
                    discount = 0
                
            elif priceorstatus.lower() == 'free':
                free_items += 1
                
            else:
                try:
                    price = int(priceorstatus)
                    total_amount += price
                    purchased_items += 1
                except ValueError:
                    # This handles cases where the price is not a valid number
                    print(f"Warning: Invalid price for '{item_part}'. Skipping item.")


    final_amount = total_amount - discount
    
    print(f"No of items purchased: {purchased_items}")
    print(f"No of free items: {free_items}")
    print(f"Amount to pay: {total_amount}")
    print(f"Discount given: {discount}")
    print(f"Final amount paid: {final_amount}")

# Handle the case where the file does not exist
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please check the file name and location.")

# Handle any other unexpected errors during execution
except Exception as e:
    print(f"An unexpected error occurred: {e}")

