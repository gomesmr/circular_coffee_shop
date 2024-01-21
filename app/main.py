import random

from app.domain import AquecedorDeAguaParaCafe


if __name__ == '__main__':
    aquecedor_de_agua = AquecedorDeAguaParaCafe()
    temperatura_aleatoria = round(random.uniform(90, 96), 1)
    aquecedor_de_agua.ajustar_temperatura(temperatura_aleatoria)