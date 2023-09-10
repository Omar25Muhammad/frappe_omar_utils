@frappe.whitelist()
def get_em_all():
    """
    This is a simple algorithm to fetch Frappe apps components (Modules, DocTypes, Fields)
    """

    # Define the directory path to store the files
    path = "exported_files"  # You can change this to your desired directory

    # Ensure the directory exists or create it if not
    os.makedirs(path, exist_ok=True)

    # Getting all DocTypes of the site
    doctypes = frappe.get_list("DocType", pluck="name")

    # Getting all Modules of the site
    # IBFO: { Set } is to remove duplicates
    modules = list(set(frappe.get_list("DocType", pluck="module")))

    # Exporting data
    file_type = "xlsx"

    # Initialize the where and files
    for module in modules:
        with open(f"{path}/{module}.{file_type}", "w") as file:
            file.write("")

    # Start the algorithm
    for module in modules:
        doctypes_of_each_module = frappe.get_list(
            "DocType", filters={"module": module}, pluck="name"
        )
        with open(f"{path}/{module}.{file_type}", "a") as file:
            file.write(f"Module: {module}")
        for doctype in doctypes_of_each_module:
            with open(f"{path}/{module}.{file_type}", "a") as file:
                file.write(f"\nDocType: {doctype}")
            for field in get_fields(doctype):
                with open(f"{path}/{module}.{file_type}", "a") as file:
                    file.write(f"\nField: {field}\n")

    return f"Files exported to {path}"


def get_fields(doctype):
    """Getting Fields of DocType"""
    fields = frappe.get_doc("DocType", doctype).fields
    r = []
    for field in fields:
        if field.label is not None and field.label != "Amended From":
            r.append(field.label)
    return r
