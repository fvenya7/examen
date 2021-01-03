import tkinter as tk
import ph,galleta,detergente,aceite,leche,cafe,shampoo,abarrote,conserva,pasta

class Ventana_catalogo(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Catalogo de Productos")
        self.crea_categorias()
        self.geometry("600x400+750+100")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        

    def volver(self):
        self.deiconify()
        self.destroy()
    def crea_categorias(self):
        tk.Label(self, text="Categorias de productos",bg="white", font=("Verdana",24)).place(x=10,y=10,width=600, height=50)
        tk.Button(self, text="Papel Higienico", command=self.pah).place(x=80,y=100,width=200, height=30)
        tk.Button(self, text="Galletas", command=self.galleta).place(x=80,y=150,width=200, height=30)
        tk.Button(self, text="Detergente", command=self.detergente).place(x=80,y=200,width=200, height=30)
        tk.Button(self, text="Aceite", command=self.aceite).place(x=80,y=250,width=200, height=30)
        tk.Button(self, text="Leche", command=self.leche).place(x=80,y=300,width=200, height=30)
        tk.Button(self, text="Café", command=self.cafe).place(x=340,y=100,width=200, height=30)
        tk.Button(self, text="Shampoo", command=self.shampoo).place(x=340,y=150,width=200, height=30)
        tk.Button(self, text="Abarrotes", command=self.abarrote).place(x=340,y=200,width=200, height=30)
        tk.Button(self, text="Conservas", command=self.conserva).place(x=340,y=250,width=200, height=30)
        tk.Button(self, text="Pastas", command=self.pasta).place(x=340,y=300,width=200, height=30)


    def pah(self):
        ph.ventana_ph()
    def galleta(self):
        galleta.ventana_galleta()
    def detergente(self):
        detergente.ventana_detergente()
    def aceite(self):
        aceite.ventana_aceite()
    def leche(self):
        leche.ventana_leche()
    def cafe(self):
        cafe.ventana_cafe()
    def shampoo(self):
        shampoo.ventana_shampoo()
    def abarrote(self):
        abarrote.ventana_abarrote()
    def conserva(self):
        conserva.ventana_conserva()
    def pasta(self):
        pasta.ventana_pasta()