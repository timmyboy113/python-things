from xml.dom import minidom

def loader(var):
  xmldoc = minidom.parse('vars.xml')
  item = xmldoc.getElementsByTagName(var) 
  return item[0].attributes['name'].value