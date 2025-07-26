# 💳 Simulador de Tarjetas de Crédito en Python

Este proyecto fue desarrollado como parte del Bootcamp de Desarrollador Full Stack Python Trainee de Skillnest. El objetivo principal es poner en práctica conceptos fundamentales de la **Programación Orientada a Objetos (POO)** en Python.

## 🚀 Objetivos del Proyecto

- Practicar la creación de clases con atributos y métodos personalizados.
- Implementar argumentos por defecto.
- Utilizar estructuras de control de flujo.
- Manipular atributos de instancia usando `self`.
- Aplicar encadenamiento de métodos (`return self`).
- Simular el funcionamiento básico de una tarjeta de crédito: compras, pagos, cobro de intereses y visualización de saldo.

## 🧠 Conceptos Aplicados

- Clases y objetos
- Métodos de instancia
- Métodos de clase (`@classmethod`)
- Encadenamiento de métodos
- Valores por defecto en el constructor (`__init__`)
- Lógica condicional con `if / else`

## 🏗️ Estructura de la Clase

```python
class TarjetaCredito:
    tarjetas_creadas = []

    def __init__(self, nombre, limite_credito, intereses, saldo_pagar=0):
        ...

    def compra(self, monto):
        ...

    def pago(self, monto):
        ...

    def mostrar_info_tarjeta(self):
        ...

    def cobrar_interes(self):
        ...

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        ...
```

## 🧪 Ejemplo de Uso

```python
tarjeta_1 = TarjetaCredito('Tarjeta 1', 10000, 0.015)
tarjeta_2 = TarjetaCredito('Tarjeta 2', 20000, 0.020)
tarjeta_3 = TarjetaCredito('Tarjeta 3', 30000, 0.025)

tarjeta_1.compra(3000).compra(5000).pago(4000).cobrar_interes().mostrar_info_tarjeta()
tarjeta_2.compra(2000).compra(5500).compra(1111).pago(5555).pago(3000).cobrar_interes().mostrar_info_tarjeta()
tarjeta_3.compra(5000).compra(10000).compra(8000).compra(4500).compra(5000).mostrar_info_tarjeta()

TarjetaCredito.mostrar_todas_las_tarjetas()
```

## 📎 Requisitos

Python 3.6+

No se requieren librerías externas

## 🧑‍💻 Autor

Estefany Rodríguez P
GitHub: @EstefanyRodriguezP
