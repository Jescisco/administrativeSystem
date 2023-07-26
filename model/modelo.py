import mariadb

class Connection:

    def connect(self):
        try:
            connection = mariadb.connect(host='localhost',user='root',password='',database='nueva_acropolis')
            return connection
        except mariadb.Error as error:
            return error

    def setExecute(self, query):
        conn=self.connect()
        cursor=conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            row=cursor.rowcount
            return row
        except mariadb.Error as error:
            return error
        finally:
            conn.close()

    def getExecute(self, query):
        conn=self.connect()
        cursor=conn.cursor()
        try:
            cursor.execute(query)
            resultados=cursor.fetchall()
            return resultados
        except mariadb.Error as error:
            return error
        finally:
            conn.close()   

class Usuario(Connection):
    def search_miembros(self, desc):
        query = f"SELECT * FROM voluntarios WHERE nombre_completo = '{desc}'"
        resultado = self.getExecute(query)
        return resultado

    def editMembers(self, id, cedula, nombre, telefono, genero, disponibilidad):
        query= f"UPDATE voluntarios SET cedula= '{cedula}', nombre_completo= '{nombre}', telefono= '{telefono}', genero= '{genero}', disponibilidad= '{disponibilidad}' WHERE id= '{id}'"
        resultado=self.setExecute(query)
        return resultado

    def login_user(self, username, password):
        query = f"SELECT * FROM login WHERE user='{username}' AND password='{password}'"
        result =self.getExecute(query)
        return result
        
    def insert_user(self, usuario, password, level):
        query = f"INSERT INTO login(user, password, level_user) VALUES ('{usuario}', '{password}', '{level}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="Insertado"
        elif resultado==0:
            respuesta="No se insertó"
        else:
            respuesta=resultado
        return respuesta
    
    def new_register(self, cedula, nombre, telefono, genero, disponibilidad):
        query = f"INSERT INTO voluntarios(cedula, nombre_completo, telefono, genero, disponibilidad) VALUES ('{cedula}', '{nombre}', '{telefono}', '{genero}', '{disponibilidad}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="Insertado"
        elif resultado==0:
            respuesta="No se insertó"
        else:
            respuesta=resultado
        return respuesta
    
    def view_registers(self):
        query = f"SELECT * FROM voluntarios ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def delete_register(self, id):
        query = f"DELETE FROM voluntarios WHERE id = '{id}'"
        result=self.setExecute(query)
        return result
    
    def view_loginUsers(self):
        query = f"SELECT * FROM login ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def EditAdm(self, id, usuario, password, level):
        query = f"UPDATE login SET user='{usuario}', password='{password}', level_user='{level}' WHERE id='{id}'"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="Insertado"
        elif resultado==0:
            respuesta="No se insertó"
        else:
            respuesta=resultado
        return respuesta
    
    def deleteAdm(self, id):
        query = f"DELETE FROM login WHERE id = '{id}'"
        result=self.setExecute(query)
        return result
    

#TABLA INGRESOS    

    def insert_eco_ingre(self, concepto, fecha, monto, donante_id, forma_pago_id):
        query = f"INSERT INTO ingresos(concepto, fecha, monto, donante_id, forma_pago_id) VALUES ('{concepto}', '{fecha}', '{monto}', '{donante_id}', '{forma_pago_id}')"
        resultado=self.setExecute(query)

        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_eco_ingre(self):
        query = f"SELECT * FROM ingresos ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def search_eco_ingre(self, desc):
        query = f"SELECT * FROM ingresos WHERE concepto = '{desc}'"
        resultado = self.getExecute(query)
        return resultado
    
    def update_eco_ingre(self, id, u_concepto, u_fecha, u_monto, u_donante_id, u_forma_pago_id):
        query = f"UPDATE ingresos SET concepto = '{u_concepto}', fecha = '{u_fecha}', monto = '{u_monto}', donante_id = '{u_donante_id}', forma_pago_id = '{u_forma_pago_id}' WHERE id = '{id}'"
        resultado = self.setExecute(query)
        print(resultado)
        if resultado != 0:
           respuesta = "No se actualizó"
        elif resultado == 0:
           respuesta = "Actualizado"
        else:
           respuesta = resultado
        return respuesta
    
    def delete_eco_ingre(self, id):
        query = f"DELETE FROM ingresos WHERE id = '{id}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta    
   
#TABLA EGRESOS

    def insert_eco_egre(self, concepto, fecha, monto, proveedor_id, forma_pago_id):
        query = f"INSERT INTO egresos(concepto, fecha, monto, proveedor_id, forma_pago_id) VALUES ('{concepto}', '{fecha}', '{monto}', '{proveedor_id}', '{forma_pago_id}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_eco_egre(self):
        query = f"SELECT * FROM egresos ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def search_eco_egre(self, desc):
        query = f"SELECT * FROM egresos WHERE concepto = '{desc}'"
        resultado = self.getExecute(query)
        return resultado
    
    def update_eco_egre(self, id, u_concepto, u_fecha, u_monto, u_proveedor_id, u_forma_pago_id):
        query = f"UPDATE egresos SET concepto = '{u_concepto}', fecha = '{u_fecha}', monto = '{u_monto}', proveedor_id = '{u_proveedor_id}', forma_pago_id = '{u_forma_pago_id}' WHERE id = '{id}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_eco_egre(self, id):
        query = f"DELETE FROM egresos WHERE id = '{id}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta     
    

# TABLA DE DONANTES

    def insert_donantes(self, nombre, direccion, telefono, correo):
        query = f"INSERT INTO donantes(nombre, direccion, telefono, correo_electronico) VALUES ('{nombre}', '{direccion}', '{telefono}', '{correo}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_donantes(self):
        query = f"SELECT * FROM donantes ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def update_donantes(self, id, u_nombre, u_direccion, u_telefono, u_correo):
        query = f"UPDATE donantes SET nombre = '{u_nombre}', direccion = '{u_direccion}', telefono = '{u_telefono}', correo_electronico = '{u_correo}' WHERE id = '{id}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_donantes(self, id):
        query = f"DELETE FROM donantes WHERE id = '{id}'"
        result=self.setExecute(query)
        print(result)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta     
    
#TABLA DE PROVEEDORES

    def insert_proveedores(self, nombre, direccion, telefono, correo):
        query = f"INSERT INTO proveedores(nombre, direccion, telefono, correo_electronico) VALUES ('{nombre}', '{direccion}', '{telefono}', '{correo}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_proveedores(self):
        query = f"SELECT * FROM proveedores ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def update_proveedores(self, id, u_nombre, u_direccion, u_telefono, u_correo):
        query = f"UPDATE proveedores SET nombre = '{u_nombre}', direccion = '{u_direccion}', telefono = '{u_telefono}', correo_electronico = '{u_correo}' WHERE id = '{id}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_proveedores(self, id):
        query = f"DELETE FROM proveedores WHERE id = '{id}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta     
    

#TABLA DE FORMAS DE PAGO

    def insert_formas_pago(self, nombre, descripcion):
        query = f"INSERT INTO formas_pago(nombre, descripcion) VALUES ('{nombre}', '{descripcion}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_formas_pago(self):
        query = f"SELECT * FROM formas_pago ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def update_formas_pago(self, id, u_nombre, u_descripcion):
        query = f"UPDATE formas_pago SET nombre = '{u_nombre}', descripcion = '{u_descripcion}' WHERE id = '{id}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_formas_pago(self, id):
        query = f"DELETE FROM formas_pago WHERE id = '{id}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta  
    
#TABLA DE EVENTOS
    
    def insert_eventos(self, nombre, fecha, ubicacion, descripcion, responsable_id):
        query = f"INSERT INTO eventos(nombre, fecha, ubicacion, descripcion, responsable_id) VALUES ('{nombre}', '{fecha}', '{ubicacion}', '{descripcion}', '{responsable_id}')"
        resultado=self.setExecute(query)
        if resultado!=0:
            respuesta="No se insertó"
        elif resultado==0:
            respuesta="Insertado"
        else:
            respuesta=resultado
        return respuesta
    
    def view_eventos(self):
        query = f"SELECT * FROM eventos ORDER BY id DESC"
        result =self.getExecute(query)
        return result
    
    def search_eventos(self, desc):
        query = f"SELECT * FROM eventos WHERE nombre = '{desc}'"
        resultado = self.getExecute(query)
        return resultado
    
    def update_eventos(self, id, u_nombre, u_fecha, u_ubicacion, u_descripcion, u_responsable_id):
        query = f"UPDATE eventos SET nombre = '{u_nombre}', fecha = '{u_fecha}', ubicacion = '{u_ubicacion}', descripcion = '{u_descripcion}', responsable_id = '{u_responsable_id}' WHERE id = '{id}'"
        resultado = self.setExecute(query)
        if resultado != 0:
         respuesta = "No se actualizó"
        elif resultado == 0:
            respuesta = "Actualizado"
        else:
            respuesta = resultado
        return respuesta
    
    def delete_eventos(self, id):
        query = f"DELETE FROM eventos WHERE id = '{id}'"
        result=self.setExecute(query)
        if result!=0:
            respuesta="No se elimino"
        elif result==0:
            respuesta="Eliminado"
        else:
            respuesta=result
        return respuesta     

   