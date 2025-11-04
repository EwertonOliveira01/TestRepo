class Usuario:
  '''Cria um usuário e suas informações'''

  def __init__(self, primeiro_nome, ultimo_nome, idade, nacionalidade):
    ''''Recebe um nome e sobrenome'''
    self.primeiro_nome = primeiro_nome
    self.ultimo_nome = ultimo_nome
    self.idade = idade
    self.nacionalidade = nacionalidade

  def descricao_usuario(self):
    nome = f'{self.primeiro_nome} {self.ultimo_nome}'
    print(f'\nO(a) {nome.title()} possui {self.idade} anos e nasceu no {self.nacionalidade.title()}.')

  def cumprimento(self):
    nome = f'{self.primeiro_nome} {self.ultimo_nome}'
    print(f'Olá {nome.title()}.')

class Privileges:
    '''Cria uma classe separada de privilégios'''


    def __init__(self, privilegios=[]):
      self.privilegios = privilegios

    def mostrar_privilegios(self):
      print('\nPrivilégios:')
      for privilegio in self.privilegios:
        print(f'\n- {privilegio.title()}')


class Admin(Usuario):
    '''Cria um administrador'''


    def __init__(self, primeiro_nome, ultimo_nome, idade, nacionalidade):
      super().__init__(primeiro_nome, ultimo_nome, idade, nacionalidade)
      self.privi = Privileges()