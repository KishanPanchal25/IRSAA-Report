# Copyright (c) 2022, a and contributors
# For license information, please see license.txt

import frappe
from frappe import _, _dict
from erpnext.accounts.report.financial_statements import get_cost_centers_with_children

def execute(filters=None):
	columns, data = [], []
	return get_columns(), get_data(filters)



def get_data(filters):
	print(f"\n\n\n{filters}\n\n\n")
	_from, to = filters.get('from_date'), filters.get('to_date')

	conditions = " AND 1=1 "
	
	if(filters.get('Business Division')):conditions += f" AND business_division='{filters.get('Business Division')}' "
	if(filters.get('Business Line')):conditions += f" AND business_line='{filters.get('Business Line')}' "
	#if(filters.get('Business Division')):conditions += f" AND name='{filters.get('Business Division')}' "

	print(f"\n\n\n{conditions}\n\n\n")




	data = frappe.db.sql(f"""SELECT name, business_division, business_line,lead_name, company_name, email_id, lead_owner, status, 
							salutation, designation, gender, source, customer  FROM `tabLead`
							WHERE (creation BETWEEN '{_from}' AND '{to}') {conditions};""")
	
	print(f"\n\n\n{data}\n\n\n")
	return data


def get_columns():
	return[
		"Series:Data:200",
		"Business Division:Data:150",
		"Business Line:Data:150",
		"Person Name:Data:200",
		"Organization Name:Data:200",
		"Email Address:Data:200",
		"Lead Owner:Data:130",
		"Status:Data:150",
		"Salutation:Data:70",
		"Designation:Data:120",
		"Gender:Data:70",
		"Source:Data:70",
		"From Customer:Data:70",




	]
