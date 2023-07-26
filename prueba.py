lista_tuplas = [('usuario1', 'correo1@mail.com'), ('usuario2', 'correo2@mail.com'), ('usuario3', 'correo3@mail.com')]

usuario_eliminar = input('Ingrese el nombre del usuario que desea eliminar: ')

usuario_encontrado = False

for tupla in lista_tuplas:
    if usuario_eliminar in tupla:
        usuario_encontrado = True
        lista_tuplas.remove(tupla)

if usuario_encontrado:
    print('El usuario ha sido eliminado de la lista de tuplas.')
    print(lista_tuplas)
else:
    print('El usuario a eliminar no existe en la lista de tuplas.')