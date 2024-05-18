frappe.ready(function() {
	let res = frappe.web_form.get_values();
		let emaildata = res.email;
		sendEmailToUser(emaildata);
})
function sendEmailToUser(email) {
    frappe.call({
        method: 'customer_management.customer_management.web_form.email_web_form.email_web_form.send_email',
        args: {
            email: email 
        },
        callback: function(response) {
            // Handle the response
            if (response.message) {
               frappe.msgprint("Registered");
            } else {
                frappe.error('Failed to register:', response.error);
            }
        }
    });
}