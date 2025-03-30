import tkinter as Ventana
from tkinter import messagebox

class Vehiculo:
    def __init__(self):
        self.lista_vehiculos = []
        self.ventana_formulario = Ventana.Tk()
        self.ventana_formulario.title("Formulario de Vehículo")

        self.label_placa = Ventana.Label(self.ventana_formulario, text="Ingrese la placa: ")
        self.label_placa.configure(bg="yellow", fg = "red")
        self.entry_placa = Ventana.Entry(self.ventana_formulario)
        self.label_marca = Ventana.Label(self.ventana_formulario, text="Ingrese la marca: ")
        self.label_marca.configure(bg="yellow", fg = "red")
        self.entry_marca = Ventana.Entry(self.ventana_formulario)
        self.label_color = Ventana.Label(self.ventana_formulario, text="Ingrese el color: ")
        self.label_color.configure(bg="yellow", fg = "red")
        self.entry_color = Ventana.Entry(self.ventana_formulario)
        self.label_tipo = Ventana.Label(self.ventana_formulario, text="Ingrese el tipo (Residente/Visitante): ")
        self.label_tipo.configure(bg="yellow", fg = "red")
        self.entry_tipo = Ventana.Entry(self.ventana_formulario)
        self.label_hora = Ventana.Label(self.ventana_formulario, text="Ingrese la hora: ")
        self.label_hora.configure(bg="yellow", fg = "red")
        self.entry_hora = Ventana.Entry(self.ventana_formulario)

        self.boton_enviar = Ventana.Button(self.ventana_formulario, text="Guardar cliente", command= lambda : self.tomar_datos())
        self.boton_enviar.configure(bg="blue", fg="yellow", width=30)
        self.boton_limpiar = Ventana.Button(self.ventana_formulario, text="Limpiar campos", command= lambda : self.evento_borrar())
        self.boton_limpiar.configure(bg="blue", fg="yellow", width=30)
        self.boton_mostrar = Ventana.Button(self.ventana_formulario, text="Mostrar clientes", command= lambda : self.evento_mostrar())
        self.boton_mostrar.configure(bg="blue", fg="yellow", width=30)

        self.label_placa.grid(row=0, column=0)
        self.entry_placa.grid(row=0, column=1)
        self.label_marca.grid(row=1, column=0)
        self.entry_marca.grid(row=1, column=1)
        self.label_color.grid(row=2, column=0)
        self.entry_color.grid(row=2, column=1)
        self.label_tipo.grid(row=3, column=0)
        self.entry_tipo.grid(row=3, column=1)
        self.label_hora.grid(row=4, column=0)
        self.entry_hora.grid(row=4, column=1)
        self.boton_enviar.grid(row=5, column=0)
        self.boton_limpiar.grid(row=5, column=1)
        self.boton_mostrar.grid(row=6, column=0, columnspan=2)

        self.labelResultado = Ventana.Label(self.ventana_formulario, text="")
        self.labelResultado.configure(bg="yellow", fg = "red")
        self.labelResultado.grid(row=7, column=0, columnspan=2, sticky="ew")
        

    def iniciar_ventana(self):
        """ Método para devolver la ventana (sin ejecutar `mainloop`) """
        self.ventana_formulario.geometry("400x400")
        self.ventana_formulario.resizable(False, False)
        self.ventana_formulario.configure(bg="red")
        self.ventana_formulario.configure(cursor="hand2")
        return self.ventana_formulario

    def tomar_datos(self):
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        color = self.entry_color.get()
        tipo = self.entry_tipo.get()
        hora = self.entry_hora.get()
        
        if not all([placa, marca, color, tipo, hora]):
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        vehiculos = {
            "placa": placa,
            "marca": marca,
            "color": color,
            "tipo": tipo,
            "hora": hora
        }
        self.lista_vehiculos.append(vehiculos)
        messagebox.showwarning("Valido","Vehiculo registrado exitosamente.")
        print("Vehiculo registrado")
        

    def evento_borrar(self):
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')
        self.entry_hora.delete(0, 'end')
        print("campos  borrados...")

    def evento_mostrar(self):
        if not self.lista_vehiculos:
            self.labelResultado.config(text="Lista vacía", fg="red")
        else:
            msj = "Listado de vehículos:\n"
            for i, diccionario in enumerate(self.lista_vehiculos, start=1):
                msj += f"{i}. Placa: {diccionario['placa']}, Marca: {diccionario['marca']}, Color: {diccionario['color']}, Tipo: {diccionario['tipo']}, Hora: {diccionario['hora']}\n"

            self.labelResultado.config(text=msj, fg="black", wraplength=400, justify="left")
