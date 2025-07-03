import xml.etree.ElementTree as ET




tree = ET.parse('new.xml')
root = tree.getroot()
# print(root)
# for i in root:
#     print(i.tag)
for i in root:
    print(i.tag, i.attrib)
