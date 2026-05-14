"""
This file contains functions for saving and loading all inventory data
(products, vendors, purchase orders) using a single JSON file.
"""

import json
from models import Product, Vendor, PurchaseOrder

# Unified file path
DATA_FILE = "inventory_data.json"
SAMPLE_DATA = "sample_data.json"

# -----------------------------
# SAVE FUNCTION
# -----------------------------
def save_inventory(all_products, all_vendors, all_purchase_orders):
    data = {
        "products": [
            {
                "product_id": p.product_id,
                "product_name": p.product_name,
                "category": p.category,
                "in_stock": p.in_stock,
                "reorder_level": p.reorder_level,
                "reorder_quantity": p.reorder_quantity,
                "unit_price": p.unit_price,
                "vendor_id": p.vendor_id,
                "active_status": p.active_status
            }
            for p in all_products
        ],
        "vendors": [
            {
                "vendor_id": v.vendor_id,
                "vendor_name": v.vendor_name,
                "contact_name": v.contact_name,
                "phone": v.phone,
                "email": v.email,
                "address": v.address
            }
            for v in all_vendors
        ],
        "purchase_orders": [
            {
                "po_number": po.po_number,
                "vendor_id": po.vendor_id,
                "date_created": po.date_created,
                "item_ordered": po.item_ordered,  # [[product_id, qty], ...]
                "total_cost": po.total_cost,
                "status": po.status
            }
            for po in all_purchase_orders
        ]
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# LOAD FUNCTION
# -----------------------------
def load_inventory():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        all_products = [
            Product(
                p["product_id"],
                p["product_name"],
                p["category"],
                p["in_stock"],
                p["reorder_level"],
                p["reorder_quantity"],
                p["unit_price"],
                p["vendor_id"],
                p["active_status"]
            )
            for p in data.get("products", [])
        ]

        all_vendors = [
            Vendor(
                v["vendor_id"],
                v["vendor_name"],
                v["contact_name"],
                v["phone"],
                v["email"],
                v["address"]
            )
            for v in data.get("vendors", [])
        ]

        all_purchase_orders = [
            PurchaseOrder(
                po["po_number"],
                po["vendor_id"],
                po["date_created"],
                po["item_ordered"],
                po["total_cost"],
                po["status"]
            )
            for po in data.get("purchase_orders", [])
        ]

        return all_products, all_vendors, all_purchase_orders

    except FileNotFoundError:
        # If file doesn't exist, return empty lists
        return [], [], []
    
def load_sample():
    try:
        with open(SAMPLE_DATA, "r") as f:
            data = json.load(f)

        all_products = [
            Product(
                p["product_id"],
                p["product_name"],
                p["category"],
                p["in_stock"],
                p["reorder_level"],
                p["reorder_quantity"],
                p["unit_price"],
                p["vendor_id"],
                p["active_status"]
            )
            for p in data.get("products", [])
        ]

        all_vendors = [
            Vendor(
                v["vendor_id"],
                v["vendor_name"],
                v["contact_name"],
                v["phone"],
                v["email"],
                v["address"]
            )
            for v in data.get("vendors", [])
        ]

        all_purchase_orders = [
            PurchaseOrder(
                po["po_number"],
                po["vendor_id"],
                po["date_created"],
                po["item_ordered"],
                po["total_cost"],
                po["status"]
            )
            for po in data.get("purchase_orders", [])
        ]

        return all_products, all_vendors, all_purchase_orders

    except FileNotFoundError:
        # If file doesn't exist, return empty lists
        return [], [], []