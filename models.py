"""This file contains the class definitions for Products, Vendors, and Purchase Orders."""

class Product:
    def __init__(self, product_id, product_name, category, in_stock, reorder_level, reorder_quantity, unit_price, vendor_id, active_status):
        self.product_id = str(product_id)
        self.product_name = str(product_name)
        self.category = str(category)
        self.in_stock = int(in_stock)
        self.reorder_level = int(reorder_level)
        self.reorder_quantity = int(reorder_quantity)
        self.unit_price = float(unit_price)
        self.vendor_id = str(vendor_id)
        self.active_status = bool(active_status)

    def __repr__(self):
        return (
            f"ID: {self.product_id} | Name: {self.product_name} | Category: {self.category} | "
            f"In Stock: {self.in_stock} | Reorder Level: {self.reorder_level} | "
            f"Reorder Quantity: {self.reorder_quantity} | Unit Price: ${self.unit_price:.2f} | "
            f"Vendor ID: {self.vendor_id} | Active Status: {self.active_status}"
        )

    def to_dict(self):
        return self.__dict__.copy()


class Vendor:
    def __init__(self, vendor_id, vendor_name, contact_name, phone, email, address):
        self.vendor_id = str(vendor_id)
        self.vendor_name = str(vendor_name)
        self.contact_name = str(contact_name)
        self.phone = str(phone)
        self.email = str(email)
        self.address = str(address)

    def __repr__(self):
        return (
            f"Vendor ID: {self.vendor_id} | Vendor Name: {self.vendor_name} | "
            f"Contact Name: {self.contact_name} | Phone: {self.phone} | "
            f"Email: {self.email} | Address: {self.address}"
        )

    def to_dict(self):
        return self.__dict__.copy()


class PurchaseOrder:
    def __init__(self, po_number, vendor_id, date_created, item_ordered, total_cost, status):
        """
        item_ordered: list of dicts, e.g. [{"product_id": "1012", "quantity": 5}]
        total_cost: float
        status: str ("shipping" or "received")
        """
        self.po_number = str(po_number)
        self.vendor_id = str(vendor_id)
        self.date_created = str(date_created)
        self.item_ordered = item_ordered  # list of dicts
        self.total_cost = float(total_cost)
        self.status = str(status)

    def __repr__(self):
        items_str_list = []
        for item in self.item_ordered:
            if isinstance(item, dict):
                pid = item.get('product_id', 'Unknown')
                qty = item.get('reorder_quantity', '?')
                items_str_list.append(f"{pid} x {qty}")
            else:  # assume it's a Product object
                items_str_list.append(f"{getattr(item, 'user_id_product', 'Unknown')} x {getattr(item, 'reorder_quantity', '?')}")
        items_str = ", ".join(items_str_list)
    
        return (
            f"PO number: {self.po_number} | Vendor ID: {self.vendor_id} | "
            f"Date Created: {self.date_created} | Items Ordered: [{items_str}] | "
            f"Total Cost: ${self.total_cost:.2f} | Status: {self.status}"
        )

    def to_dict(self):
        return {
            "po_number": self.po_number,
            "vendor_id": self.vendor_id,
            "date_created": self.date_created,
            "item_ordered": self.item_ordered.copy(),
            "total_cost": self.total_cost,
            "status": self.status
        }