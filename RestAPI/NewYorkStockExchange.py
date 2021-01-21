import xml.etree.ElementTree as xml

stock = xml.parse('nyse.xml').getroot()
print('\n{:<40} {:<10} {:<10} {:<10} {:<10}'.format('COMPANY', 'LAST', 'CHANGE', 'MIN', 'MAX'))
print('='*85)
for i in range(len(stock)-1):
    x = stock[i]
    print('{:<40} {:<10} {:<10} {:<10} {:<10}'.format(x.text,
                                                      x.attrib['last'],
                                                      x.attrib['change'],
                                                      x.attrib['min'],
                                                      x.attrib['max']))