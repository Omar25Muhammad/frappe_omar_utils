"""This piece of code looks up for a given word that is a value of a field, showing its DocType,
 Document, and DocField."""

import frappe
import time


def spotting(wanted, app_name):
    # wanted = ''  # Type here the value you are looking for
    # app_name = ''  # Type here the name of app which you wanna look into it
    ls = [], fou = []
    start = time.time()
    doctypes = frappe.get_list('DocType', pluck='name', filters=[
        ['module', 'in', frappe.get_module_list(app_name)]])

    for doctype in doctypes:
        try:
            for doc in frappe.get_list(doctype, pluck='name'):
                ls.append(frappe.get_doc(doctype, doc).as_dict())
                for i in ls:
                    if wanted in i.values():
                        fou.append(
                            f'Found. In DocType: {i.doctype}, Document: {i.name}, at Field Name: {list(i.keys())[list(i.values()).index(wanted)]}')
        except:
            ...
    end = time.time()
    for count, found in enumerate(list(set(fou)), start=1):
        print(f'{count}. {found}')
    print(f'---------\nProcess took: {end-start:.2f}sec.\n---------')
