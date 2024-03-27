# In your custom script file e.g., custom_script.py
import frappe

@frappe.whitelist()
def get_user_full_name(owner):
    full_name = frappe.db.get_value("User", {"name": owner}, "full_name")
    return full_name
