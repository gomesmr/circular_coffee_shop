class AquecedorDeAguaParaCafe:
    def __init__(self):
        self.temperatura_atual = 25  # temperatura ambiente inicial

    def ajustar_temperatura(self, temperatura_desejada):
        if 90 <= temperatura_desejada <= 96:
            self.temperatura_atual = temperatura_desejada
            print(f"Ajustando a temperatura para {temperatura_desejada:.1f} graus Celsius, ideal para café.")
        else:
            print("Temperatura fornecida fora da faixa ideal de 90°C a 96°C para café.")