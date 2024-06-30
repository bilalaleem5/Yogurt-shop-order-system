# Define the menu
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

# Initialize the order history
order_total = {
    'icecream' : 0,
    'ice-total' : 0,
    'yogurt' : 0,
    'yog-total' : 0,
}

order_history = {}

# Function to calculate the order total
def calculate_order_total(order):
    total = 0
    for item in order:
        total += menu[item['type']][item['size']][item['container']]
        if item.get('topping'): # Use get method to avoid KeyError
            total += menu['toppings'][item['topping']]
        if item.get('cookie'): # Use get method to avoid KeyError
            total += menu['cookies'][item['cookie_size']][item['cookie_type']]
    return total

# Function to take an order
def take_order():
    # Get the customer's name
    name = input("Enter your name: ")
    
    # Check if the customer has ordered before
    if name in order_history:
        print("Welcome back!")
    
    # Initialize the order
    order = []
    
    # Get the order details
    product_type = input("Do you want Frozen Yogurt or Ice cream? (Y: Frozen Yogurt, I: Ice cream) ")
    product_type = "frozen_yogurt" if product_type.lower() == "y" else "ice_cream"
    
    size = input("What size? (S: Small, M: Medium, L: Large) ")
    size = "small" if size.lower() == "s" else "medium" if size.lower() == "m" else "large"
    
    container = input("What kind of container? (V: Cone, U: Cup) ")
    container = "cone" if container.lower() == "v" else "cup"
    
    topping = None
    if input("Do you like to add a topping? (Y: Yes, N: No) ").lower() == "y":
        topping = input("What topping do you like? (G: Gummies, N: Nuts) ")
        topping = "gummies" if topping.lower() == "g" else "nuts"
    
    cookie_type = None
    cookie_size = None
    if input("Do you like to have cookies? (Y: Yes, N: No) ").lower() == "y":
        cookie_type = input("What kind of cookies? (R: Raisin, C: Chocolate) ")
        cookie_type = "raisin" if cookie_type.lower() == "r" else "chocolate"
        
        cookie_size = input("And the size? (R: Regular, L: Large) ")
        cookie_size = "regular" if cookie_size.lower() == "r" else "large"
    
    # Add the item to the order
    order.append({
        'type': product_type,
        'size': size,
        'container': container,
        'topping': topping,
        'cookie_type': cookie_type,
        'cookie_size': cookie_size,
    })
    
    # Calculate the order total
    total = calculate_order_total(order)
    
    # Apply the weekend discount if applicable
    day_of_week = input("What day of the week is this? (1:Monday, ..., 7:Sunday) ")
    if day_of_week in ['6', '7']:
        total *= 0.9

    if product_type == 'frozen_yogurt':
        order_total['yogurt']+=total
        order_total['yog-total']+=1
    else:
        order_total['icecream']+=total
        order_total['ice-total']+=1
    
    # Update the order history
    if name in order_history:
        order_history[name] += total
    else:
        order_history[name] = total
    
    print(f"Your order total is ${total:.2f}")
  
# Function to generate a sales report
def generate_report():

    print("Customer Name\tOrder Total")
    for idx, data in order_history.items() :
        print("{:}\t\t{:.2f}".format(idx, order_history[idx]))

    yogurt_avg = order_total['yogurt']/order_total['yog-total'] if order_total['yog-total'] !=0 else 0
    ice_avg = order_total['icecream']/order_total['ice-total'] if order_total['ice-total'] !=0 else 0
    
    print(f"Item\t\t#Order\tOrder Total\tAverage Per Order")
    print(f"Yogurt\t\t${order_total['yog-total']:}\t${order_total['yogurt']:.2f}\t\t${yogurt_avg:.2f}")
    print(f"Ice Cream\t${order_total['ice-total']:}\t${order_total['icecream']:.2f}\t\t${ice_avg:.2f}")
    print(f"Total\t\t${order_total['yog-total']+order_total['ice-total']:}\t${order_total['yogurt']+order_total['icecream']:.2f}\t\t${yogurt_avg+ice_avg:.2f}")
# Main program loop
while True:
    take_order()
    
    # Check if the user wants to quit
    if input("Enter C to continue or Q to quit: ").lower() == 'q':
        break

# Generate a sales report at the end of the day
generate_report()
