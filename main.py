"""This file contains the main menu and starts up the program."""

import file_manager
import inventory_manager
import models
import file_manager
import reports

inventory_manager.all_products, inventory_manager.all_vendors, inventory_manager.all_purchase_orders = file_manager.load_inventory()


while True:  # To get out of this menu you have to type "quit" and press ENTER.
    print("\nWelcome to the Home Menu!\n\nType in a number + press \"ENTER\" to select a menu. Type \"quit\" to exit program.")
    menu_1 = input("1. Products\n2. Vendors\n3. Purchase Orders\n4. Reports\n5. Load Sample Data\n").strip()

    if menu_1 == "1":
        while True:  # To get out of this menu you have to type "back" and press ENTER
            print("\nYou Selected the Products Menu. Select a number or type \"back\" to go back.")
            menu_product_options = input(
                "1. Add New Product\n"
                "2. View All Products\n"
                "3. Search for Products\n"
                "4. Edit Product\n"
                "5. Display Low Stock Products\n"
            ).strip().lower()

            if menu_product_options == "1":
                inventory_manager.add_product()

            elif menu_product_options == "2":
                inventory_manager.view_all_products()

            elif menu_product_options == "3":
                inventory_manager.search_products()

            elif menu_product_options == "4":
                inventory_manager.edit_product()

            elif menu_product_options == "5":
                inventory_manager.low_stock_display()

            elif menu_product_options == "back":
                print("\nGoing to Previous Menu...")
                break

            else:
                print("\nError: Invalid menu option. Please try again.")

    elif menu_1 == "2":
        while True:
            print("\nYou Selected the Vendors Menu. Select a number or type \"back\" to go back.")
            menu_vendor_options = input(
                "1. Add New Vendor\n"
                "2. View All Vendors\n"
                "3. Search for Vendors\n"
                "4. Edit Vendor\n"
            ).strip().lower()

            if menu_vendor_options == "1":
                inventory_manager.add_vendor()

            elif menu_vendor_options == "2":
                inventory_manager.view_all_vendors()

            elif menu_vendor_options == "3":
                inventory_manager.search_vendors()

            elif menu_vendor_options == "4":
                inventory_manager.edit_vendor()

            elif menu_vendor_options == "back":
                print("\nGoing to Previous Menu...")
                break

            else:
                print("\nError: Invalid menu option. Please try again.")

    elif menu_1 == "3":
        while True:
            print("\nYou Selected the Purchase Orders Menu. Select a number or type \"back\" to go back.")
            menu_po_options = input(
                "1. Add New Purchase Order\n"
                "2. View Purchase Orders\n"
                "3. Mark Purchase Order as Received\n"
            ).strip().lower()

            if menu_po_options == "1":
                inventory_manager.add_purchase_order()

            elif menu_po_options == "2":
                # Make sure this method exists in inventory_manager
                inventory_manager.view_purchase_order()

            elif menu_po_options == "3":
                inventory_manager.mark_purchase_order_received()

            elif menu_po_options == "back":
                print("\nGoing to Previous Menu...")
                break

            else:
                print("\nError: Invalid menu option. Please try again.")

    elif menu_1 == "4":
        reports.create_report()
    
    elif menu_1 == "5":
        print("Saving current data...")
        inventory_manager.save_everything()
        print("Saved!")
    
        inventory_manager.all_products, inventory_manager.all_vendors, inventory_manager.all_purchase_orders = file_manager.load_sample()
        print("Loaded Sample Data!")
        
    elif menu_1.lower() == "quit":
        print("Now exiting...")
        save_question = input("\n1. Save\n2. Exit Without Saving\n")
        if save_question == "1":
            print("\nSaving...")
            inventory_manager.save_everything()
            print("Saved!")
            print("\nExiting program...")
            print("Goodbye!")
        if save_question == "2":
            print("Deleting current files...")
            print("Deleted!")
            print("\nExiting program...")
            print("Goodbye!")
        break

    else:
        print("\nError: Invalid menu option. Please try again.")