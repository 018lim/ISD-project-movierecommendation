import xml.etree.ElementTree as ET

tree = ET.parse('BookData.xml')
root = tree.getroot()

# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print('----------------')
        if(subelem.tag != 'Authors'):
            print(subelem.tag, ": ", subelem.text)
        else:
            for sub in subelem:
                print(sub.tag, ": ", sub.text)
