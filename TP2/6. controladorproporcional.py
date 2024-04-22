class ControladorProporcional:
    def __init__(self, kp):
        self.kp = kp  # Ganancia proporcional

    def calcular_entrada(self, setpoint, temperatura_actual):
        error = setpoint - temperatura_actual
        entrada = self.kp * error
        return entrada

# Simulación del sistema de control de temperatura
class Horno:
    def __init__(self, temperatura_inicial=20):
        self.temperatura = temperatura_inicial

    def actualizar_temperatura(self, entrada_control):
        # Simulamos el proceso del horno
        self.temperatura += entrada_control

# Función de simulación del proceso de control
def simular_control():
    controlador = ControladorProporcional(kp=0.5)  # Ganancia proporcional
    horno = Horno(temperatura_inicial=25)  # Temperatura inicial del horno

    setpoint = 150  # Temperatura deseada
    tiempo_simulacion = 100  # Tiempo de simulación en segundos
    tiempo = 0

    while tiempo < tiempo_simulacion:
        entrada_control = controlador.calcular_entrada(setpoint, horno.temperatura)
        horno.actualizar_temperatura(entrada_control)
        tiempo += 1
        print(f"Tiempo: {tiempo}, Temperatura: {horno.temperatura:.2f}")

# Ejecutar la simulación del control
simular_control()
