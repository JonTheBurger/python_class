# Lesson 7
# XML or 'Extensible Markup Language' is a common hierarchical storage format
import xml.etree.cElementTree as ET


def create_xml_file():
    cust = ET.Element('Customers')
    ET.SubElement(cust, 'Customer', name='Mountain Inc.', city='Denver', state='CO').text = str(30000)
    ET.SubElement(cust, 'Customer', name='SteelView LLC.', city='Phoenix', state='AZ').text = str(45000)
    tree = ET.ElementTree(cust)
    tree.write('example.xml')


def read_xml_file():
    tree = ET.parse('example.xml')
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib, child.text)
        # We can edit attributes with set
        child.set('name', 'Greg Corp.')
        # We can also edit text as such
        child.text = 9999
        print(child.tag, child.attrib, child.text)

create_xml_file()
read_xml_file()
