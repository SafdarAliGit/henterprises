import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from erpnext.setup.doctype.sales_partner.sales_partner import SalesPartner
from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.model.naming import getseries, make_autoname
from frappe.utils import cstr, filter_strip_join
from frappe.website.website_generator import WebsiteGenerator


class SalesInvoiceOverrides(SalesInvoice):
    def on_submit(self):
        frappe.msgprint("===========================")
        self.booker = frappe.session.user.full_name
        self.save()
