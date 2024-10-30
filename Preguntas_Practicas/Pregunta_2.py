from abc import ABC, abstractmethod

# Definimos la interfaz de estrategia para integración numérica
class IntegrationStrategy(ABC):
    @abstractmethod
    def integrate(self, func, a, b, n):
        pass

# Estrategia: Método del Trapecio
class TrapezoidalMethod(IntegrationStrategy):
    def integrate(self, func, a, b, n):
        h = (b - a) / n
        result = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            result += func(a + i * h)
        return result * h

# Estrategia: Método de Simpson
class SimpsonMethod(IntegrationStrategy):
    def integrate(self, func, a, b, n):
        if n % 2 == 1:  # Simpson's rule requires an even number of intervals
            n += 1
        h = (b - a) / n
        result = func(a) + func(b)
        for i in range(1, n, 2):
            result += 4 * func(a + i * h)
        for i in range(2, n-1, 2):
            result += 2 * func(a + i * h)
        return result * h / 3

# Clase Integrator que utiliza la estrategia seleccionada
class Integrator:
    def __init__(self, strategy: IntegrationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: IntegrationStrategy):
        self.strategy = strategy

    def integrate(self, func, a, b, n):
        return self.strategy.integrate(func, a, b, n)

# Función de prueba para integración
def example_function(x):
    return x ** 2  # Integrar f(x) = x^2

# Ejemplo de uso del patrón Estrategia para integración numérica
a = 0  # Límite inferior de integración
b = 1  # Límite superior de integración
n = 10  # Número de intervalos

# Integración usando el método del trapecio
integrator = Integrator(TrapezoidalMethod())
print("Trapecio:", integrator.integrate(example_function, a, b, n))

# Cambiar a método de Simpson en tiempo de ejecución
integrator.set_strategy(SimpsonMethod())
print("Simpson:", integrator.integrate(example_function, a, b, n))