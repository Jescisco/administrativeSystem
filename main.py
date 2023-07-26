from customtkinter import *
from view.login import log

if __name__ == "__main__":
    pantalla = CTk()
    pantalla.title("Nueva Acropolis")
    pantalla.geometry("350x450")
    pantalla.resizable(width=False, height=False)
    log(pantalla)
    pantalla.mainloop()


 
    

    
