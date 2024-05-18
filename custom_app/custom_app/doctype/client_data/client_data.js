// Copyright (c) 2024, Aman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Data", {
	refresh(frm) {
        frm.add_custom_button(__('Add Subject'), () => { // function to add button to Client Data form
        let customModal=new frappe.ui.Dialog({ // this method creates new Dialog
            title: 'Enter details',
    fields: [
        {
            label: 'Subject Code',
            fieldname: 'sub_code',
            fieldtype: 'Int'
        },
        {
            label: 'Subject Name',
            fieldname: 'sub_name',
            fieldtype: 'Data'
        },
        {
            label: 'Marks Scored',
            fieldname: 'sub_marks',
            fieldtype: 'Int'
        }
    ],
    size: 'small', 
    primary_action_label: 'Submit',
    primary_action:(values) =>{ // function to add row and data into it
        frm.add_child('subjects',{'sub_code':values.sub_code,'sub_name':values.sub_name,'sub_marks':values.sub_marks});
       frm.refresh_field('subjects');
        customModal.hide();
    }
});
customModal.show();
        })  
	},
});
