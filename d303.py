#------------ EXEMPLO DE FUNÇÃO ARGS-------------
# def montar_perfil (nome,*args):
#     print (f"Perfil de {nome}:")

#     print ('Características dela:')
#     for item in args:
#         print(item)

# montar_perfil('Bárbara', '21 anos', 'Mora em São Paulo')

# montar_perfil ('Mayara','17 anos', 'Parle françois','tem enxaqueca cronica')





# ----------PROGRAMAÇÃO ORIENTADA A OBJETOS----------------
    #Paradigmas de programação = formas de se pensar códigos, algoritmos
    # programação procedural: escrevver os códigos em sequência.
    # programação orientada a objetos = vms criar objetos que terão características e  ações e vamos trabalhar manipulando os objetos.
    # classe= como se fosse um manual de criar objetos, ela é declarada assim:
#  class Bolo:
#     def __init__(self): 
#         self.sabor = sabor
#         self.qtde_ovos = qtde_ovos
#         self.qtde_andares = qtde_andares
#         formato = 'redondo'

    # -----AÇÕES DO OBJETO-----  
    #  def assar (): 
    #     print('o bolo esta assando')
    #  def servir():
    #     print('o bolo esta servido')    
# sendo a palavra 'Bolo', podendo ser substituida por qualquer palavra iniciada em letra maiuscula
#  o Construtor é necessário quando vamos criar uma classe, e é o construtor da classe que vamos passar cada uma das características definidas no Bolo     

# bolo_chocolate = Bolo ('chocolate',4,1)
# print(bolo_chocolate.sabor)

# bolo_laranja = Bolo ('laranja',2,4)
# print (bolo_laranja.qtde_andares)

# class Carro:
#         qtde_rodas = 4

#         def __init__(self, cor, marca, modelo):
#             self.cor = cor
#             self.marca = marca
#             self.modelo = modelo
    
#     def (buzinar)(self)
#     print('biiiiiiiiiii')
    
#     def (acelerar)(self)
#     print('vromm vrommm')

#     carro

class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
        print('Nhom, nhom')

class Gato(Animal):
    def __init__(self, nome, dono, raca):
        self.raca = raca
        super().__init__(nome, dono)

    def Miar(self):
        print('miaaaaaau')

class Cachorro(Animal):
    def latir(self):
        print('AUAUUAAUAU')

gato = Gato('xuxuzinho', 'matheus', 'siames')
cachorro = Cachorro ('rex','Barbara')
animal=Animal('nome','dono')
