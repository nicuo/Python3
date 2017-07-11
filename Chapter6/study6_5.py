from study6_4 import Element

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number':1}

# hydrogen = Element(el_dict['name'], el_dict['symbol'],el_dict['number'])
hydrogen = Element(**el_dict)
hydrogen.name
