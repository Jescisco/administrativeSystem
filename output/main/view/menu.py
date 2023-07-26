from customtkinter import *
from tkcalendar import DateEntry
import babel.numbers
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from controller.cont import *

class menu:
    def __init__(self, list):
        self.ControladorUsuarios=ControladorUsuarios()
        self.list =list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        #self.list = [self.pantalla, self.role]  no se pq escribi esto xd
        self.men()

    def validar_input(self, input_text):
        if not input_text:
            print("Este campo es requerido.")
            return False
        return True
    
    def men(self):
        self.pantalla.title("Nueva Acropolis")
        self.pantalla.geometry("800x600")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondo.jpg"), size=(800, 600))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        if self.role == 1:
            btn_regis_admin= CTkButton(self.pantalla, text="Opciones de admin", command=self.adminOptions, height=50, fg_color='#004C45')
            btn_regis_admin.place(x=25, y=500)

        btn_admin= CTkButton(self.pantalla, text="Gestion de Miembros", command=self.miembros, height=50, fg_color='#004C45')
        btn_admin.place(x=600, y=150)

        btn_eco= CTkButton(self.pantalla, text="Movimientos Economicos", command=self.eco, height=50, fg_color='#004C45')
        btn_eco.place(x=590, y=250)

        btn_eventos= CTkButton(self.pantalla, text="Eventos y Actividades", command=self.event, height=50, fg_color='#004C45')
        btn_eventos.place(x=600, y=350)

        btn_exit= CTkButton(self.pantalla, text="Salir", command=self.salir, height=25, width=20, fg_color='#004C45')
        btn_exit.place(x= 760, y= 575)
  
    def volver(self):
        self.limpiar_ventana()
        self.men()
    

    def salir(self):
        respuesta = messagebox.askquestion("Salir", "¿Estás seguro que quieres salir?")
        if respuesta == "yes":
            self.pantalla.destroy()

    def miembros(self):
        self.limpiar_ventana()
        Miembros(self.list)
        

    def eco(self):
        self.limpiar_ventana()
        Eco(self.list)
    
    def event(self):
        self.limpiar_ventana()
        Eventos(self.list)

    def limpiar_ventana(self):
        for widget in self.pantalla.winfo_children():
            widget.destroy()

    def adminOptions(self):
        self.limpiar_ventana()
        adminOptions(self.list)

class Miembros(menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.pantalla.geometry("800x630")
        self.ControladorUsuarios=ControladorUsuarios()
        self.pantalla.title("Miembros")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondomiem.jpg"), size=(800, 630))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5", "#6"), show="headings")

        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=40, anchor=CENTER)
        self.grid.column("#3",width=70, anchor=CENTER)
        self.grid.column("#4",width=60, anchor=CENTER)
        self.grid.column("#5",width=60, anchor=CENTER)
        self.grid.column("#6",width=60, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="id", anchor=CENTER)
        self.grid.heading("#2", text="Cedula", anchor=CENTER)
        self.grid.heading("#3", text="Nombre", anchor=CENTER)
        self.grid.heading("#4", text="Telefono", anchor=CENTER)
        self.grid.heading("#5", text="Genero", anchor=CENTER)
        self.grid.heading("#6", text="Disponibilidad", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.mostrar_voluntarios(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))
        
        self.grid.place(x=100,y=110,width=600,height=400)

        back_btn = CTkButton(self.pantalla, text="Volver al menu", command=self.volver, fg_color='#004C45')
        back_btn.place(x=340, y=70)

        self.buscar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.buscar.place(x=25, y=530)

        search_btn = CTkButton(self.pantalla, text="Buscar", command=self.search_miembros, fg_color='#004C45', width=15)
        search_btn.place(x=70, y=560)

        if not self.role == 3:

            back_btn = CTkButton(self.pantalla, text="Registrar", command=self.miem_regis, fg_color='#004C45')
            back_btn.place(x=423, y=520)

            back_btn = CTkButton(self.pantalla, text="Editar", command=self.Editar_miembros, fg_color='#004C45')
            back_btn.place(x=243, y=520)

            btn_eliminar =  CTkButton(self.pantalla, text="Eliminar", command=self.eliminarMiembros, fg_color='#FF2F2F')
            btn_eliminar.place(x=333, y=560)

    def search_miembros(self):
        if self.buscar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.ControladorUsuarios.buscar_miembros(self.buscar.get())!=[]:
                data=self.ControladorUsuarios.buscar_miembros(self.buscar.get())
                sano= self.grid.get_children()

                for element in sano:
                    self.grid.delete(element)
                
                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))

    def Editar_miembros(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("650x450")
            self.toplevel.title("Editar miembros")
            self.toplevel.resizable(width=False, height=False)

            img = CTkImage(light_image=Image.open("view/img/fondoedit.jpg"), size=(650, 450))
            lbl_img = CTkLabel(self.toplevel, image=img, text="")
            lbl_img.place(x=0, y=0)

            self.txtCed = CTkEntry(self.toplevel, placeholder_text="Cedula")
            self.txtCed.place(x=250, y=130)
            self.txtnom = CTkEntry(self.toplevel, placeholder_text="Nombre")
            self.txtnom.place(x=250, y=180)
            self.txtTlf = CTkEntry(self.toplevel, placeholder_text="Telefono")
            self.txtTlf.place(x=250, y=230)
            self.txtGen = CTkComboBox(self.toplevel, values=["Masculino", "Femenino", "Otro"], state="readonly")
            self.txtGen.set("Genero...")
            self.txtGen.place(x=250, y=280)
            self.txtDisp = CTkComboBox(self.toplevel, values=["Disponible"], state="readonly")    
            self.txtDisp.set("Disponibilidad...")                                                                                                                                                                                                                                                            
            self.txtDisp.place(x=250, y=330)

            btn_nuevo =  CTkButton(self.toplevel, text="Editar", command=self.editmiembros, fg_color='#004C45', height=40)
            btn_nuevo.place(x=250, y=380)

            back_btn = CTkButton(self.toplevel, text="Volver a la lista", command=self.vol_miem, fg_color='#004C45')
            back_btn.place(x=250, y=80)
    def editmiembros(self):
        if self.txtCed.get() == "" or self.txtnom.get() == "" or self.txtTlf.get() == "" or self.txtGen.get() == "" or self.txtDisp.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.editar_voluntario(self.sisas, self.txtCed.get(), self.txtnom.get(), self.txtTlf.get(), self.txtGen.get(), self.txtDisp.get()):
                messagebox.showerror(message="Error al Actualizar el Ingreso", title="Error")
                self.pantalla.deiconify()
                self.toplevel.destroy()
            else:
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Miembros(self.list)
                self.toplevel.destroy()

    def eliminarMiembros(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.ControladorUsuarios.eliminar_voluntario(self.sisas):
                    messagebox.showerror(message="Error al eliminar el miembro", title="Error")
                else:
                    messagebox.showinfo(message="Eliminado con exito")
                    menu(self.list)

    def volver(self):
        self.limpiar_ventana()
        self.men()

    def fActualizar(self):
        pass
      
    def vol_miem(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()

    def miem_regis(self):
        self.limpiar_ventana()
        Registro_miembros(self.list)
  
class Eco(menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.pantalla.geometry("400x250")
        self.ControladorUsuarios=ControladorUsuarios()
        self.pantalla.title("Movimientos Economicos")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondoeco.jpg"), size=(400, 250))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        self.back_btn = CTkButton(self.pantalla, text="Ingresos", command=self.ingresos_eco, fg_color='#004C45')
        self.back_btn.place(x=40, y=90)

        self.back_btn = CTkButton(self.pantalla, text="Egresos", command=self.egresos_eco, fg_color='#004C45')
        self.back_btn.place(x=220, y=90)
        
        self.back_btn = CTkButton(self.pantalla, text="Volver al menu", command=self.volver, fg_color='#004C45')
        self.back_btn.place(x=125, y=170)

    def ingresos_eco(self):
        self.limpiar_ventana()
        Ingresos_eco(self.list)    

    def egresos_eco(self):
        self.limpiar_ventana()
        Egresos_eco(self.list)    

class Eventos(menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.pantalla.geometry("800x630")
        self.ControladorUsuarios=ControladorUsuarios()
        self.pantalla.title("Eventos")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondoeve.jpg"), size=(800, 630))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5", "#6"), show="headings")

        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=40, anchor=CENTER)
        self.grid.column("#3",width=70, anchor=CENTER)
        self.grid.column("#4",width=60, anchor=CENTER)
        self.grid.column("#5",width=60, anchor=CENTER)
        self.grid.column("#6",width=60, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="id", anchor=CENTER)
        self.grid.heading("#2", text="Nombre", anchor=CENTER)
        self.grid.heading("#3", text="Fecha", anchor=CENTER)
        self.grid.heading("#4", text="Ubicacion", anchor=CENTER)
        self.grid.heading("#5", text="Descripcion", anchor=CENTER)
        self.grid.heading("#6", text="Responsabilidad", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.mostrar_eventos(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))
        
        self.grid.place(x=100,y=110,width=600,height=400)

        back_btn = CTkButton(self.pantalla, text="Volver al menu", command=self.volver, fg_color='#004C45')
        back_btn.place(x=340, y=70) 

        self.buscar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.buscar.place(x=25, y=530)

        search_btn = CTkButton(self.pantalla, text="Buscar", command=self.search_eventos, fg_color='#004C45', width=15)
        search_btn.place(x=70, y=560)

        if not self.role == 3:

            back_btn = CTkButton(self.pantalla, text="Registrar", command=self.actividad_regis, fg_color='#004C45')
            back_btn.place(x=423, y=520)

            back_btn = CTkButton(self.pantalla, text="Editar", command=self.Editar_eventos, fg_color='#004C45')
            back_btn.place(x=243, y=520)

            btn_eliminar =  CTkButton(self.pantalla, text="Eliminar", command=self.eliminarEventos, fg_color='#FF2F2F')
            btn_eliminar.place(x=333, y=560)

    def search_eventos(self):
        if self.buscar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.ControladorUsuarios.buscar_eventos(self.buscar.get())!=[]:
                data=self.ControladorUsuarios.buscar_eventos(self.buscar.get())
                sano= self.grid.get_children()

                for element in sano:
                    self.grid.delete(element)
                
                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))

    def Editar_eventos(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("650x450")
            self.toplevel.title("Editar miembros")
            self.toplevel.resizable(width=False, height=False)

            img = CTkImage(light_image=Image.open("view/img/fondoedit.jpg"), size=(650, 450))
            lbl_img = CTkLabel(self.toplevel, image=img, text="")
            lbl_img.place(x=0, y=0)

            self.txtnom = CTkEntry(self.toplevel, placeholder_text="Nombre")
            self.txtnom.place(x=250, y=130)
            self.txtfech= DateEntry(self.toplevel, width=20)
            self.txtfech.place(x=250, y=180)
            self.txtubi = CTkEntry(self.toplevel, placeholder_text="Ubicacion")
            self.txtubi.place(x=250, y=230)
            self.txtDes = CTkEntry(self.toplevel, placeholder_text="Descripcion")
            self.txtDes.place(x=250, y=280)
            self.txtResp = CTkComboBox(self.toplevel, values=self.llenar_combo_responsable(), state="readonly")                                                                                                                                                                                                                                                            
            self.txtResp.place(x=250, y=330)

            btn_nuevo =  CTkButton(self.toplevel, text="Editar", command=self.editeventos, fg_color='#004C45', height=40)
            btn_nuevo.place(x=250, y=380)

            back_btn = CTkButton(self.toplevel, text="Volver a la lista", command=self.vol_miem, fg_color='#004C45')
            back_btn.place(x=250, y=80)

    def editeventos(self):
        if self.txtnom.get() == "" or self.txtfech.get_date() == "" or self.txtubi.get() == "" or self.txtDes.get() == "" or self.txtResp.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.actualizar_eventos(self.sisas, self.txtnom.get(), self.txtfech.get_date(), self.txtubi.get(), self.txtDes.get(), self.txtResp.get()):
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.toplevel.destroy()
            else:
                messagebox.showerror(message="Error al Actualizar el Ingreso", title="Error")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Eventos(self.list)
                self.toplevel.destroy()

    def eliminarEventos(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.ControladorUsuarios.eliminar_eventos(self.sisas):
                    messagebox.showinfo(message="Eliminado con exito")
                    menu(self.list)
                else:
                    messagebox.showerror(message="Error al eliminar el miembro", title="Error")
    
    def llenar_combo_responsable(self):
        valores = self.ControladorUsuarios.mostrar_voluntarios()
        valores_combo = [str(result[0])+'-'+result[2] for result in valores]
        return valores_combo 

    def volver(self):
        self.limpiar_ventana()
        self.men()

    def fActualizar(self):
        pass
      
    def vol_miem(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()

    def actividad_regis(self):
        self.limpiar_ventana()
        Registro_actividades(self.list)

class Registro_actividades(Eventos):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Registro de miembros")
        self.pantalla.geometry("650x450")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondora.jpg"), size=(650, 450))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        self.txtnom = CTkEntry(self.pantalla, placeholder_text="Nombre")
        self.txtnom.place(x=250, y=130)
        self.txtfech= DateEntry(self.pantalla, width=20)
        self.txtfech.place(x=250, y=180)
        self.txtubi = CTkEntry(self.pantalla, placeholder_text="Ubicacion")
        self.txtubi.place(x=250, y=230)
        self.txtDes = CTkEntry(self.pantalla, placeholder_text="Descripcion")
        self.txtDes.place(x=250, y=280)
        self.txtResp = CTkComboBox(self.pantalla, values=self.llenar_combo_responsable(), state="readonly")                                                                                                                                                                                                                                                            
        self.txtResp.place(x=250, y=330)

        btn_nuevo =  CTkButton(self.pantalla, text="Nuevo", command=self.fNuevo, fg_color='#004C45', height=40)
        btn_nuevo.place(x=250, y=380)

        back_btn = CTkButton(self.pantalla, text="Volver a la lista", command=self.vol_eco, fg_color='#004C45')
        back_btn.place(x=250, y=80)

    def llenar_combo_responsable(self):
        valores = self.ControladorUsuarios.mostrar_voluntarios()
        valores_combo = [str(result[0])+'-'+result[2] for result in valores]
        return valores_combo 

    def vol_eco(self):
        self.limpiar_ventana()
        Eventos(self.list)
 
    def fNuevo(self):
        if self.txtnom.get() == "" or self.txtfech.get_date() == "" or self.txtubi.get() == "" or self.txtDes.get() == "" or self.txtResp.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.insertar_eventos(self.txtnom.get(), self.txtfech.get_date(), self.txtubi.get(), self.txtDes.get(), self.txtResp.get()):
                self.limpiar_ventana()
                menu(self.list)
            else:
                messagebox.showerror("Error", "No se pudo registrar el miembro")

class adminOptions(menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()
        
        self.pantalla.title("Administracion")
        self.pantalla.geometry("800x600")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondoadmin.jpg"), size=(800, 600))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        frame = CTkFrame(self.pantalla, width=250, height=400)
        frame.place(x=30, y=150)

        back_btn = CTkButton(self.pantalla, text="Volver al menu", command=self.volver, fg_color='#004C45')
        back_btn.place(x=380, y=80)

        title = CTkLabel(frame, text="Registrar Usuarios")
        self.entryUser = CTkEntry(frame, placeholder_text="Usuario")
        self.entryPass = CTkEntry(frame, placeholder_text="Contraseña", show="*")
        self.entryLevel = CTkComboBox(frame, values=["1", "2", "3"], state="readonly")
        self.entryLevel.set("Nivel de usuario...")
        btnSend = CTkButton(frame, text="Registrar", fg_color="#004C45", height=50, command=self.hagale)
        btnEdit = CTkButton(frame, text="Editar", fg_color="#004C45", height=50, command=self.editarsapo)
        btnDelete = CTkButton(frame, text="Eliminar", fg_color="#004C45", height=50, command=self.eliminarsapo)

        CTkLabel(frame, text="").pack()
        title.pack()
        self.entryUser.pack(pady=5)
        self.entryPass.pack(pady=5)
        self.entryLevel.pack(pady=5)
        CTkLabel(frame, text="").pack()
        btnSend.pack()
        btnEdit.pack(pady=10)
        btnDelete.pack()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])

        self.grid = ttk.Treeview( columns=("#1","#2","#3"), show="headings")
        self.grid.place(x=250, y=150, width=450, height=400)

        self.grid.column("#0", width=0, anchor=CENTER)
        self.grid.column("#1",width=20, anchor=CENTER)
        self.grid.column("#2",width=40, anchor=CENTER)
        self.grid.column("#3",width=70, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="Usuario", anchor=CENTER)
        self.grid.heading("#2", text="Contraseña", anchor=CENTER)
        self.grid.heading("#3", text="Nivel del usuario", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.viewLoginUsers(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[1], loca[2], loca[3]))
            #Self.treeview.selection(self.treeview.item()["text"])
    
    def hagale(self):
        if self.entryPass.get() == "" or self.entryUser.get() == "" or self.entryLevel.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.newUser(self.entryUser.get(), self.entryPass.get(), self.entryLevel.get()):
                messagebox.showinfo(message="Registro con exito")
                self.limpiar_ventana()
                menu(self.list)
            else:
                messagebox.showerror(message="Error al regisrar el usuario")
    
    def eliminarsapo(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.ControladorUsuarios.eliminarAdmin(self.sisas):
                    messagebox.showerror(message="Error al eliminar el miembro", title="Error")
                else:
                    messagebox.showinfo(message="Eliminado con exito")
                    menu(self.list)

    def editarsapo(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas=="":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.tplv = CTkToplevel(self.pantalla)
            self.tplv.geometry("200x300")
            self.tplv.title("Editar usuarios")
            self.tplv.resizable(width=False, height=False)

            self.entryUser = CTkEntry(self.tplv, placeholder_text="Usuario")
            self.entryPass = CTkEntry(self.tplv, placeholder_text="Contraseña", show="*")
            self.entryLevel = CTkComboBox(self.tplv, values=["1", "2", "3"], state="readonly")
            self.entryLevel.set("Nivel de usuario...")

            CTkLabel(self.tplv, text="").pack()
            self.entryUser.pack(pady=5)
            self.entryPass.pack(pady=5)
            self.entryLevel.pack(pady=5)
            CTkLabel(self.tplv, text="").pack()

            btnSend= CTkButton(self.tplv, text="Actualizar", command=self.sobelo)
            btnSend.pack(pady=5)

    def sobelo(self):
        if self.entryPass.get() == "" or self.entryUser.get() == "" or self.entryLevel.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.editarAdmin(self.sisas, self.entryUser.get(), self.entryPass.get(), self.entryLevel.get()):
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                menu(self.list)
            else:
                messagebox.showerror(message="Error al actualizar", title="Error")
            
    def fCancelar(self):
        self.toplevel.destroy()
        self.pantalla.deiconify()


#FUNCIONES FUERA DEL MENU PRINCIPAL        
            
class Registro_miembros(Miembros):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Registro de miembros")
        self.pantalla.geometry("650x450")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondora.jpg"), size=(650, 450))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        self.txtCed = CTkEntry(self.pantalla, placeholder_text="Cedula")
        self.txtCed.place(x=250, y=130)
        self.txtnom = CTkEntry(self.pantalla, placeholder_text="Nombre")
        self.txtnom.place(x=250, y=180)
        self.txtTlf = CTkEntry(self.pantalla, placeholder_text="Telefono")
        self.txtTlf.place(x=250, y=230)
        self.txtGen = CTkComboBox(self.pantalla, values=["Masculino", "Femenino", "Otro"], state="readonly")
        self.txtGen.set("Genero...")
        self.txtGen.place(x=250, y=280)
        self.txtDisp = CTkComboBox(self.pantalla, values=["Disponible"], state="readonly")       
        self.txtDisp.set("Disponibilidad...")                                                                                                                                                                                                                                                          
        self.txtDisp.place(x=250, y=330)

        btn_nuevo =  CTkButton(self.pantalla, text="Nuevo", command=self.fNuevo, fg_color='#004C45', height=40)
        btn_nuevo.place(x=250, y=380)

        back_btn = CTkButton(self.pantalla, text="Volver a la lista", command=self.vol_class_miem, fg_color='#004C45')
        back_btn.place(x=250, y=80)
    
    def vol_class_miem(self):
        self.limpiar_ventana()
        Miembros(self.list)
 
    def fNuevo(self):
        if self.txtCed.get() == "" or self.txtnom.get() == "" or self.txtTlf.get() == "" or self.txtGen.get() == "" or self.txtDisp.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.nuevo_voluntario(self.txtCed.get(), self.txtnom.get(), self.txtTlf.get(), self.txtGen.get(), self.txtDisp.get()):
                self.limpiar_ventana()
                menu(self.list)
            else:
                messagebox.showerror("Error", "No se pudo registrar el miembro")

#INGRESOS TABLA

class Ingresos_eco(Eco, menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Ingresos")
        self.pantalla.geometry("650x506")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondoingre.jpg"), size=(650, 506))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])        

        
        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5", "#6"), show="headings")

        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=50, anchor=CENTER)
        self.grid.column("#3",width=30, anchor=CENTER)
        self.grid.column("#4",width=40, anchor=CENTER)
        self.grid.column("#5",width=50, anchor=CENTER)
        self.grid.column("#6",width=70, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="id", anchor=CENTER)
        self.grid.heading("#2", text="Concepto", anchor=CENTER)
        self.grid.heading("#3", text="Fecha", anchor=CENTER)
        self.grid.heading("#4", text="Monto", anchor=CENTER)
        self.grid.heading("#5", text="Donante", anchor=CENTER)
        self.grid.heading("#6", text="Forma de pago", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.mostrar_eco_ingre(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))
        
        self.grid.place(x=50,y=90,width=550,height=300)

        back_btn = CTkButton(self.pantalla, text="Volver", command=self.volveratras, fg_color='#004C45')
        back_btn.place(x=490, y=430)

        self.buscar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.buscar.place(x=220, y=430)

        search_btn = CTkButton(self.pantalla, text="Buscar",command=self.search_ingresos, fg_color='#004C45', width=15)
        search_btn.place(x=370, y=430)

        if not self.role == 3:

            back_btn = CTkButton(self.pantalla, text="Registrar Ingreso", command=self.regis_eco_ingre, fg_color='#004C45')
            back_btn.place(x=245, y=390)

            back_btn = CTkButton(self.pantalla, text="Editar", command=self.Editar_ingre, fg_color='#004C45')
            back_btn.place(x=90, y=390)

            btn_eliminar =  CTkButton(self.pantalla, text="Eliminar", command=self.eliminarIngresos, fg_color='#FF2F2F')
            btn_eliminar.place(x=400, y=390)


            btn_eventos= CTkButton(self.pantalla, text="Registra Donantes", command=self.donan, fg_color='#004C45')
            btn_eventos.place(x=20, y=430)
        
    def search_ingresos(self):
        if self.buscar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.ControladorUsuarios.buscador_ingresos(self.buscar.get())!=[]:
                data=self.ControladorUsuarios.buscador_ingresos(self.buscar.get())
                sano= self.grid.get_children()

                for element in sano:
                    self.grid.delete(element)
                
                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))

    def Editar_ingre(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("650x450")
            self.toplevel.title("Editar Ingreso")
            self.toplevel.resizable(width=False, height=False)

            img = CTkImage(light_image=Image.open("view/img/fondoedit.jpg"), size=(650, 450))
            lbl_img = CTkLabel(self.toplevel, image=img, text="")
            lbl_img.place(x=0, y=0)

            self.txtconcep = CTkEntry(self.toplevel, placeholder_text="Concepto")
            self.txtconcep.place(x=250, y=130)
            self.txtfech= DateEntry(self.toplevel, width=20)
            self.txtfech.place(x=250, y=180)
            self.txtmonto = CTkEntry(self.toplevel, placeholder_text="Monto")
            self.txtmonto.place(x=250, y=230)
            self.txtdonan = CTkComboBox(self.toplevel, values=self.llenar_combo_donante(), state="readonly")      
            self.txtdonan.set("Donantes...")
            self.txtdonan.place(x=250, y=280)
            self.txtfpago = CTkComboBox(self.toplevel, values=self.llenar_combo_fpago(), state="readonly") 
            self.txtfpago.set("Metodos de pago...")
            self.txtfpago.place(x=250, y=330)

            btn_nuevo =  CTkButton(self.toplevel, text="Editar", command=self.editingre, fg_color='#004C45', height=40)
            btn_nuevo.place(x=250, y=380)

            back_btn = CTkButton(self.toplevel, text="Volver a la lista", command=self.vol_ingre, fg_color='#004C45')
            back_btn.place(x=250, y=80)

    def editingre(self):
        if self.sisas == "" or self.txtconcep.get() == "" or self.txtfech.get_date() == "" or self.txtmonto.get() == "" or self.txtdonan.get() == "" or self.txtfpago.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.actualizar_eco_ingre(self.sisas, self.txtconcep.get(), self.txtfech.get_date(), self.txtmonto.get(), self.txtdonan.get(), self.txtfpago.get()):
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Ingresos_eco(self.list)
                self.toplevel.destroy()
            else:
                messagebox.showerror(message="Error al Actualizar el Ingreso", title="Error")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Ingresos_eco(self.list)
                self.toplevel.destroy()

    def eliminarIngresos(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.ControladorUsuarios.eliminar_eco_ingre(self.sisas):
                    messagebox.showinfo(message="Eliminado con exito")
                    menu(self.list)
                else:
                    messagebox.showerror(message="Error al eliminar el miembro", title="Error")
    
    def llenar_combo_donante(self):
        valores = self.ControladorUsuarios.mostar_donantes()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 
    
    def llenar_combo_fpago(self):
        valores = self.ControladorUsuarios.mostar_formas_pago()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 

    def volver(self):
        self.limpiar_ventana()
        self.men()

    def volveratras(self):
        self.limpiar_ventana()
        Eco(self.list)    

    def vol_ingre(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()     

    def donan(self):
        self.limpiar_ventana()
        Donantes(self.list)  

    def regis_eco_ingre(self):
        self.limpiar_ventana()
        registrar_eco_ingre(self.list)        

#REGISTRAR INGRESOS

class registrar_eco_ingre(Eco, menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Registro de ingresos")
        self.pantalla.geometry("650x450")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondora2.jpg"), size=(650, 450))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        self.txtconcep = CTkEntry(self.pantalla, placeholder_text="Concepto")
        self.txtconcep.place(x=250, y=80)
        self.txtfech= DateEntry(self.pantalla, width=20)
        self.txtfech.place(x=250, y=130)
        self.txtmonto = CTkEntry(self.pantalla, placeholder_text="Monto")
        self.txtmonto.place(x=250, y=180)
        self.txtdonan = CTkComboBox(self.pantalla, values=self.llenar_combo_donante(), state="readonly")  
        self.txtdonan.set("Donantes...")                                                                                                                                                                                                                                                                 
        self.txtdonan.place(x=250, y=230)
        self.txtfpago = CTkComboBox(self.pantalla, values=self.llenar_combo_fpago(), state="readonly")  
        self.txtfpago.set("Metodos de pago...")                                                                                                                                                                                                                                                          
        self.txtfpago.place(x=250, y=280)

        btn_nuevo = CTkButton(self.pantalla, text="Ingresar", command=self.nuevo_ingreso, fg_color='#004C45', height=40)
        btn_nuevo.place(x=250, y=330)

        back_btn = CTkButton(self.pantalla, text="Volver a la lista", command=self.volveratras, fg_color='#004C45')
        back_btn.place(x=250, y=380)

    def llenar_combo_donante(self):
        valores = self.ControladorUsuarios.mostar_donantes()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 
    
    def llenar_combo_fpago(self):
        valores = self.ControladorUsuarios.mostar_formas_pago()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 

    def nuevo_ingreso(self):
        if self.txtconcep.get()== "" or self.txtfech.get_date()== "" or self.txtmonto.get()== "" or self.txtdonan.get()== "" or self.txtfpago.get()== "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.insertar_eco_ingre(self.txtconcep.get(), self.txtfech.get_date(), self.txtmonto.get(), self.txtdonan.get(), self.txtfpago.get()):
                self.limpiar_ventana()
                Ingresos_eco(self.list)
            else:
                messagebox.showerror("Error", "No se pudo registrar el Ingreso")

    def volveratras(self):
        self.limpiar_ventana()
        Eco(self.list)         

class Egresos_eco(Eco, menu):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Egresos")
        self.pantalla.geometry("650x506")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondoegre.jpg"), size=(650, 506))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])        

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5", "#6"), show="headings")

        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=50, anchor=CENTER)
        self.grid.column("#3",width=30, anchor=CENTER)
        self.grid.column("#4",width=40, anchor=CENTER)
        self.grid.column("#5",width=50, anchor=CENTER)
        self.grid.column("#6",width=70, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="id", anchor=CENTER)
        self.grid.heading("#2", text="Concepto", anchor=CENTER)
        self.grid.heading("#3", text="Fecha", anchor=CENTER)
        self.grid.heading("#4", text="Monto", anchor=CENTER)
        self.grid.heading("#5", text="Proveedor", anchor=CENTER)
        self.grid.heading("#6", text="Forma de pago", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.mostrar_eco_egre(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))
        
        self.grid.place(x=50,y=90,width=550,height=300)

        back_btn = CTkButton(self.pantalla, text="Volver", command=self.volveratras, fg_color='#004C45')
        back_btn.place(x=490, y=430)

        self.buscar = CTkEntry(self.pantalla, placeholder_text="Buscar")
        self.buscar.place(x=220, y=430)

        search_btn = CTkButton(self.pantalla, text="Buscar",command=self.search_egresos, fg_color='#004C45', width=15)
        search_btn.place(x=370, y=430)

        if not self.role == 3:

            back_btn = CTkButton(self.pantalla, text="Registrar Egreso", command=self.regis_eco_egre, fg_color='#004C45')
            back_btn.place(x=245, y=390)

            back_btn = CTkButton(self.pantalla, text="Editar", command=self.Editar_egre, fg_color='#004C45')
            back_btn.place(x=90, y=390)

            btn_eliminar =  CTkButton(self.pantalla, text="Eliminar", command=self.eliminarEgresos, fg_color='#FF2F2F')
            btn_eliminar.place(x=400, y=390)


            btn_eventos= CTkButton(self.pantalla, text="Registra Proveedores", command=self.provee, fg_color='#004C45')
            btn_eventos.place(x=20, y=430)

    def search_egresos(self):
        if self.buscar.get() == "":
            messagebox.showerror(message=f"Campo vacio, Ingrese un dato", title="Error")
        else:
            if self.ControladorUsuarios.buscador_egresos(self.buscar.get())!=[]:
                data=self.ControladorUsuarios.buscador_egresos(self.buscar.get())
                sano= self.grid.get_children()

                for element in sano:
                    self.grid.delete(element)
                
                i=-1
                for loca in data:
                    self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4], loca[5]))

    def Editar_egre(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("650x450")
            self.toplevel.title("Editar Ingreso")
            self.toplevel.resizable(width=False, height=False)

            img = CTkImage(light_image=Image.open("view/img/fondoedit.jpg"), size=(650, 450))
            lbl_img = CTkLabel(self.toplevel, image=img, text="")
            lbl_img.place(x=0, y=0)

            self.txtconcep = CTkEntry(self.toplevel, placeholder_text="Concepto")
            self.txtconcep.place(x=250, y=130)
            self.txtfech= DateEntry(self.toplevel, width=20)
            self.txtfech.place(x=250, y=180)
            self.txtmonto = CTkEntry(self.toplevel, placeholder_text="Monto")
            self.txtmonto.place(x=250, y=230)
            self.txtprovee = CTkComboBox(self.toplevel, values=self.llenar_combo_provee(), state="readonly")
            self.txtprovee.set("Proveedor...")   
            self.txtprovee.place(x=250, y=280)
            self.txtfpago = CTkComboBox(self.toplevel, values=self.llenar_combo_fpago(), state="readonly")           
            self.txtfpago.set("Metodos de pago...")                                                                                                                                                                                                                                                             
            self.txtfpago.place(x=250, y=330)

            btn_nuevo =  CTkButton(self.toplevel, text="Editar", command=self.editegre, fg_color='#004C45', height=40)
            btn_nuevo.place(x=250, y=380)

            back_btn = CTkButton(self.toplevel, text="Volver a la lista", command=self.vol_egre, fg_color='#004C45')
            back_btn.place(x=250, y=80)

    def editegre(self):
        if self.sisas == "" or self.txtconcep.get() == "" or self.txtfech.get_date() == "" or self.txtmonto.get() == "" or self.txtprovee.get() == "" or self.txtfpago.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.actualizar_eco_egre(self.sisas, self.txtconcep.get(), self.txtfech.get_date(), self.txtmonto.get(), self.txtprovee.get(), self.txtfpago.get()):
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.toplevel.destroy()
            else:
                messagebox.showerror(message="Error al Actualizar el Ingreso", title="Error")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Egresos_eco(self.list)
                self.toplevel.destroy()

    def eliminarEgresos(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Debe seleccionar un campo", title="Error")
        else:
            respuesta = messagebox.askquestion("Eliminar", "¿Estás seguro que deseas eliminar este campo?")
            if respuesta == "yes":
                if self.ControladorUsuarios.eliminar_eco_egre(self.sisas):
                    messagebox.showinfo(message="Eliminado con exito")
                    menu(self.list)
                else:
                    messagebox.showerror(message="Error al eliminar el miembro", title="Error")
    
    def llenar_combo_provee(self):
        valores = self.ControladorUsuarios.mostar_proveedores()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 
    
    def llenar_combo_fpago(self):
        valores = self.ControladorUsuarios.mostar_formas_pago()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 

    def volveratras(self):
        self.limpiar_ventana()
        Eco(self.list)
     
    def vol_egre(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()     

    def provee(self):
        self.limpiar_ventana()
        Proveedores(self.list) 

    def regis_eco_egre(self):
        self.limpiar_ventana()
        registrar_eco_egre(self.list)

#REGISTRAR EGRESOS

class registrar_eco_egre(Egresos_eco, Eco):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Registro de egresos")
        self.pantalla.geometry("650x450")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondora2.jpg"), size=(650, 450))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)
        
        self.txtconcep = CTkEntry(self.pantalla, placeholder_text="Concepto")
        self.txtconcep.place(x=250, y=80)
        self.txtfech= DateEntry(self.pantalla, width=20)
        self.txtfech.place(x=250, y=130)
        self.txtmonto = CTkEntry(self.pantalla, placeholder_text="Monto")
        self.txtmonto.place(x=250, y=180)
        self.txtprovee = CTkComboBox(self.pantalla, values=self.llenar_combo_provee(), state="readonly")    
        self.txtprovee.set("Proveedor...")                                                                                                                                                                                                                                                        
        self.txtprovee.place(x=250, y=230)
        self.txtfpago = CTkComboBox(self.pantalla, values=self.llenar_combo_fpago(), state="readonly")  
        self.txtfpago.set("Metodos de pago...")
        self.txtfpago.place(x=250, y=280)

        btn_nuevo = CTkButton(self.pantalla, text="Ingresar", command=self.nuevo_egreso, fg_color='#004C45', height=40)
        btn_nuevo.place(x=250, y=330)

        back_btn = CTkButton(self.pantalla, text="Volver a la lista", command=self.volveratras, fg_color='#004C45')
        back_btn.place(x=250, y=380)

    def llenar_combo_provee(self):
        valores = self.ControladorUsuarios.mostar_proveedores()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 
    
    def llenar_combo_fpago(self):
        valores = self.ControladorUsuarios.mostar_formas_pago()
        valores_combo = [str(result[0])+'-'+result[1] for result in valores]
        return valores_combo 
    
    def volveratras(self):
        self.limpiar_ventana()
        Eco(self.list)

    def nuevo_egreso(self):
        if self.txtconcep.get() == "" or self.txtfech.get_date() == "" or self.txtmonto.get() == "" or self.txtprovee.get() == "" or self.txtfpago.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.insertar_eco_egre(self.txtconcep.get(), self.txtfech.get_date(), self.txtmonto.get(), self.txtprovee.get(), self.txtfpago.get()):
                self.limpiar_ventana()
                Egresos_eco(self.list)
            else:
                messagebox.showerror("Error", "No se pudo registrar el Ingreso")


#DONANTES

class Donantes(Ingresos_eco, Eco):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios = ControladorUsuarios()
        self.pantalla.geometry("800x600")

        img = CTkImage(light_image=Image.open("view/img/fondodona.jpg"), size=(800, 600))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5"), show="headings")

        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=40, anchor=CENTER)
        self.grid.column("#3",width=70, anchor=CENTER)
        self.grid.column("#4",width=60, anchor=CENTER)
        self.grid.column("#5",width=60, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="id", anchor=CENTER)
        self.grid.heading("#2", text="Nombre", anchor=CENTER)
        self.grid.heading("#3", text="Direccion", anchor=CENTER)
        self.grid.heading("#4", text="Telefono", anchor=CENTER)
        self.grid.heading("#5", text="Correo", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.mostar_donantes(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4]))

        self.grid.place(x=100,y=110,width=600,height=400)


        back_btn = CTkButton(self.pantalla, text="Volver al menu", command=self.volveratras, fg_color='#004C45')
        back_btn.place(x=340, y=70) 

        back_btn = CTkButton(self.pantalla, text="Registrar",command=self.regis_dona, fg_color='#004C45')
        back_btn.place(x=423, y=520)

        back_btn = CTkButton(self.pantalla, text="Editar",command=self.Editar_donantes, fg_color='#004C45')
        back_btn.place(x=243, y=520)

    def Editar_donantes(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("650x450")
            self.toplevel.title("Editar Donantes")
            self.toplevel.resizable(width=False, height=False)

            img = CTkImage(light_image=Image.open("view/img/fondoedit.jpg"), size=(650, 450))
            lbl_img = CTkLabel(self.toplevel, image=img, text="")
            lbl_img.place(x=0, y=0)

            self.txtnom = CTkEntry(self.toplevel, placeholder_text="Nombre")
            self.txtnom.place(x=250, y=130)
            self.txtdir = CTkEntry(self.toplevel, placeholder_text="Direccion")
            self.txtdir.place(x=250, y=180)
            self.txtTlf = CTkEntry(self.toplevel, placeholder_text="Telefono")
            self.txtTlf.place(x=250, y=230)
            self.txtcor = CTkEntry(self.toplevel, placeholder_text="Correo")
            self.txtcor.place(x=250, y=280)

            btn_nuevo =  CTkButton(self.toplevel, text="Editar", command=self.editdona, fg_color='#004C45', height=40)
            btn_nuevo.place(x=250, y=320)

            back_btn = CTkButton(self.toplevel, text="Volver a la lista", command=self.volveratrasok, fg_color='#004C45')
            back_btn.place(x=250, y=80)

    def volveratrasok(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()

    def editdona(self):
        if self.txtnom.get() == "" or self.txtdir.get() == "" or self.txtTlf.get() == "" or self.txtcor.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.actualizar_donantes(self.sisas, self.txtnom.get(), self.txtdir.get(), self.txtTlf.get(), self.txtcor.get()):
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Ingresos_eco(self.list)
                self.toplevel.destroy() 
            else:
                messagebox.showerror(message="Error al Actualizar el Ingreso", title="Error")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Egresos_eco(self.list)
                self.toplevel.destroy()         

    def volveratras(self):
        self.limpiar_ventana()
        Eco(self.list)        

    def regis_dona(self):
        self.limpiar_ventana()
        Registro_donantes(self.list)

class Registro_donantes(Donantes):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Registro de miembros")
        self.pantalla.geometry("650x450")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondora.jpg"), size=(650, 450))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        self.txtnom = CTkEntry(self.pantalla, placeholder_text="Nombre")
        self.txtnom.place(x=250, y=130)
        self.txtdir = CTkEntry(self.pantalla, placeholder_text="Direccion")
        self.txtdir.place(x=250, y=180)
        self.txtTlf = CTkEntry(self.pantalla, placeholder_text="Telefono")
        self.txtTlf.place(x=250, y=230)
        self.txtcor = CTkEntry(self.pantalla, placeholder_text="Correo")
        self.txtcor.place(x=250, y=280)


        btn_nuevo =  CTkButton(self.pantalla, text="Nuevo",command=self.registrarDonante, fg_color='#004C45', height=40)
        btn_nuevo.place(x=250, y=320)

        back_btn = CTkButton(self.pantalla, text="Volver a la lista", command=self.vol_dona, fg_color='#004C45')
        back_btn.place(x=250, y=80)

    def registrarDonante(self):
        if self.txtnom.get() == "" or self.txtdir.get() == "" or self.txtTlf.get() == "" or self.txtcor.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.insert_donantes(self.txtnom.get(), self.txtdir.get(), self.txtTlf.get(), self.txtcor.get()):
                messagebox.showinfo(message="Donante Registrado con exito", title="Info")
                self.limpiar_ventana()
                self.men()
            else:
                messagebox.showerror(message="El donante no fue registrado", title="Error")

    def vol_dona(self):
        self.limpiar_ventana()
        Donantes(self.list)


#PROVEEDORES
class Proveedores(Egresos_eco, Eco):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios = ControladorUsuarios()
        self.pantalla.geometry("800x600")

        img = CTkImage(light_image=Image.open("view/img/fondoprovee.jpg"), size=(800, 600))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="white",background="#004C45", relief="flat")
        style.map("Treeview.Heading", background=[('active','#004C45')])

        self.grid = ttk.Treeview( columns=("#1","#2","#3","#4","#5"), show="headings")

        self.grid.column("#0", width=5, anchor=CENTER)
        self.grid.column("#1",width=10, anchor=CENTER)
        self.grid.column("#2",width=40, anchor=CENTER)
        self.grid.column("#3",width=70, anchor=CENTER)
        self.grid.column("#4",width=60, anchor=CENTER)
        self.grid.column("#5",width=60, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("#1", text="id", anchor=CENTER)
        self.grid.heading("#2", text="Nombre", anchor=CENTER)
        self.grid.heading("#3", text="Direccion", anchor=CENTER)
        self.grid.heading("#4", text="Telefono", anchor=CENTER)
        self.grid.heading("#5", text="Correo", anchor=CENTER)

        sano= self.grid.get_children()
        for element in sano:
            self.grid.delete(element)
        
        data,i=self.ControladorUsuarios.mostar_proveedores(),-1
        for loca in data:
            self.grid.insert('',i, text=loca[0], values=(loca[0], loca[1], loca[2], loca[3], loca[4]))

        self.grid.place(x=100,y=110,width=600,height=400)


        back_btn = CTkButton(self.pantalla, text="Volver al menu", command=self.volveratras, fg_color='#004C45')
        back_btn.place(x=340, y=70) 

        back_btn = CTkButton(self.pantalla, text="Registrar",command=self.regis_provee, fg_color='#004C45')
        back_btn.place(x=423, y=520)

        back_btn = CTkButton(self.pantalla, text="Editar", command=self.Editar_provee, fg_color='#004C45')
        back_btn.place(x=243, y=520)

    def Editar_provee(self):
        self.sisas= self.grid.item(self.grid.selection())["text"]
        if self.sisas == "":
            messagebox.showerror(message="Seleccione un campo", title="Error")
        else:
            self.pantalla.withdraw()
            self.toplevel = CTkToplevel(self.pantalla)
            self.toplevel.geometry("650x450")
            self.toplevel.title("Editar Donantes")
            self.toplevel.resizable(width=False, height=False)

            img = CTkImage(light_image=Image.open("view/img/fondoedit.jpg"), size=(650, 450))
            lbl_img = CTkLabel(self.toplevel, image=img, text="")
            lbl_img.place(x=0, y=0)

            self.txtnom = CTkEntry(self.toplevel, placeholder_text="Nombre")
            self.txtnom.place(x=250, y=130)
            self.txtdir = CTkEntry(self.toplevel, placeholder_text="Direccion")
            self.txtdir.place(x=250, y=180)
            self.txtTlf = CTkEntry(self.toplevel, placeholder_text="Telefono")
            self.txtTlf.place(x=250, y=230)
            self.txtcor = CTkEntry(self.toplevel, placeholder_text="Correo")
            self.txtcor.place(x=250, y=280)

            btn_nuevo =  CTkButton(self.toplevel, text="Editar", command=self.editprovee, fg_color='#004C45', height=40)
            btn_nuevo.place(x=250, y=320)

            back_btn = CTkButton(self.toplevel, text="Volver a la lista", command=self.volveratrasok, fg_color='#004C45')
            back_btn.place(x=250, y=80)

    def editprovee(self):
        if self.txtnom.get() == "" or self.txtdir.get() == "" or self.txtTlf.get() == "" or self.txtcor.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.actualizar_proveedores(self.sisas, self.txtnom.get(), self.txtdir.get(), self.txtTlf.get(), self.txtcor.get()):
                messagebox.showinfo(message="Actualizado con exito")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Egresos_eco(self.list)
                self.toplevel.destroy() 
            else:
                messagebox.showerror(message="Error al Actualizar el Proveedor", title="Error")
                self.pantalla.deiconify()
                self.limpiar_ventana()
                Egresos_eco(self.list)
                self.toplevel.destroy()        

    def volveratrasok(self):
        self.pantalla.deiconify()
        self.toplevel.destroy()            
    
    def regis_provee(self):
        self.limpiar_ventana()
        Registro_proveedores(self.list)

class Registro_proveedores(Proveedores):
    def __init__(self, list):
        self.list = list
        self.pantalla = self.list[0]
        self.role = self.list[1]
        self.ControladorUsuarios=ControladorUsuarios()

        self.pantalla.title("Registro de miembros")
        self.pantalla.geometry("650x450")
        self.pantalla.resizable(width=False, height=False)

        img = CTkImage(light_image=Image.open("view/img/fondora.jpg"), size=(650, 450))
        lbl_img = CTkLabel(self.pantalla, image=img, text="")
        lbl_img.place(x=0, y=0)

        self.txtnom = CTkEntry(self.pantalla, placeholder_text="Nombre")
        self.txtnom.place(x=250, y=130)
        self.txtdir = CTkEntry(self.pantalla, placeholder_text="Direccion")
        self.txtdir.place(x=250, y=180)
        self.txtTlf = CTkEntry(self.pantalla, placeholder_text="Telefono")
        self.txtTlf.place(x=250, y=230)
        self.txtcor = CTkEntry(self.pantalla, placeholder_text="Correo")
        self.txtcor.place(x=250, y=280)

        btn_nuevo =  CTkButton(self.pantalla, text="Nuevo",command=self.registrarProveedor, fg_color='#004C45', height=40)
        btn_nuevo.place(x=250, y=320)

        back_btn = CTkButton(self.pantalla, text="Volver a la lista", command=self.vol_provee, fg_color='#004C45')
        back_btn.place(x=250, y=80)

    def registrarProveedor(self):
        if self.txtnom.get() == "" or self.txtdir.get() == "" or self.txtTlf.get() == "" or self.txtcor.get() == "":
            messagebox.showerror(message="Por favor, llenar los campos", title="Error")
        else:
            if self.ControladorUsuarios.insert_proveedores(self.txtnom.get(), self.txtdir.get(), self.txtTlf.get(), self.txtcor.get()):
                messagebox.showinfo(message="Proveedor Registrado con exito", title="Info")
                self.limpiar_ventana()
                self.men()
            else:
                messagebox.showerror(message="El Proveedor no fue registrado", title="Error")

    def vol_provee(self):
        self.limpiar_ventana()
        Proveedores(self.list)
