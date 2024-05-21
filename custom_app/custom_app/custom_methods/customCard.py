import frappe
@frappe.whitelist()
def get_customer_count(): # function to get count of customer present in customer doctype
    data = frappe.db.sql("""SELECT COUNT(*) FROM `tabCustomer`;""")
    return {     
	"value": data,
	"fieldtype": "Int",
    }
@frappe.whitelist()
def get_active_students(): # function to get count of active students from custom doctype based on few given filters
    students=frappe.db.sql("""SELECT COUNT(*) FROM `tabStudent`
                          WHERE active_check=1 AND stu_age>=18
                          """)
    return {     
	"value": students,
	"fieldtype": "Int",
    }
