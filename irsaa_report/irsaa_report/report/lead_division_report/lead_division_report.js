// Copyright (c) 2022, a and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Lead Division Report"] = {
	"filters": [
		{
			"fieldname":"Business Division",
			"label": __("Business Division"),
			"fieldtype": "Link",
			"options": "Business Division",
			"default": frappe.defaults.get_user_default("Business Division"),
			"reqd": 1
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"Business Line",
			"label": __("Business Line"),
			"fieldtype": "Link",
			"options": "Cost Center",
			//"default": frappe.defaults.get_user_default("Cost Center")
			get_data: function(txt) {
				if (frappe.query_report.get_filter_value('Business Division')) {
					var name = frappe.query_report.get_filter_value("Business Division");
					return frappe.db.get_list("Cost Center", {fields: ['business_line'], filters: {"business_division": name}});
					//return frappe.db.get_link_options("Activity Log", txt, {"user":name});
				}
				else {
					return [];
				};
			},
			on_change: function(query_report) {
				query_report.refresh();
			},
				
				

		}
	]
};
