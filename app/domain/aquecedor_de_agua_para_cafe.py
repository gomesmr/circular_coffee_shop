# A classe AquecedorDeAguaParaCafe com o sistema de log integrado
from app.infraestructure.logging.logger import Logger


class AquecedorDeAguaParaCafe:
    def __init__(self):
        self.logger = Logger('AquecedorDeAguaParaCafe')
        self.temperatura_atual = 25  # temperatura ambiente inicial
        self.logger.info(f"Aquecedor de Água para Café inicializado com temperatura ambiente de {self.temperatura_atual}°C")

    def ajustar_temperatura(self, temperatura_desejada):
        if 90 <= temperatura_desejada <= 96:
            self.temperatura_atual = temperatura_desejada
            self.logger.info(f"Ajustando a temperatura para {temperatura_desejada:.1f} graus Celsius, ideal para café.")
        else:
            self.logger.warning("Temperatura fornecida fora da faixa ideal de 90°C a 96°C para café.")
