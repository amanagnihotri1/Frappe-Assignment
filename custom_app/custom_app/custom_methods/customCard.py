import frappe
@frappe.whitelist()
def get_customer_count():
    data = frappe.db.sql("""SELECT COUNT(*) FROM `tabCustomer`;""")
    return {     
	"value": data,
	"fieldtype": "Int",
    }
@frappe.whitelist()
def get_active_students():
    students=frappe.db.sql("""SELECT COUNT(*) FROM `tabStudent`
                          WHERE active_check=1 AND stu_age>=18
                          """)
    return {     
	"value": students,
	"fieldtype": "Int",
    }