import tkinter as tk
from editar_excel import list1


class ventana_leche(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Papel Higienico")
        self.geometry("300x160")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        self.generar_inv()
        tk.Button(self, text="Volver", command=self.volver).grid(row=6,column=1)

        

    def volver(self):
        self.deiconify()
        self.destroy()
    def generar_inv(self):
        i=20
        j=1
        tk.Label(self,text="          NOMBRE        ",bg="black",fg="white").grid(row=0,column=0)
        tk.Label(self,text="        CODIGO        ",bg="black",fg="white").grid(row=0,column=1)
        tk.Label(self,text="        PRECIO        ",bg="black",fg="white").grid(row=0,column=2)
        for element in range(5):
            tk.Label(self,text=list1[i][0]).grid(row=j,column=0)
            tk.Label(self,text=list1[i][1]).grid(row=j,column=1)
            tk.Label(self,text=f"S/. {list1[i][3]}").grid(row=j,column=2)
            i=i+1
            j=j+1

