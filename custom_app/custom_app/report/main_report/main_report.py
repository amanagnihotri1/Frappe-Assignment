# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "customer_name", "label": "Customer Name", "fieldtype": "Data", "options": "Customer", "width": "120"},
        {"fieldname": "sales_order", "label": "Sales Order", "fieldtype": "Link", "options": "Sales Order", "width": "120"},
        {"fieldname": "delivery_date", "label": "Delivery Date", "fieldtype": "Date", "width": "120"},
        {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": "120"},
        {"fieldname": "item_name", "label": "Item Name", "fieldtype": "Data", "width": "120"},
        {"fieldname": "item_qty", "label": "Item Qty", "fieldtype": "Float", "width": "120"}
    ]

    data = frappe.db.sql("""
        SELECT salOrder.customer_name, salOrder.name AS sales_order, salOrder.delivery_date, salItem.item_code, salItem.item_name, salItem.qty AS item_qty
        FROM `tabSales Order` salOrder
        INNER JOIN `tabSales Order Item` salItem ON salOrder.name = salItem.parent
        """, as_dict=True)

    return columns, data