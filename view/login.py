from customtkinter import *
from tkinter import messagebox
from tkinter import *
from PIL import Image
from view.menu import menu
from controller.cont import *



class log:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.ControladorUsuarios=ControladorUsuarios()

        lb = Label(pantalla, text="Acceso al Sistema", bg="#004C45", fg="white", width="300", height="3", font="1" )
        lb.pack()

        img = CTkImage(light_image=Image.open("view/img/logo_peq.png"), size=(250, 150))
        lbl_img = CTkLabel(pantalla, image=img, text="")
        lbl_img.pack(pady=20)

        CTkLabel(pantalla, text="Usuario").pack()
        self.usuarioVerify = CTkEntry(pantalla)
        self.usuarioVerify.pack()

        CTkLabel(pantalla, text="Contraseña").pack()
        self.passwordVerify = CTkEntry(pantalla, show="*")
        self.passwordVerify.pack()

        boton_ini = CTkButton(pantalla, text="Iniciar Sesion", command=self.LoginValidation, fg_color='#004C45')
        boton_ini.pack(pady=10)
    
    def limpiar_ventana(self):
        for widget in self.pantalla.winfo_children():
            widget.destroy()

    def LoginValidation(self):
        if self.ControladorUsuarios.userVerify(self.usuarioVerify.get(), self.passwordVerify.get()):
            self.role = self.ControladorUsuarios.userVerify(self.usuarioVerify.get(), self.passwordVerify.get())[0][3]
            self.limpiar_ventana()
            self.list = [self.pantalla, self.role]
            menu(self.list)

        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")



  
        
        
        
    
