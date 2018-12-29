import shelve

shelf_file = shelve.open('CitiesInTohoku')
cities = ['Sendai', 'Yamagata', 'Fukushima']
shelf_file['cities'] = cities
shelf_file.close()

shelf_file = shelve.open('CitiesInTohoku')
print(type(shelf_file))
print(shelf_file['cities'])
shelf_file.close()
