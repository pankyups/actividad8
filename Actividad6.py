class Cuenta:
  def __init__(self, titular, cantidad = None):
    self.titular = titular
    self.cantidad = cantidad

  def mostrar(self):
    print(self.titular, self.cantidad)

  def ingresar(self, cantidad_a_agregar):
    if cantidad_a_agregar < 0:
      return

    self.cantidad += cantidad_a_agregar

  def retirar(self, cantidad_a_retirar):
    self.cantidad -= cantidad_a_retirar