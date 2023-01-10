"""
This is a simple algorithm to fetch Frappe apps components (Modules, DocTypes, Fields)
"""

import frappe

 # Getting all DocTypes of the site
doctypes = frappe.get_list('DocType', pluck='name')

# Getting all Modules of the site
# Set is to remove duplicates
modules = list(set(frappe.get_list('DocType', pluck='module')))

# Exporting data
file_type = 'xlsx'

# Initializaing the where and files
path = ''
for module in modules:
    with open(f'{path}/{module}.{file_type}', 'w') as file:
        file.write('')

# Getting DocType Fileds
def get_fields(doctype):
    fields = frappe.get_doc('DocType', doctype).fields
    r = []
    for field in fields:
        if field.label != None and field.label != 'Amended From':
            r.append(field.label)
    return r


# Start the algorithm
for module in modules:
    doctypes_of_each_module = frappe.db.sql(f'''SELECT name FROM `tabDocType` WHERE module='{module}';''')
    with open(f'Modules Translataions Excel Files of Each Frappe and ERPNext/{module}.{file_type}', 'a') as file:
        file.write(f'Module: {module}')
         # print(f'Module: {module}')
    for doctype in doctypes_of_each_module:
        with open(f'Modules Translataions Excel Files of Each Frappe and ERPNext/{module}.{file_type}', 'a') as file:
            file.write(f'\nDocType: {doctype[0]}')
        # print(f'\tDocType: {doctype[0]}')
        for field in get_fields(doctype[0]):
            with open(f'Modules Translataions Excel Files of Each Frappe and ERPNext/{module}.{file_type}', 'a') as file:
                file.write(f'\nField: {field}')
            # print(f'\t\tField: {field}')
                with open(f'Modules Translataions Excel Files of Each Frappe and ERPNext/{module}.{file_type}', 'a') as file:
                    file.write('\n')