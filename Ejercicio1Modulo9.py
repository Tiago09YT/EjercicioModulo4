listaPaises = input('Dame una lista de paises (separados por comas): ')
listaPaises = listaPaises.split(',')
#listaPaises = listaPaises.split(', ')
listaPaises = set(listaPaises)
print(listaPaises)