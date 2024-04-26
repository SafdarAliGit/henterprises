# In your custom script file e.g., custom_script.py
import frappe

@frappe.whitelist()
def get_tp(item_code):
    tp = frappe.db.get_value("Item", {"name": item_code}, "tp")
    return tp

