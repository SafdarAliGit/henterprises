# In your custom script file e.g., custom_script.py
import frappe

@frappe.whitelist()
def get_territory(customer):
    territory = frappe.db.get_value("Customer", {"name": customer}, "territory")
    return territory

