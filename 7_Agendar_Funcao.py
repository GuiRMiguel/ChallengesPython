"""
Desafio #7: Agendamento de funções
Seu objetivo é implementar uma função chamada agendar_funcao(), que recebe três argumentos de entrada:

horário em que executar uma função específica;
a função que você deseja executar; e
um número variável (zero ou mais) de argumentos que são passados para a função de agendamento para uso.
Exemplo de entrada e saída
>>> agendar_funcao(time.time() + 3, print, 'Olá!')
# print() agendado para Sun Jan 28 01:18:06 2024
Então, 3 segundos depois...

Olá!
"""

import time
import threading


def agendar_funcao(horario, funcao, *args):
    """
    Agenda uma função para ser executada em um horário específico.

    :param horario: Horário (timestamp) em que a função será executada
    :param funcao: Função a ser executada
    :param args: Argumentos para a função
    """

    def tarefa_agendada():
        tempo_atual = time.time()
        tempo_espera = max(0, horario - tempo_atual)
        print(f"{funcao.__name__} agendado para {time.ctime(horario)}")
        time.sleep(tempo_espera)
        funcao(*args)

    # Usar uma thread para não bloquear a execução do programa principal
    threading.Thread(target=tarefa_agendada).start()


if __name__ == "__main__":
    # Exemplo de uso
    agendar_funcao(time.time() + 3, print, 'Olá!')
