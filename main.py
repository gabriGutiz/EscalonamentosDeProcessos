
from simulador import Simulador

opcoes = {
    1: ['First come, first served', 'fcfs'],
    2: ['Shortest Job First', 'sjf'],
    3: ['Não implementado', ''],
    4: ['Round-Robin', 'rr'],
    5: ['COMPARAR ALGORÍTMOS', 'compare'],
    0: ['SAIR', 'sair'],
}

def main():
    print('========== Opções para simular  ==========')

    for index in opcoes.keys():
        print(f'== ( {index} ) {opcoes.get(index)[0].center(30)} ==')

    opcao = input('Sua opção: ')
    print('\n')

    if opcao.isnumeric():
        opcao = int(opcao)
        if opcoes.get(opcao) is None:
            print('Opção inválida! Tente novamente!\n')
            main()
        elif opcao == 0:
            return '\nSaindo...'
        else:
            try:
                simulador = Simulador('./input/simulacao.csv', opcao)
                return simulador.simular()
            except Exception as ex:
                print(ex)

if __name__ == '__main__':
    print('** LEIA AS INSTRUÇÕES NO README.md PARA MELHOR UTILIZAÇÃO **')
    print(main())
