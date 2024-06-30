1. Introduction
This Python script simulates an ordering system for a frozen yogurt and ice cream shop. Customers can place orders for frozen yogurt or ice cream, choose various sizes, containers, and toppings, and add cookies to their order. The system calculates the order total and applies a weekend discount if applicable. At the end of the day, a sales report is generated.

2. Features
Menu Options: Offers frozen yogurt and ice cream with various sizes, containers, toppings, and cookies.
Order Management: Takes customer orders, calculates totals, and applies discounts.
Order History: Tracks individual customer order totals.
Sales Report: Generates a report summarizing sales and averages.
3. System Requirements
Python 3.6 or later
A terminal or command-line interface
4. Installation
Clone the Repository: Clone this repository to your local machine using:

bash
Copy code
git clone <repository_url>
Navigate to the Directory:

bash
Copy code
cd <repository_directory>
Run the Script:

bash
Copy code
python yogurt_shop.py
Replace <repository_url> and <repository_directory> with the actual URL and directory name.

5. Usage
Starting the System: Run the script using Python. The system will prompt you to enter your name and order details.

Ordering Process:

Enter your name.
Choose between Frozen Yogurt (Y) or Ice Cream (I).
Select the size (S: Small, M: Medium, L: Large).
Choose the container (V: Cone, U: Cup).
Optionally add toppings (Y: Yes, N: No).
Optionally add cookies (Y: Yes, N: No).
Specify the day of the week (1: Monday, ..., 7: Sunday) for potential weekend discounts.
Finalizing Order:

The total price of the order will be displayed.
Choose to continue or quit the system.
Generating Reports: A sales report is automatically generated when quitting the system.

6. Code Overview
Menu Definition
The menu is defined as a dictionary with prices for various items:

python
Copy code
menu = {
    'frozen_yogurt': {
        'small': {'cone': 3.09, 'cup': 3.19},
        'medium': {'cone': 3.89, 'cup': 3.99},
        'large': {'cone': 4.69, 'cup': 4.79}
    },
    'ice_cream': {
        'small': {'cone': 3.49, 'cup': 3.59},
        'medium': {'cone': 3.49, 'cup': 3.59},
        'large': {'cone': 5.49, 'cup': 5.59}
    },
    'toppings': {
        'gummies': 1.59,
        'nuts': 1.89
    },
    'cookies': {
        'regular': {'raisin': 1.49, 'chocolate': 1.59},
        'large': {'raisin': 2.49, 'chocolate': 2.59}
    }
}
Order Calculation
Calculates the total price for a given order:

python
Copy code
def calculate_order_total(order):
    total = 0
    for item in order:
        total += menu[item['type']][item['size']][item['container']]
        if item.get('topping'):
            total += menu['toppings'][item['topping']]
        if item.get('cookie'):
            total += menu['cookies'][item['cookie_size']][item['cookie_type']]
    return total
Order Taking
Handles user input to build and calculate an order:

python
Copy code
def take_order():
    name = input("Enter your name: ")
    # ... (additional input handling)
    total = calculate_order_total(order)
    # Apply weekend discount
    day_of_week = input("What day of the week is this? (1:Monday, ..., 7:Sunday) ")
    if day_of_week in ['6', '7']:
        total *= 0.9
    # ... (order history and reporting)
Sales Reporting
Generates a summary report at the end of the session:

python
Copy code
def generate_report():
    print("Customer Name\tOrder Total")
    for idx, data in order_history.items():
        print("{:}\t\t{:.2f}".format(idx, order_history[idx]))
    # ... (sales totals and averages)
Main Loop
Runs the main order-taking loop until the user chooses to quit:

python
Copy code
while True:
    take_order()
    if input("Enter C to continue or Q to quit: ").lower() == 'q':
        break
generate_report()
7. Examples
Example Order
mathematica
Copy code
Enter your name: John
Do you want Frozen Yogurt or Ice cream? (Y: Frozen Yogurt, I: Ice cream) Y
What size? (S: Small, M: Medium, L: Large) M
What kind of container? (V: Cone, U: Cup) U
Do you like to add a topping? (Y: Yes, N: No) Y
What topping do you like? (G: Gummies, N: Nuts) G
Do you like to have cookies? (Y: Yes, N: No) N
What day of the week is this? (1: Monday, ..., 7: Sunday) 6
Your order total is $5.57
Example Report
bash
Copy code
Customer Name	Order Total
John		$5.57
Item		#Order	Order Total	Average Per Order
Yogurt		1	$5.57		$5.57
Ice Cream	0	$0.00		$0.00
Total		1	$5.57		$5.57
8. Author
This script was created by [Your Name]. For any questions or support, please contact 
