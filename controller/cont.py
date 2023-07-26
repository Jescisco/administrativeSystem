from model.modelo import Usuario

class ControladorUsuarios(Usuario):
     
    #Controlador de Miembros

    def buscar_miembros(self, nombre):
        respuesta= self.search_miembros(nombre)
        return respuesta
    
    def nuevo_voluntario(self, cedula, nombre, telefono, genero, disponibilidad):
        respuesta=self.new_register(cedula, nombre, telefono, genero, disponibilidad)
        return respuesta
    
    def editar_voluntario(self, id, cedula, nombre, telefono, genero, disponibilidad):
        respuesta=self.editMembers(id, cedula, nombre, telefono, genero, disponibilidad) 
        return respuesta
    
    def mostrar_voluntarios(self):
        respuesta=self.view_registers()
        return respuesta
    
    def eliminar_voluntario(self, id):
        respuesta=self.delete_register(id)
        return respuesta

    #controlador del login

    def userVerify(self, usuario, password):
        respuesta=self.login_user(usuario, password)
        return respuesta
    
    def newUser(self, usuario, password, level):
        respuesta=self.insert_user(usuario, password, level)
        return respuesta
    
    def viewLoginUsers(self):
        respuesta=self.view_loginUsers()
        return respuesta
        
    def editarAdmin(self, id, usuario, password, level):
        respuesta=self.EditAdm(id, usuario, password, level) 
        return respuesta
    
    def eliminarAdmin(self, id):
        respuesta=self.deleteAdm(id)
        return respuesta
    
    #Controlador de movimientos economicos
    #INGRESOS

    def buscador_ingresos(self, nombre):
        respuesta=self.search_eco_ingre(nombre)
        return respuesta

    def insertar_eco_ingre(self, concepto, fecha, monto, donante_id, forma_pago_id):
        respuesta = self.insert_eco_ingre(concepto, fecha, monto, donante_id, forma_pago_id)
        return respuesta

    def mostrar_eco_ingre(self):
        respuesta = self.view_eco_ingre()
        return respuesta

    def actualizar_eco_ingre(self, id, u_concepto, u_fecha, u_monto, u_donante_id, u_forma_pago_id):
        respuesta = self.update_eco_ingre(id, u_concepto, u_fecha, u_monto, u_donante_id, u_forma_pago_id)
        print(respuesta)
        return respuesta
    
    def eliminar_eco_ingre(self, id):
        respuesta = self.delete_eco_ingre(id)
        return respuesta

    #Egresos

    def buscador_egresos(self, nombre):
        respuesta=self.search_eco_egre(nombre)
        return respuesta
    
    def insertar_eco_egre(self, concepto, fecha, monto, proveedor_id, forma_pago_id):
        respuesta = self.insert_eco_egre(concepto, fecha, monto, proveedor_id, forma_pago_id)
        return respuesta

    def mostrar_eco_egre(self):
        respuesta = self.view_eco_egre()
        return respuesta

    def actualizar_eco_egre(self, id, u_concepto, u_fecha, u_monto, u_proveedor_id, u_forma_pago_id):
        respuesta = self.update_eco_egre(id, u_concepto, u_fecha, u_monto, u_proveedor_id, u_forma_pago_id)
        return respuesta
    
    def eliminar_eco_egre(self, id):
        respuesta = self.delete_eco_egre(id)
        return respuesta
    
    #DONANTES

    def insertar_donantes(self, nombre, direccion, telefono, correo):
        respuesta = self.insert_donantes(nombre, direccion, telefono, correo)
        return respuesta
    
    def mostar_donantes(self):
        respuesta = self. view_donantes()
        return respuesta
    
    def actualizar_donantes(self, id, u_nombre, u_direccion, u_telefono, u_correo):
        respuesta = self.update_donantes(id, u_nombre, u_direccion, u_telefono, u_correo)
        return respuesta
    
    def eliminar_donantes(self, id):
        respuesta = self.delete_donantes(id)
        return respuesta
    
    #PROVEEDORES

    def insertar_proveedores(self, nombre, direccion, telefono, correo):
        respuesta = self.insert_proveedores(nombre, direccion, telefono, correo)
        return respuesta
    
    def mostar_proveedores(self):
        respuesta = self. view_proveedores()
        return respuesta
    
    def actualizar_proveedores(self, id, u_nombre, u_direccion, u_telefono, u_correo):
        respuesta = self.update_proveedores(id, u_nombre, u_direccion, u_telefono, u_correo)
        return respuesta
    
    def eliminar_proveedores(self, id):
        respuesta = self.delete_proveedores(id)
        return respuesta
    
    #FORMAS DE PAGO

    def insertar_formas_pago(self, nombre, descripcion):
        respuesta = self.insert_formas_pago(nombre, descripcion)
        return respuesta
    
    def mostar_formas_pago(self):
        respuesta = self. view_formas_pago()
        return respuesta
    
    def actualizar_formas_pago(self, id, u_nombre, u_descripcion):
        respuesta = self.update_formas_pago(id, u_nombre, u_descripcion)
        return respuesta
    
    def eliminar_formas_pago(self, id):
        respuesta = self.delete_formas_pago(id)
        return respuesta
    
    #EVENTOS

    def insertar_eventos(self, nombre, fecha, ubicacion, descripcion, responsable_id):
        respuesta = self.insert_eventos(nombre, fecha, ubicacion, descripcion, responsable_id)
        return respuesta

    def mostrar_eventos(self):
        respuesta = self.view_eventos()
        return respuesta

    def actualizar_eventos(self, id, u_nombre, u_fecha, u_ubicacion, u_descripcion, u_responsable_id):
        respuesta = self.update_eventos(id, u_nombre, u_fecha, u_ubicacion, u_descripcion, u_responsable_id)
        return respuesta
    
    def eliminar_eventos(self, id):
        respuesta = self.delete_eventos(id)
        return respuesta

    def buscar_eventos(self, desc):
        respuesta = self.search_eventos(desc)
        return respuesta







    
