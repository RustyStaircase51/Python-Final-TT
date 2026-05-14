"""This file contains the core functions for adding, editing, sorting, and processing inventory and purchase orders."""


from models import Product
from models import Vendor
from models import PurchaseOrder
import file_manager

all_products = []
all_vendors = []
all_purchase_orders = []


# Product Management
# -------------------------------------------------------------------------------------------------------------------------------------

def add_product():  # creates a product object and saves the object to the list "all_products"
    user_product_id = input("\nEnter Product ID: ").strip()
    user_product_name = input("Enter Product Name: ").strip()
    user_category = input("Enter Category: ").strip()

    # Validate integer inputs
    try:
        user_in_stock = int(input("Enter Current Stock: "))
    except ValueError:
        print("Value Error: Current Stock must be an integer. New Product was discarded.")
        return

    try:
        user_reorder_level = int(input("Enter Reorder Level: "))
        if user_reorder_level < 0:
            print("Value Error: Reorder Level must be zero or greater. New Product was discarded.")
            return
    except ValueError:
        print("Value Error: Reorder Level must be an integer. New Product was discarded.")
        return

    try:
        user_reorder_quantity = int(input("Enter Reorder Quantity: "))
        if user_reorder_quantity < 0:
            print("Value Error: Reorder Quantity must be zero or greater. New Product was discarded.")
            return
    except ValueError:
        print("Value Error: Reorder Quantity must be an integer. New Product was discarded.")
        return

    try:
        user_unit_price = float(input("Enter Unit Price: "))
        if user_unit_price <= 0.00:
            print("Value Error: Unit Price must be greater than zero. New Product was discarded.")
            return
    except ValueError:
        print("Value Error: Unit Price must be a number. New Product was discarded.")
        return

    user_vendor_id = input("Enter Vendor ID: ").strip()
    user_active_status = input("Enter the active status: ").strip()

    new_product = Product(
        user_product_id,
        user_product_name,
        user_category,
        user_in_stock,
        user_reorder_level,
        user_reorder_quantity,
        user_unit_price,
        user_vendor_id,
        user_active_status
    )
    all_products.append(new_product)
    print("New Product Added:", new_product)

def view_all_products():  # prints all products using the __repr__ method from "models.py"
    if all_products:
        for product in all_products:
            print(product)
    else:
        print("\nError: No Products to Display.")  # Input Validation


def search_products():
    user_product_search = input(
        "\nSelect Search Options\n"
        "1. Search by Product ID\n"
        "2. Search by Category\n"
        "3. Search by Product Name\n"
        "4. Search by PO date\n"
    ).strip()

    if user_product_search == "1":  # Search by Product ID
        product_id_search = input("Enter the product ID: ").strip()
        if all_products:
            found = False
            for i in all_products:
                if i.product_id.lower() == product_id_search.lower():
                    print(i)
                    found = True
            if not found:
                print(f"No product found for the ID: {product_id_search}")  # input validation
        else:
            print("No products to display.")

    elif user_product_search == "2":  # Search by Category
        category_search = input("Enter the category: ").strip()
        if all_products:
            found = False
            for c in all_products:
                if c.category.lower() == category_search.lower():
                    print(c)
                    found = True
            if not found:
                print(f"No product found for the category: {category_search}")
        else:
            print("No products to display.")

    elif user_product_search == "3":  # Search by Product Name
        product_name_search = input("Enter the product name: ").strip()
        if all_products:
            found = False
            for n in all_products:
                if n.product_name.lower() == product_name_search.lower():
                    print(n)
                    found = True
            if not found:
                print(f"No product found for the product name: {product_name_search}")
        else:
            print("No products to display.")

    elif user_product_search == "4":  # Search by PO Date
        po_search = input("Enter the PO date: ").strip()
        if all_purchase_orders:
            found = False
            for p in all_purchase_orders:
                if str(p.date_created).lower() == po_search.lower():
                    print(p)
                    found = True
            if not found:
                print(f"No product found for the PO date: {po_search}")
        else:
            print("No purchase orders to display.")

    else:
        print("Invalid menu option. Please try again.")



def edit_product(): 
    product_edit_search = input("Enter the Product's current ID: ").strip()

    if all_products:
        found = False
        for u in all_products:  # reused from "def search_products()"
            if u.product_id.lower() == product_edit_search.lower():
                print(u)
                product_index = all_products.index(u)  # gets the position of the product
                found = True
                break

        if not found:
            print(f"No product found for the ID: {product_edit_search}")
            return
    else:
        print("Error: No products to display")
        return

    # Edit menu
    product_edit_options = input(
        "Select Edit Options\n"
        "1. Edit Product ID\n"
        "2. Edit Product Name\n"
        "3. Edit Product Category\n"
        "4. Edit In-Stock Inventory\n"
        "5. Edit Reorder Level\n"
        "6. Edit Reorder Quantity\n"
        "7. Edit Unit Price\n"
        "8. Edit Vendor ID\n"
        "9. Edit Active Status\n"
    ).strip()

    # Edit options
    if product_edit_options == "1":  # changes product ID
        print(f"The current product ID is: {all_products[product_index].product_id}")
        new_product_id = input("Enter the new product ID: ").strip()
        all_products[product_index].product_id = new_product_id

    elif product_edit_options == "2":  # change product name
        print(f"The current product name is: {all_products[product_index].product_name}")
        new_product_name = input("Enter the new product name: ").strip()
        all_products[product_index].product_name = new_product_name

    elif product_edit_options == "3":  # change product category
        print(f"The current product category is: {all_products[product_index].category}")
        new_product_category = input("Enter the new product category: ").strip()
        all_products[product_index].category = new_product_category

    elif product_edit_options == "4":  # change in-stock inventory
        print(f"The current product in-stock inventory is: {all_products[product_index].in_stock}")
        try:
            new_product_in_stock = int(input("Enter the new product in-stock inventory: "))
            all_products[product_index].in_stock = new_product_in_stock
        except ValueError:
            print("Value Error: In-stock inventory must be an integer. Update discarded.")
            return

    elif product_edit_options == "5":  # change reorder level
        print(f"The current product reorder level is: {all_products[product_index].reorder_level}")
        try:
            new_product_reorder_level = int(input("Enter the new product reorder level: "))
            if new_product_reorder_level < 0:
                print("Value Error: Reorder Level must be zero or greater. Update discarded.")
                return
            all_products[product_index].reorder_level = new_product_reorder_level
        except ValueError:
            print("Value Error: Reorder Level must be an integer. Update discarded.")
            return

    elif product_edit_options == "6":  # change reorder quantity
        print(f"The current product reorder quantity is: {all_products[product_index].reorder_quantity}")
        try:
            new_product_reorder_quantity = int(input("Enter the new product reorder quantity: "))
            if new_product_reorder_quantity < 0:
                print("Value Error: Reorder Quantity must be zero or greater. Update discarded.")
                return
            all_products[product_index].reorder_quantity = new_product_reorder_quantity
        except ValueError:
            print("Value Error: Reorder Quantity must be an integer. Update discarded.")
            return

    elif product_edit_options == "7":  # change unit price
        print(f"The current product unit price is: {all_products[product_index].unit_price}")
        try:
            new_product_unit_price = float(input("Enter the new product unit price: "))
            if new_product_unit_price <= 0:
                print("Value Error: Unit Price must be greater than zero. Update discarded.")
                return
            all_products[product_index].unit_price = new_product_unit_price
        except ValueError:
            print("Value Error: Unit Price must be a number. Update discarded.")
            return

    elif product_edit_options == "8":  # change vendor ID
        print(f"The current product vendor ID is: {all_products[product_index].vendor_id}")
        new_product_vendor_id = input("Enter the new product vendor ID: ").strip()
        all_products[product_index].vendor_id = new_product_vendor_id

    elif product_edit_options == "9":  # change active status
        print(f"The current product active status is: {all_products[product_index].active_status}")
        new_product_active_status = input("Enter the new product active status: ").strip()
        all_products[product_index].active_status = new_product_active_status

    else:
        print("Invalid menu option. Please try again.")
        return

    print("Updated product information:", all_products[product_index])



def low_stock_display():  # displays product if product.reorder_level is greater than the product.in_stock
    found = False
    for l in all_products:
        if l.reorder_level >= l.in_stock:
            print(l)
            found = True
    if not found:
        print("No low stock items found.")



#Vendor Management
#--------------------------------------------------------------------------------------------------------------------------------------

def add_vendor():
    user_vendor_id_2 = input("Enter Vendor ID: ").strip()
    
    # Initialize duplicate flag
    id_duplicate_found = False
    
    # Check for duplicate IDs
    for i in all_vendors:
        if i.vendor_id.lower() == user_vendor_id_2.lower():
            id_duplicate_found = True
            break  # stop searching if duplicate is found
    
    if id_duplicate_found:
        print(f"{user_vendor_id_2} already exists.")
        print("New Vendor discarded")
    else:
        user_vendor_name = input("Enter Vendor Name: ").strip()
        user_contact_name = input("Enter Vendor Contact Name: ").strip()
        user_phone = input("Enter Vendor's Phone Number: ").strip()
        user_email = input("Enter Vendor's Email Address: ").strip()
        user_address = input("Enter Vendor's Postal Address: ").strip()
    
        new_vendor = Vendor(user_vendor_id_2, user_vendor_name, user_contact_name, user_phone, user_email, user_address)
        all_vendors.append(new_vendor)
        print(f"New Vendor Added: {new_vendor}")



def view_all_vendors():  # prints all vendors using the __repr__ method from "models.py"
    if all_vendors:
        for vendor in all_vendors:
            print(vendor)
    else:
        print("Error: no vendors to display.")


def search_vendors():
    if not all_vendors:
        print("Error: no vendors to display.")
        return

    user_vendor_search = input(
        "Select Search Options\n"
        "1. Search by Vendor ID\n"
        "2. Search by Vendor Name\n"
        "3. Search by Contact Name\n"
        "4. Search by Phone Number\n"
    ).strip()

    if user_vendor_search == "1":
        vendor_id_search = input("Enter the Vendor ID: ").strip().lower()
        found = False
        for i in all_vendors:
            if i.vendor_id.lower() == vendor_id_search:
                print(i)
                found = True
        if not found:
            print(f"No vendor found for the ID: {vendor_id_search}")

    elif user_vendor_search == "2":
        vendor_name_search = input("Enter the Vendor Name: ").strip().lower()
        found = False
        for n in all_vendors:
            if n.vendor_name.lower() == vendor_name_search:
                print(n)
                found = True
        if not found:
            print(f"No vendor found for the name: {vendor_name_search}")

    elif user_vendor_search == "3":
        contact_name_search = input("Enter the Vendor Contact Name: ").strip().lower()
        found = False
        for c in all_vendors:
            if c.contact_name.lower() == contact_name_search:
                print(c)
                found = True
        if not found:
            print(f"No vendor found for the contact name: {contact_name_search}")

    elif user_vendor_search == "4":
        phone_search = input("Enter the Vendor Phone Number: ").strip()
        found = False
        for p in all_vendors:
            if p.phone == phone_search:
                print(p)
                found = True
        if not found:
            print(f"No vendor found for the phone number: {phone_search}")

    else:
        print("Invalid menu option. Please try again.")


def edit_vendor():
    if not all_vendors:
        print("Error: No vendors to display.")
        return

    vendor_edit_search = input("Enter the Vendor's current ID: ").strip().lower()
    found = False
    for i in all_vendors:
        if i.vendor_id.lower() == vendor_edit_search:
            print(i)
            vendor_index = all_vendors.index(i)
            found = True
            break

    if not found:
        print(f"No vendor found for the ID: {vendor_edit_search}")
        return

    vendor_edit_options = input(
        "Select Edit Option\n"
        "1. Edit Vendor ID\n"
        "2. Edit Vendor Name\n"
        "3. Edit Contact Name\n"
        "4. Edit Phone Number\n"
        "5. Edit Email Address\n"
        "6. Edit Postal Address\n"
    ).strip()

    if vendor_edit_options == "1":
        print(f"The current vendor ID is: {all_vendors[vendor_index].vendor_id}")
        new_vendor_id = input("Enter the new vendor ID: ").strip()
        all_vendors[vendor_index].vendor_id = new_vendor_id

    elif vendor_edit_options == "2":
        print(f"The current vendor name is: {all_vendors[vendor_index].vendor_name}")
        new_vendor_name = input("Enter the new vendor name: ").strip()
        all_vendors[vendor_index].vendor_name = new_vendor_name

    elif vendor_edit_options == "3":
        print(f"The current vendor contact name is: {all_vendors[vendor_index].contact_name}")
        new_vendor_contact_name = input("Enter the new vendor contact name: ").strip()
        all_vendors[vendor_index].contact_name = new_vendor_contact_name

    elif vendor_edit_options == "4":
        print(f"The current vendor phone number is: {all_vendors[vendor_index].phone}")
        new_vendor_phone = input("Enter the new vendor phone number: ").strip()
        all_vendors[vendor_index].phone = new_vendor_phone

    elif vendor_edit_options == "5":
        print(f"The current vendor email address is: {all_vendors[vendor_index].email}")
        new_vendor_email = input("Enter the new vendor email address: ").strip()
        all_vendors[vendor_index].email = new_vendor_email

    elif vendor_edit_options == "6":
        print(f"The current vendor postal address is: {all_vendors[vendor_index].address}")
        new_vendor_address = input("Enter the new vendor postal address: ").strip()
        all_vendors[vendor_index].address = new_vendor_address

    else:
        print("Invalid menu option. Please try again.")
        return

    print("Updated vendor information:", all_vendors[vendor_index])



#Purchase Order System
#-----------------------------------------------------------------------------------------------------------------------------------


unique_item_saver = []
user_item_totals = 1
user_total_cost = 0


def add_purchase_order():
    user_po_number = input("Enter a Purchase Order Number: ").strip()
    user_vendor_id = input("Enter a Vendor ID: ").strip()
    user_date_created = input("Enter the Purchase Order Date (YYYY-MM-DD): ").strip()

    # Validate vendor exists
    if not any(v.vendor_id.lower() == user_vendor_id.lower() for v in all_vendors):
        print(f"Error: Vendor ID '{user_vendor_id}' not found.")
        return

    # Number of unique items
    try:
        user_item_counter = int(input("Enter the number of UNIQUE items ordered: ").strip())
        if user_item_counter <= 0:
            print("Error: Number of items must be greater than zero.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for number of items.")
        return

    unique_item_saver = []  # Local list for this PO
    user_total_cost = 0

    for item_num in range(1, user_item_counter + 1):
        user_id_product = input(f"Enter the {item_num} item's product ID: ").strip()
        try:
            user_item_number = int(input(f"Enter the total number of '{user_id_product}' ordered: ").strip())
            if user_item_number <= 0:
                print("Error: Quantity must be greater than zero.")
                return
        except ValueError:
            print("Error: Please enter a valid integer for item quantity.")
            return

        # Search for product
        po_index = None
        for idx, p in enumerate(all_products):
            if p.product_id.lower() == user_id_product.lower():
                po_index = idx
                break
        
        if po_index is None:
            print(f"Error: no product found for '{user_id_product}'.")
            return

        # Add to PO
        unique_item_saver.append({"product_id": user_id_product, "reorder_quantity": user_item_number})
        user_total_cost += all_products[po_index].unit_price * user_item_number

    # Create purchase order
    new_purchase_order = PurchaseOrder(
        user_po_number,
        user_vendor_id,
        user_date_created,
        unique_item_saver,
        user_total_cost,
        "shipping"
    )
    all_purchase_orders.append(new_purchase_order)
    print(f"New Purchase Order Added: {new_purchase_order}")

def view_purchase_order():
    po_sort_style = input(
        "Select Sort Option\n"
        "1. Purchase Order Number\n"
        "2. Purchase Order Date\n"
        "3. Purchase Order Shipping Status\n"
    ).strip()

    if not all_purchase_orders:
        print("Error: No purchase orders to display.")
        return

    if po_sort_style == "1":
        po_sorted = sorted(all_purchase_orders, key=lambda x: x.po_number)
    elif po_sort_style == "2":
        po_sorted = sorted(all_purchase_orders, key=lambda x: x.date_created)
    elif po_sort_style == "3":
        po_sorted = sorted(all_purchase_orders, key=lambda x: x.status)
    else:
        print("Invalid menu option. Please try again.")
        return

    for po in po_sorted:
        print(po)

def mark_purchase_order_received():
    if not all_purchase_orders:
        print("Error: No purchase orders found.")
        return

    purchase_order_id_finder = input("Enter the purchase order number: ").strip().lower()

    # Search for the purchase order
    po_index = next((i for i, po in enumerate(all_purchase_orders) 
                     if po.po_number.lower() == purchase_order_id_finder), None)

    if po_index is None:
        print("Order number not found.")
        return

    po = all_purchase_orders[po_index]

    if po.status.lower() == "received":
        print("Purchase Order already marked as received.")
        return

    # Mark as received
    po.status = "received"
    print(f"Purchase Order '{po.po_number}' marked as received.")

    # Update stock
    if not all_products:
        print("Error: No products found.")
        return

    # FIXED: Accessing dictionary keys instead of tuple unpacking
    for item in po.item_ordered:
        p_id = item["product_id"]
        # FIXED: Using the correct variable name for the quantity
        reorder_qty = int(item["reorder_quantity"]) 

        for x in all_products:
            if x.product_id.lower() == p_id.lower():
                print(f"Current stock for '{x.product_name}': {x.in_stock}")
                x.in_stock += reorder_qty  # FIXED: Added reorder_qty
                print(f"New stock for '{x.product_name}': {x.in_stock}")
                break
        else:
            print(f"Warning: Product '{p_id}' not found in product list.")
            
            
            
            
def save_everything():
    file_manager.save_inventory(all_products, all_vendors, all_purchase_orders)
    print("Inventory Information Saved")