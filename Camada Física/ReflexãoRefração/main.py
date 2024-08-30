import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o ângulo de refração usando a Lei de Snell
def angulo_reflexao(n1, n2, angulo_incidencia):
    # n1: índice de refração do núcleo
    # n2: índice de refração da casca
    # angulo_incidencia: ângulo de incidência em graus
    angulo_incidencia_rad = np.radians(angulo_incidencia)
    angulo_refracao_rad = np.arcsin(n1 * np.sin(angulo_incidencia_rad) / n2)
    return np.degrees(angulo_refracao_rad)

# Parâmetros da fibra óptica
n1 = 1.5  # Índice de refração do núcleo
n2 = 1.4  # Índice de refração da casca
angulo_incidencia = np.linspace(0, 90, 500)  # Variação do ângulo de incidência

# Cálculo do ângulo de refração
angulo_refracao = np.array([angulo_reflexao(n1, n2, ang) for ang in angulo_incidencia])

# Encontrar o ângulo crítico para reflexão total interna
angulo_critico = np.degrees(np.arcsin(n2 / n1))
reflexao_total = angulo_incidencia >= angulo_critico

# Gráfico
plt.figure(figsize=(8, 5))
plt.plot(angulo_incidencia, angulo_refracao, label="Ângulo de Refração")
plt.axvline(x=angulo_critico, color='r', linestyle='--', label=f"Ângulo Crítico: {angulo_critico:.2f}°")
plt.fill_between(angulo_incidencia, angulo_refracao, where=reflexao_total, color='gray', alpha=0.3, label="Reflexão Total Interna")
plt.xlabel("Ângulo de Incidência (graus)")
plt.ylabel("Ângulo de Refração (graus)")
plt.title("Simulação de Reflexão e Refração em Fibra Óptica")
plt.legend()
plt.grid(True)
plt.show()
