import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# 1. Definir el sistema LTI
# Usaremos un sistema de segundo orden como ejemplo
num = [1]
den = [1, 2, 1]
system = ctl.tf(num, den)

# 2. Crear el controlador PID
# Parámetros del PID
Kp = 350
Ki = 300
Kd = 50

# Función de transferencia del PID
pid = ctl.tf([Kd, Kp, Ki], [1, 0])

# 3. Configurar el sistema en lazo cerrado
closed_loop_system = ctl.feedback(pid * system, 1)

# 4. Análisis de la respuesta temporal
time = np.linspace(0, 2, 100)
t, y = ctl.step_response(closed_loop_system, time)

# 5. Graficar la respuesta temporal
plt.figure()
plt.plot(t, y)
plt.title('Respuesta temporal del sistema en lazo cerrado con PID')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta (Amplitud)')
plt.grid(True)

# 6. Análisis de la respuesta en frecuencia
mag, phase, omega = ctl.bode_plot(closed_loop_system, dB=True)

# Mostrar todas las gráficas
plt.show()
