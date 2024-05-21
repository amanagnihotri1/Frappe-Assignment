import frappe

def get_context(context):
	# do your magic here
	pass
@frappe.whitelist(allow_guest=True)
def send_email(email): # function to send Email Address to given email Id
    try:
        # This function triggers email sending to email address provided as argument 
        frappe.sendmail( 
            recipients=email,  
            subject='Customer registration', 
            content='Thank you for registering with us!', 
            now=True 
        )

        return "Form submitted successfully"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Form Submission Error")
        return "An error occurred while submitting the form"	
