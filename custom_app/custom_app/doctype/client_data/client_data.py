# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class ClientData(Document):
    @frappe.whitelist(allow_guest=True)
    def validate(self):
        if not (self.first_name.strip() and self.last_name.strip() and self.allow_check):
            frappe.throw("Please fill in all fields (first name, last name) and tick the checkbox.")
        else:
            self.full_name = f"{self.first_name} {self.last_name}"
pass
@frappe.whitelist(allow_guest=True)
def create_client(fname, lname):
    try:
        doc_data = frappe.get_doc({
            'doctype': 'Client Data',
            'first_name': str(fname),
            'last_name': str(lname),
            'allow_check': 1
        })
        doc_data.insert()
        return {"status": "success", "message": "Client created successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@frappe.whitelist(allow_guest=True)
def get_client(client_id):
    try:
        doc = frappe.get_doc('Client Data', client_id)
        return doc.as_dict()
    except frappe.DoesNotExistError as e:
        frappe.throw(f"Client {client_id} does not exist")
    except Exception as e:
        frappe.log_error(str(e))

@frappe.whitelist(allow_guest=True)
def update_client(client_id, field_name, field_value):
    try:
        doc = frappe.get_doc('Client Data', client_id)
        if not doc:
            frappe.throw("Error client with this id does not exist")
        doc.field_name = field_value
        doc.save()
        return "Client updated successfully"
    except frappe.DoesNotExistError as e:
        frappe.throw(f"Client {client_id} does not exist")
    except Exception as e:
        frappe.log_error(str(e))

@frappe.whitelist(allow_guest=True)
def delete_client(client_id):
    try:
        frappe.delete_doc('Client Data', client_id)
        return "Client deleted successfully"
    except frappe.DoesNotExistError as e:
        frappe.throw(f"Client {client_id} does not exist")
    except Exception as e:
        frappe.log_error(str(e))
