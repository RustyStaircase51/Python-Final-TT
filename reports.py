"""This file contains all reporting functions."""

import inventory_manager
from models import Product, Vendor, PurchaseOrder



def create_report():
    report_menu_options = input(
        "Reports Menu Options\n"
        "1. Full Inventory Report\n"
        "2. Total Inventory Value Report\n"
        "3. Open Purchase Orders Report\n"
    ).strip()

    report_lines = []  # Will hold the lines of the report for optional export

    # ---------------- Full Inventory Report ----------------
    if report_menu_options == "1":
        if inventory_manager.all_products:
            header = "Full Inventory Report\n"
            report_lines.append(header)
            report_lines.append(
                "Product ID | Product Name | Category | In Stock | Reorder Level | Reorder Quantity | Unit Price | Vendor ID | Active Status"
            )
            for p in inventory_manager.all_products:
                line = (
                    f"{p.product_id} | {p.product_name} | {p.category} | {p.in_stock} | "
                    f"{p.reorder_level} | {p.reorder_quantity} | ${p.unit_price:.2f} | {p.vendor_id} | {p.active_status}"
                )
                report_lines.append(line)
            print("\n".join(report_lines))
        else:
            print("No products to report.")
            return

    # ---------------- Total Inventory Value Report ----------------
    elif report_menu_options == "2":
        if inventory_manager.all_products:
            total_value = 0
            header = "Total Inventory Value Report\n"
            report_lines.append(header)
            report_lines.append("Product ID | Product Name | Category | In Stock | Unit Price | Total Value")
            for p in inventory_manager.all_products:
                product_value = p.in_stock * p.unit_price
                total_value += product_value
                line = (
                    f"{p.product_id} | {p.product_name} | {p.category} | {p.in_stock} | "
                    f"${p.unit_price:.2f} | ${product_value:.2f}"
                )
                report_lines.append(line)
            report_lines.append(f"\nTotal inventory value: ${total_value:.2f}")
            print("\n".join(report_lines))
        else:
            print("No products to report.")
            return

    # ---------------- Open Purchase Orders Report ----------------
    elif report_menu_options == "3":
        if inventory_manager.all_purchase_orders:
            header = "Open Purchase Orders Report\n"
            report_lines.append(header)
            report_lines.append("PO Number | Vendor ID | Date Created | Item Ordered | Total Cost | Status")
            for po in inventory_manager.all_purchase_orders:
                if po.status.lower() == "shipping":
                    line = (
                        f"{po.po_number} | {po.vendor_id} | {po.date_created} | {po.item_ordered} | "
                        f"${po.total_cost:.2f} | {po.status}"
                    )
                    report_lines.append(line)
            if len(report_lines) == 2:
                print("No open purchase orders to report.")
                return
            print("\n".join(report_lines))
        else:
            print("No purchase orders to report.")
            return

    else:
        print("Invalid menu option. Please try again.")
        return

    # ---------------- Export Report to TXT ----------------
    export_option = input("\nDo you want to export this report to a TXT file? (yes/no): ").strip().lower()
    if export_option == "yes":
        filename = "report_export.txt"
        with open(filename, "w") as file:
            file.write("\n".join(report_lines))
        print(f"Report exported successfully as '{filename}'")
    else:
        print("Report not exported.")