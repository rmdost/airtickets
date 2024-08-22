# Copyright (c) 2024, Rashid and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        total_add_ons = sum([item.amount for item in self.add_ons])
        self.total_amount = self.flight_price + total_add_ons

        # Ensure each add-on is unique
        add_on_items = [item.item for item in self.add_ons]
        if len(add_on_items) != len(set(add_on_items)):
            frappe.throw("Duplicate add-ons are not allowed.")
