class TarjetaCredito:
   
    tarjetas_creadas = []

    def __init__(self, nombre, limite_credito, intereses, saldo_pagar = 0):
       self.nombre = nombre
       self.limite_credito = limite_credito
       self.intereses = intereses
       self.saldo_pagar = saldo_pagar
       TarjetaCredito.tarjetas_creadas.append(self)

    def __str__(self):
        return f"{self.nombre} -> Saldo a pagar: ${self.saldo_pagar}, Límite: ${self.limite_credito}, Interés: {self.intereses}"

    def compra(self, monto):
        if monto <= self.limite_credito:
            self.saldo_pagar += monto
            self.limite_credito -= monto
            print(f'{self.nombre}, Haz realizado una compra por ${monto}')
        else:
            print(f'{self.nombre}: Tarjeta Rechazada, has alcanzado tu límite de crédito ')
        return self

    def pago(self, monto):
        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            print(f'{self.nombre}, Haz realizado un pago por ${monto}, tu nuevo saldo a pagar es ${self.saldo_pagar}')
        else:
            print('El monto ingresado supera el saldo a pagar, inténtalo de nuevo')
        return self
        
    def mostrar_info_tarjeta(self):
        print(f'{self.nombre}. Saldo a pagar: ${self.saldo_pagar}. Límite de crédito: ${self.limite_credito}')
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        print(f'{self.nombre}, El nuevo saldo a pagar con intereses es ${self.saldo_pagar}')
        return self
   
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        for tarjeta in cls.tarjetas_creadas:
            print(tarjeta)
   
tarjeta_1 = TarjetaCredito('Tarjeta 1', 10000, 0.015)
tarjeta_2 = TarjetaCredito('Tarjeta 2', 20000, 0.020)
tarjeta_3 = TarjetaCredito('Tarjeta 3', 30000, 0.025)

tarjeta_1.compra(3000).compra(5000).pago(4000)
tarjeta_2.compra(2000).compra(5500).compra(1111).pago(5555).pago(3000).cobrar_interes()
tarjeta_3.compra(5000).compra(10000).compra(8000).compra(4500).compra(5000).mostrar_info_tarjeta()

TarjetaCredito.mostrar_todas_las_tarjetas()