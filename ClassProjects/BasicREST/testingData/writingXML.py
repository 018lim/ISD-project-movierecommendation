import xml.etree.ElementTree as ET

root = ET.Element("Books")
book = ET.SubElement(root, "Book")

#data1
ET.SubElement(book, "Title").text = "Python"
authors = ET.SubElement(book, "Authors")
ET.SubElement(book, "Date").text = "2013"
ET.SubElement(book, "Publisher").text = "Springer"

ET.SubElement(authors, "Author").text="John"
ET.SubElement(authors, "Author").text="Bob"

#data2
ET.SubElement(book, "Title").text = "Information System"
authors = ET.SubElement(book, "Authors")
ET.SubElement(book, "Date").text = "2014"
ET.SubElement(book, "Publisher").text = "Elsevier"

ET.SubElement(authors, "Author").text="Andrew"
ET.SubElement(authors, "Author").text="Martin"


#data3
ET.SubElement(book, "Title").text = "Database"
authors = ET.SubElement(book, "Authors")
ET.SubElement(book, "Date").text = "2016"
ET.SubElement(book, "Publisher").text = "Wiley"

ET.SubElement(authors, "Author").text="Edward"
ET.SubElement(authors, "Author").text="David"

tree = ET.ElementTree(root)

tree.write('BookData.xml')