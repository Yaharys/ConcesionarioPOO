from abc import ABC, abstractmethod

# Paso 1: clase padre 
class Vehiculo(ABC):

    # Paso 2: atributos "encapsulados" 
    # _marca, _modelo, _precio_base

    # Paso 3: constructor con validación
    def __init__(self, marca: str, modelo: str, precio_base: float):
        if precio_base <= 0:
            raise ValueError("El precio_base debe ser mayor que 0.")
        self._marca = marca
        self._modelo = modelo
        self._precio_base = float(precio_base)

    # Paso 4: propiedades de solo lectura
    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def precio_base(self) -> float:
        return self._precio_base

    # Paso 5: método abstracto -> impuesto
    @abstractmethod
    def impuesto(self) -> float:
        """Debe devolver el valor del impuesto según el tipo de vehículo."""
        pass

    # Paso 6: precio_final = precio_base + impuesto()
    def precio_final(self) -> float:
        return self._precio_base + self.impuesto()

    # Paso 7: método ficha() y __str__
    def ficha(self) -> str:
        # similar a: "%s %s ($%.2f)" (formato clásico)
        return f"{self.marca} {self.modelo} (${self.precio_base:.2f})"

    def __str__(self) -> str:
        # similar a: "%s | Final: $%.2f"
        return f"{self.ficha()} | Final: ${self.precio_final():.2f}"


# Paso 8: clase hija (Automovil)
class Automovil(Vehiculo):

    # Paso 9: constructor con validación de puertas
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que 0.")
        self._puertas = int(puertas)

    # Paso 10: implementar impuesto() según la rúbrica
    # 8% del precio base; si tiene 5 puertas, restar 1% del precio base a ese impuesto
    def impuesto(self) -> float:
        imp = self.precio_base * 0.08         # 8%
        desc = self.precio_base * 0.01 if self._puertas == 5 else 0.0
        return imp - desc

    # Paso 11: sobrescribir ficha()
    def ficha(self) -> str:
        # "Automovil | " + super.ficha() + " | X puertas"
        return f"Automovil | {super().ficha()} | {self._puertas} puertas"


# Paso 12: clase hija (Moto)
class Moto(Vehiculo):

    # Paso 13: constructor con validación de cc
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        if cc <= 0:
            raise ValueError("El cilindraje (cc) debe ser mayor que 0.")
        self._cc = int(cc)

    # Paso 14: implementar impuesto()
    # Si cc ≤ 250 → 5%; si cc > 250 → 9%
    def impuesto(self) -> float:
        tasa = 0.05 if self._cc <= 250 else 0.09
        return self.precio_base * tasa

    # Paso 15: sobrescribir ficha()
    def ficha(self) -> str:
        return f"Moto | {super().ficha()} | {self._cc} cc (cilindraje)"


# Paso 16: Principal 
def main():
    # Paso 17: lista de Vehiculo (polimorfismo)
    inventario: list[Vehiculo] = [
        Automovil("Toyota", "Yaris", 20000, 5),     # auto 5 puertas
        Automovil("Hyundai", "Accent", 18000, 4),   # auto 4 puertas
        Moto("Yamaha", "FZ 2.0", 3500, 150),        # moto <= 250cc
        Moto("Kawasaki", "Ninja 400", 6200, 399),   # moto > 250cc
    ]

    # Paso 18: recorrer e imprimir cada vehículo
    total = 0.0
    for v in inventario:
        print(v)                      # debe verse ficha + precio final
        total += v.precio_final()     # polimorfismo: llama al de cada hijo

    # Paso 19: imprimir total del inventario
    print(f"Valor total del inventario: ${total:.2f}")


# Punto de entrada: bloque principal en Python
if __name__ == "__main__":
    main()