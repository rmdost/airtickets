# Copyright (c) 2024, Rashid and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
    def before_save(self):
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
