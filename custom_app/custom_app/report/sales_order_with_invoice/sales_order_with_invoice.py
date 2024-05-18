# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe

def get_columns():
    return [
        {"fieldname": "sales_order", "label": "Sales Order", "fieldtype": "Link", "options": "Sales Order", "width": 120},
        {"fieldname": "sales_order_item", "label": "Sales Order Item", "fieldtype": "Link", "options": "Sales Order Item", "width": 120},
        {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 120},
        {"fieldname": "qty", "label": "Quantity", "fieldtype": "Float", "width": 100},
        {"fieldname": "sales_invoice", "label": "Sales Invoice", "fieldtype": "Link", "options": "Sales Invoice", "width": 120},
        {"fieldname": "sales_invoice_item", "label": "Sales Invoice Item", "fieldtype": "Link", "options": "Sales Invoice Item", "width": 120},
        {"fieldname": "invoiced_qty", "label": "Invoiced Quantity", "fieldtype": "Float", "width": 100}
    ]

def get_data(filters):
    sales_order_items = frappe.db.sql("""
        SELECT
            slo.name AS sales_order,
            soi.item_code,
            soi.item_name,
            soi.qty,
            soi.rate,
            soi.amount AS total_amount,
            si.name AS sales_invoice
        FROM
            `tabSales Order` slo
        INNER JOIN
            `tabSales Order Item` soi ON slo.name = soi.parent
        INNER JOIN
            `tabSales Invoice Item` sii ON soi.item_code = sii.item_code
        INNER JOIN
            `tabSales Invoice` si ON sii.parent = si.name
        WHERE
            slo.docstatus = 1
    """, as_dict=1)

    return sales_order_items

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data
