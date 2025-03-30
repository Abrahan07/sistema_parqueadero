from Vehiculos import Vehiculo

class Principal:
    def __init__(self):
        self.objFormulario = Vehiculo()
    
    def ejecutar(self):
        auxFormulario = self.objFormulario.iniciar_ventana() 
        auxFormulario.mainloop()  

if __name__ == "__main__":
    app = Principal()
    app.ejecutar()