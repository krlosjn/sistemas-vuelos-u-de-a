class Avion:
    def __init__(self, matricula, modelo, capacidad_pasajeros, capacidad_carga):
        self.matricula = matricula
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"Avion modelo: {self.modelo}, matrícula: {self.matricula}, capacidad: {self.capacidad_pasajeros} pasajeros, carga: {self.capacidad_carga} kg"

class Vuelo:
    def __init__(self, id_vuelo, avion, origen, destino, hora_salida, hora_llegada, nombre_registro, cedula_registro):
        self.id_vuelo = id_vuelo
        self.avion = avion
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.nombre_registro = nombre_registro
        self.cedula_registro = cedula_registro
        self.pasajeros = []
        self.equipaje_total = 0

    def __str__(self):
        return (
            f"Vuelo {self.id_vuelo}:\n"
            f"- Avion: {self.avion.modelo} (Matrícula: {self.avion.matricula})\n"
            f"- Origen: {self.origen}\n"
            f"- Destino: {self.destino}\n"
            f"- Hora de salida: {self.hora_salida}\n"
            f"- Hora de llegada: {self.hora_llegada}\n"
            f"- Registrado por: {self.nombre_registro} (Cédula: {self.cedula_registro})"
        )

class SistemaFBO:
    def __init__(self):
        self.aviones = []
        self.vuelos = []

    def registrar_avion(self):
        matricula = input("Ingresa la matrícula del avion: ")
        modelo = input("Ingresa el modelo del avion: ")
        capacidad_pasajeros = int(input("Ingresa la capacidad de pasajeros: "))
        capacidad_carga = float(input("Ingresa la capacidad de carga en kg: "))
        avion = Avion(matricula, modelo, capacidad_pasajeros, capacidad_carga)
        self.aviones.append(avion)
        print("Avion registrado.")

    def programar_vuelo(self):
        if not self.aviones:
            print("No hay aviones registrados. Registra un avion antes de proseguir.")
            return

        print("Aviones disponibles:")
        for idx, avion in enumerate(self.aviones):
            print(f"{idx}. {avion}")

        while True:
            try:
                avion_idx = int(input("Selecciona el índice del avión para el vuelo: "))
                if 0 <= avion_idx < len(self.aviones):
                    break
                else:
                    print("Indice fuera de rango.")
            except ValueError:
                print("Ingresa un numero valido.")

        avion = self.aviones[avion_idx]

        id_vuelo = input("Ingresa el ID del vuelo: ")
        origen = input("Ingresa el origen del vuelo: ")
        destino = input("Ingresa el destino del vuelo: ")
        hora_salida = input("Ingresa la hora de salida: ")
        hora_llegada = input("Ingresa la hora de llegada: ")
        nombre_registro = input("Ingresa nombre del pasajero: ")
        cedula_registro = input("Ingresa cedula del pasajero: ")

        vuelo = Vuelo(id_vuelo, avion, origen, destino, hora_salida, hora_llegada, nombre_registro, cedula_registro)
        self.vuelos.append(vuelo)
        print("\nVuelo programado correctamente:")
        print(vuelo)

    def mostrar_vuelos(self):
        if not self.vuelos:
            print("No hay vuelos programados.")
            return

        print("Vuelos programados:")
        for vuelo in self.vuelos:
            print(vuelo)
            print("-" * 40)

    def cancelar_vuelo(self):
        if not self.vuelos:
            print("No hay vuelos programados para cancelar.")
            return

        print("Vuelos programados:")
        for idx, vuelo in enumerate(self.vuelos):
            print(f"{idx}. {vuelo.id_vuelo} - {vuelo.origen} a {vuelo.destino}")

        while True:
            try:
                vuelo_idx = int(input("Selecciona el indice del vuelo a cancelar: "))
                if 0 <= vuelo_idx < len(self.vuelos):
                    vuelo_cancelado = self.vuelos.pop(vuelo_idx)
                    print(f"El vuelo {vuelo_cancelado.id_vuelo} ha sido cancelado.")
                    break
                else:
                    print("Indice fuera de rango.")
            except ValueError:
                print("Ingresa un número válido.")

    def menu(self):
        while True:
            print("\n-Sistema FBO-")
            print("1. Registrar avion")
            print("2. Programar vuelo")
            print("3. Mostrar vuelos")
            print("4. Cancelar vuelo")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.registrar_avion()
            elif opcion == "2":
                self.programar_vuelo()
            elif opcion == "3":
                self.mostrar_vuelos()
            elif opcion == "4":
                self.cancelar_vuelo()
            elif opcion == "5":
                print("Has salido del sistema")
                break
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    sistema = SistemaFBO()
    sistema.menu()