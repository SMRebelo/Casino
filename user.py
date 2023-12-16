class User:
    def __init__(self, nome, senha, saldo, score_quiz, score_lot, score_rasp1, score_rasp2, tokens):
        self.nome = nome
        self.senha = senha
        self.saldo = saldo
        self.score_quiz = score_quiz
        self.score_lot = score_lot
        self.score_rasp1 = score_rasp1
        self.score_rasp2 = score_rasp2
        self.tokens = tokens