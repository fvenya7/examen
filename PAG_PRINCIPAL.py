from tkinter import Tk,Frame,Label,Button,Entry,Scale,StringVar,IntVar,Toplevel,ttk
import tkinter as tk
import catalogo
from editar_excel import list1

class Ventana_Principal(Frame):
	
	def __init__(self,master=None):
		super().__init__(master, width=600, height=400)
		self.master=master
		self.pack()
		self.crea_widgets()
		self.nombre= tk.StringVar()
		self.stock= tk.StringVar()
		self.precio= tk.StringVar()
		self.codigo= tk.StringVar()
		self.lista_nombres = []
		self.lista_precio = []
		self.lista_codigo = []
		self.lista_stock = []

		self.sumatotal=tk.StringVar()


		
	def Caja(self):
		self.caja = Toplevel()
		self.caja.geometry("910x500")

		tk.Label(self.caja, text="INGRESE LOS CODIGOS DEL LOS PRODUCTOS",bg="light yellow", font=("Verdana",18)).place(x=30,y=10,width=850, height=50)
		tk.Label(self.caja, text="CODIGO",bg="black",fg="white").place(x=30,y=70,width=120, height=30)
		tk.Label(self.caja, text="NOMBRE",bg="black",fg="white").place(x=155,y=70,width=200, height=30)
		tk.Label(self.caja, text="PRECIO",bg="black",fg="white").place(x=360,y=70,width=100, height=30)
		tk.Label(self.caja, text="STOCK",bg="black",fg="white").place(x=465,y=70,width=100, height=30)
		tk.Label(self.caja, text="VERIFICAR",bg="black",fg="white").place(x=570,y=70,width=100, height=30)
		tk.Label(self.caja, text="CANTIDAD",bg="black",fg="white").place(x=675,y=70,width=100, height=30)
		tk.Label(self.caja, text="SUBTOTAL",bg="black",fg="white").place(x=780,y=70,width=100, height=30)
		tk.Label(self.caja, textvariable=self.sumatotal).place(x=780,y=330,width=100, height=30)


		i=0
		self.botoncalc  = tk.Button(self.caja, text="CALCULAR",command=self.Calcular)
		self.botoncalc.place(x=780,y=440,width=100, height=30)

		self.lista_entradas = []
		self.lista_botones = []
		self.lista_cant = []
		self.lista_subtotal = []
		for i in range(5):
			self.lista_entradas.append(tk.Entry(self.caja))
			self.lista_entradas[i].place_configure(x=30,y=110+40*i,width=100,height=30)
			self.lista_botones.append(tk.Button(self.caja, text="CLICK",command=lambda a = i: self.Encontrar_nombre(a),bg="lime green"))		
			self.lista_botones[i].place_configure(x=570,y=110+40*i,width=100,height=30)
			
			self.lista_cant.append(tk.Entry(self.caja))
			self.lista_cant[i].place_configure(x=675,y=110+40*i,width=100, height=30)
			self.lista_nombres.append(tk.StringVar())
			self.lista_precio.append(tk.StringVar())
			self.lista_stock.append(tk.StringVar())
			self.lista_subtotal.append(tk.StringVar())
			tk.Label(self.caja,textvariable=self.lista_nombres[i],bg="LightSkyBlue3").place(x=155,y=110+40*i,width=200, height=30)
			tk.Label(self.caja,textvariable=self.lista_precio[i],bg="LightSkyBlue3").place(x=360,y=110+40*i,width=100, height=30)
			tk.Label(self.caja,textvariable=self.lista_stock[i],bg="LightSkyBlue3").place(x=465,y=110+40*i,width=100, height=30)
			tk.Label(self.caja,textvariable=self.lista_subtotal[i],bg="LightSkyBlue3").place(x=780,y=110+40*i,width=100, height=30)
			

		self.diccionario = dict(zip([0,1,2,3,4],self.lista_entradas))
		
	def Encontrar_nombre(self,numero):
		if self.diccionario[numero].get() != "":
			for i in list1:
				if i[1] == self.diccionario[numero].get():
					self.lista_nombres[numero].set(i[0])
					self.lista_precio[numero].set(i[3])
					self.lista_stock[numero].set(i[5])
	def Calcular(self):
		
		k = 0
		a,b,suma = 0.0,0.0,0.0
		for i in self.lista_subtotal:
			
			try: 
				a = float(self.lista_cant[k].get())
				b = float(self.lista_precio[k].get())
			except:
				a,b = 0.0,0.0
				pass
			if self.lista_cant[k].get() == "":
				a = 0.0
			if self.lista_precio[k].get() == "":
				b = 0.0
			k += 1
			suma+=a*b
			self.sumatotal.set(suma)
			i.set(str(a*b))


	def crea_widgets(self):
		tk.Label(self,text="Bienvenido!",bg="ivory2", font=("Verdana",24)).place(x=10,y=10,width=580, height=50)
		tk.Label(self, text="¿Que accion desea realizar?").place(x=210,y=70,width=200, height=30)

		tk.Button(self,text="Ir al catalogo", command=self.catalogo).place(x=100,y=200,width=120, height=30)
		tk.Button(self,text="Generar boleta", command=self.Caja).place(x=250,y=200,width=120, height=30)
		tk.Button(self,text="Cerrar caja").place(x=400,y=200,width=120, height=30)
		tk.Button(self,text="Salir",bg="red4").place(x=400,y=300,width=120, height=30)

	def catalogo(self):
		catalogo.Ventana_catalogo()

if __name__ == "__main__":
    root = tk.Tk()
    Ventana_Principal(root)
    root.mainloop()