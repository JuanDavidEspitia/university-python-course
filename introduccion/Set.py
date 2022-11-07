# Collecion de tipo set
# No tiene un orden
# No permite elementos duplicados
# No poseen indices
# El orden es aleatorio
# No se pueden modificar los elementos de en un SET
# Pero si se pueden agregar y eleminar elementos

# set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

#largo
print(len(planetas))

# revisar si un elemento está presente
print('Marte' in planetas)  # Responde con un Booleano

# agregar un elemento
planetas.add('Tierra')
print( planetas)

#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)

# eliminar elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)

# eliminar elemento sin arrojar error
planetas.discard('Júpiters')
print(planetas)

# limpiar set
planetas.clear()
print(planetas)

# eliminar el set
#del planetas
#print(planetas)









