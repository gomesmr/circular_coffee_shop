import logging


class Logger:
    def __init__(self, nome, nivel=logging.INFO):
        # Criar e configurar um logger
        self.logger = logging.getLogger(nome)
        self.logger.setLevel(nivel)
        self.logger.propagate = False  # Evitar duplicação de logs

        # Criar um manipulador de log que escreve mensagens no console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(nivel)

        # Formatação do log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Adicionar o manipulador ao logger
        self.logger.addHandler(console_handler)

    def set_level(self, nivel):
        self.logger.setLevel(nivel)

    def debug(self, mensagem):
        self.logger.debug(mensagem)

    def info(self, mensagem):
        self.logger.info(mensagem)

    def warning(self, mensagem):
        self.logger.warning(mensagem)

    def error(self, mensagem):
        self.logger.error(mensagem)

    def critical(self, mensagem):
        self.logger.critical(mensagem)
