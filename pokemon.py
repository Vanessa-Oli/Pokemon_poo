class Pokemon:
    def __init__(self, nome, tipo):
        self._nome = nome  # Encapsulamento
        self._tipo = tipo  # Encapsulamento
    
    @property
    def nome(self):
        return self._nome  # Encapsulamento
    
    @property
    def tipo(self):
        return self._tipo  # Encapsulamento
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome  # Encapsulamento
    
    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo  # Encapsulamento
    
    def atacar(self):
        pass  # Polimorfismo

class Pikachu(Pokemon): # Herança
    def atacar(self):
        return "Pikachu usou o ataque Thunderbolt!"  # Polimorfismo

class Charizard(Pokemon): # Herança
    def atacar(self):
        return "Charizard usou o ataque Flamethrower!"  # Polimorfismo

class Blastoise(Pokemon): # Herança
    def atacar(self):
        return "Blastoise usou o ataque Hydro Pump!"  # Polimorfismo

pikachu = Pikachu("Pikachu", "Elétrico")  # Instância da subclasse Pikachu
charizard = Charizard("Charizard", "Fogo")  # Instância da subclasse Charizard
blastoise = Blastoise("Blastoise", "Água")  # Instância da subclasse Blastoise

pokemons = [pikachu, charizard, blastoise]  # Lista polimórfica contendo instâncias de diferentes subclasses

for pokemon in pokemons:
    print(pokemon.atacar())  # Polimorfismo - cada instância chama seu próprio método atacar
