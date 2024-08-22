// Copyright (c) 2024, Rashid and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Map colors to Status field
        frm.fields_dict['status'].df.options = [
            {"label": "Booked", "value": "Booked", "color": "gray"},
            {"label": "Checked-In", "value": "Checked-In", "color": "purple"},
            {"label": "Boarded", "value": "Boarded", "color": "green"}
        ];
    }
});
