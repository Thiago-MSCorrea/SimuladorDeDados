from random import randint as rd

class SimulaDado():
    def __init__(self):
        self.pergunta = 'Você gostaria de jogar o dado? '
        self.adeus = 'Até outro dia!'
    def inicio(self):
        SIM = True
        resposta = input(self.pergunta)
        while SIM:
            try:
                if resposta == 'sim' or resposta == 'Sim' or resposta == 's':
                        print(rd(1,6))
                        resposta = input(self.pergunta)
                elif resposta == 'Não' or resposta == 'não' or resposta == 'n':
                    print(self.adeus)
                    SIM = False
                else:
                    print('Digite sim(S) ou não(n), por favor.')
                    resposta = input(self.pergunta)
            except:
                print('Ocorreu um erro ao analisar sua resposta, por favor digite sim (s) ou não (n)')
                resposta = input(self.pergunta)
simulador = SimulaDado()
simulador.inicio()
