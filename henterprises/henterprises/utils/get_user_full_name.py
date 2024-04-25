# In your custom script file e.g., custom_script.py
import frappe

@frappe.whitelist()
def get_user_full_name():
    user = frappe.session.user
    full_name = frappe.db.get_value("User", {"name": user}, "full_name")
    return full_name

