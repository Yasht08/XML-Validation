from lxml import etree
def validate_xml(xml_file, xsd_file):
    try:
        xml_tree = etree.parse(xml_file)
        xmlschema = etree.XMLSchema(file=xsd_file)
        is_valid = xmlschema.validate(xml_tree)

        if is_valid:
            print("XML document is valid.")
        else:
            print("XML document is not valid. Validation Errors:")
            for error in xmlschema.error_log:
                print(f"  Line {error.line}, Column {error.column}: {error.message}")

    except etree.ParseError as e:
        print(f"Error parsing XML: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    xml_file = "employee.xml"
    xsd_file = "employee_schema.xsd"

    validate_xml(xml_file, xsd_file)
