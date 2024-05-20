frappe.ready(function() {
frappe.web_form.events.on('after_save',()=>
    {
        let res = frappe.web_form.get_values();
            let emaildata = res.email;
            console.log(emaildata)
            sendEmailToUser(emaildata);
    })
})
function sendEmailToUser(email) {
    frappe.call({
        method: 'custom_app.custom_app.web_form.desired_tourist_destination_information.desired_tourist_destination_information.send_email',
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
