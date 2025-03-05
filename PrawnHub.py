import datetime
import random #For reference number

# Value Added Tax (12%)
VAT_RATE = 0.12

# Discounts
def calculate_discount(total, customer_type):
    discount_rates = {'Student': 0.20, 'Pwd': 0.20, 'Senior': 0.20, 'Teacher': 0.20}
    return total * discount_rates.get(customer_type, 0)

# Calculation of VAT
def calculate_vat(total):
    return total * VAT_RATE

# Prawn Art 🦐
def print_welcome_with_prawn():
    prawn_art = """
                  ████  ██████████████    ████
    ██          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓██████
      ██      ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓████
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓██
      ██  ████▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓████
    ▓▓        ▓▓████████▓▓              ████▓▓▓▓▓▓▓▓████▓▓██
                                        ████▓▓▓▓▓▓▓▓████▓▓██
                        ████████         ████▓▓▓▓████░░██
                      ██▓▓▓▓▓▓▓▓██    ████▓▓████░░░░░░██
                      ██▓▓▓▓▓▓░░░░████░░░░░░░░░░██████
                      ██▓▓░░░░░░██
                        ██████▓▓
    """
    print(prawn_art)
    print("Welcome to Prawn Hub!")

# Receipts
def generate_receipt(items, customer_type, total_amount, cash):
    discount_amount = calculate_discount(total_amount, customer_type)
    vat_amount = calculate_vat(total_amount)

    current_datetime = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")  # Date and Time
    reference_number = random.randint(1000, 9999)  # Random Reference Number
    location = "Prawn Hub - CvSU Imus"  # Location
    server = "Jericho Pogi"  # Server

    print("     Receipt from Prawn Hub 🦐")  # I love Prawn Hub 👉🏻👈🏻
    print("=============================================")
    print(f"Location:  {location}")
    print(f"Reference Number: \t{reference_number}")
    print(f"Server: \t{server}")
    print(f"Date & Time: {current_datetime}")
    print("Item\t\t\tQuantity\tPrice")
    print("---------------------------------------------")

    for item, (quantity, price) in items.items():
        print(f"{item}\t\t{quantity}x\t\t{price:.2f}")

    print("---------------------------------------------")
    print(f"Total Amount:\t{total_amount:.2f}")

    if discount_amount > 0:
        print(f"Discount ({customer_type})\t-{discount_amount:.2f}")

    print(f"VAT ({VAT_RATE * 100}%):\t\t{vat_amount:.2f}")
    total_with_vat = total_amount - discount_amount + vat_amount

    print("---------------------------------------------")
    print(f"Total with VAT:\t{total_with_vat:.2f}")

    change = cash - total_with_vat
    print(f"How much is your cash? {cash:.2f}")
    print(f"Change: {change:.2f}")
    print("=============================================")

def main():
    while True:
        print_welcome_with_prawn()
        prawn_store = {
            "Butter Prawn": 350.00,
            "Spicy Prawn": 290.00,
            "Fried Prawn": 320.00,
            "Prawn Pizza": 680.00,
            "Prawn Takoyaki": 250.00,
            "Prawn Sisig": 650.00,
            "Prawn Salad": 300.00,
            "Iced Tea (L)": 50.00,
            "Lemonade (L)": 60.00,
            "Prawn Smoothie (L)": 120.00
        }
        customer_type = input("Are you a Student, PWD, Senior, Teacher, or Regular customer? ").capitalize()
        if customer_type not in ['Student', 'Pwd', 'Senior', 'Teacher', 'Regular']:
            print("Invalid customer type. Exiting.")
            return
        selected_items = {}

        print("""
How may I take your order?
Menu:""")

        for idx, (item, price) in enumerate(prawn_store.items(), start=1):
            print(f"{idx}. {item} - {price:.2f}")

        menu_printed = True  # Variable to track if the menu has been printed

        while True:
            if menu_printed:
                print("""
Enter the item number you want to add to your cart (0 to finish, -1 to exclude):""")
            # Prompt to the user
            choice = input()

            if choice == '0':
                break
            elif choice == '-1':
                exclude_item(prawn_store, selected_items)
            else:
                add_item(prawn_store, selected_items, choice)
                menu_printed = False  # Set to False after the first item is added

        total_amount = sum(item[0] * item[1] for item in selected_items.values())
        generate_receipt(selected_items, customer_type, total_amount, cash=0)  # Note: Cash is set to 0 for now

        # Get cash input after ordering
        cash = float(input("How much cash do you have? "))

        if total_amount > cash:
            print("Insufficient funds. Please choose fewer items or increase your budget.")
        else:
            generate_receipt(selected_items, customer_type, total_amount, cash)

        order_again = input("Do you want to order again? (yes/no): ").lower()
        if order_again == 'no':
            main()



# Exclude Item
def exclude_item(prawn_store, selected_items):
    exclude_item = input("Enter the item number you want to exclude: ")
    try:
        exclude_item = int(exclude_item)
        if 1 <= exclude_item <= len(prawn_store):
            excluded_item_name = list(prawn_store.keys())[exclude_item - 1]
            if excluded_item_name in selected_items:
                selected_items[excluded_item_name][0] -= 1  # decrease quantity
                if selected_items[excluded_item_name][0] == 0:
                    selected_items.pop(excluded_item_name, None)
                prawn_store[excluded_item_name]
                print(f"{excluded_item_name} quantity decreased.")
            else:
                print(f"{excluded_item_name} is not in your cart.")
        else:
            print("Invalid item number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Add Item
def add_item(prawn_store, selected_items, choice):
    try:
        choice = int(choice)
        if 1 <= choice <= len(prawn_store):
            item_name = list(prawn_store.keys())[choice - 1]
            if item_name in selected_items:
                selected_items[item_name][0] += 1  # increase quantity
            else:
                selected_items[item_name] = [1, prawn_store[item_name]]  # set quantity to 1
        else:
            print("Invalid item number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main = printing the inputs
main()