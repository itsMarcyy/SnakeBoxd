import os
import sys

def main():
      while True:
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

def exibir_nome_do_programa():
    print ('Snake Box. 🐍')
    
def exibir_opcoes():
    print('\n--- Menu ---')
    print()
    print('1. Adicionar uma nova obra')
    print('2. Listar obras')
    print('3. Sair')

def voltar_ao_menu_principal():
    input('\nAperte uma tecla para voltar ao menu principal. ')

class Obra:
    '''Classe com o nome, categoria, duração, autor e ano de lançamento'''
    obras = []

    def __init__ (self, nome, categoria, duracao, ano, diretor, classificacao):
        self.nome = nome
        self.categoria = categoria
        self._classificacao = classificacao
        self.duracao = duracao
        self.ano = ano
        self.diretor = diretor
        Obra.obras.append(self)

    @classmethod
    def listar_obras(cls):
        print("\nLista de obras cadastradas:\n")
        print('★ ' * 20) 
        for obra in cls.obras: 

            print()
            print(f"Nome: {obra.nome}")
            print(f"Categoria: {obra.categoria}")
            print(f"Classificação: {obra.classificacao}")
            print(f"Duração: {obra.duracao} minutos")
            print(f"Ano: {obra.ano}")
            print(f"Diretor(a): {obra.diretor}")
            print()
            print('★ ' * 20)

        voltar_ao_menu_principal()

    @property
    def classificacao(self):
        if self._classificacao.lower() == 'livre':
            return 'Livre (para todos os públicos)'
        return f'{self._classificacao} anos'

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def finalizar_app():
    print('Saindo do programa. Até mais!')

def adicionar_obras():
    nome = input('Digite o nome da obra: ')
    categoria = input('Informe a categoria da obra: ')
    classificacao = input ('Informe a classificação da obra: ')
    duracao = input ('Informe a duração da obra: ')
    ano = input ('Informe o ano de lançamento da obra: ')
    diretor = input ('Informe o nome do Diretor(a) da obra: ')

    nova_obra = Obra(nome, categoria, duracao, ano, diretor, classificacao)
    print(f'\nObra "{nome}" adicionada com sucesso!')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            adicionar_obras()
        elif opcao_escolhida == 2: 
            Obra.listar_obras()
        elif opcao_escolhida == 3:
            finalizar_app()
            sys.exit()
        else:
            opcao_invalida()
    except SystemExit:
        raise  # deixa passar para sair do programa
    except:
        opcao_invalida()

#exemplo de obra
filme1 = Obra(
    nome='Coraline',                   
    categoria='Animação',              
    duracao='100',                
    ano='2009',                      
    diretor='Henry Selick',           
    classificacao='Livre',
)

if __name__ == '__main__':
    main()