# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
	def validate(self):
		total_amount = 0.0

		for items in self.expense_item:
			if items.amount:
				total_amount += float(items.amount)

		self.total_amount = total_amount
