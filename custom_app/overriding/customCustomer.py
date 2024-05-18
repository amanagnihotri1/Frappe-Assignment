import frappe
from frappe.model.document import Document

class customCustomer(Document):
    def before_save(self):
        frappe.throw("this popup confirms that default class has been overidden")
    