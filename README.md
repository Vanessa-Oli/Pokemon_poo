
<p align="center">
  <img src="https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/logo_horizontal_univasso.svg" alt="Logo da Universidade">
</p>

# Pokémon 

## 👩‍🎓 Aluna
- Vanessa Christiano de Oliveira  - 201920957

## 📚 Disciplina

- Engenharia de Software Experimental
- Fabricio Tadeu Dias
- 3 Período 

## Explicando o conceito:
- Este é um exemplo de código em Python que implementa um jogo Pokémon simples, demonstrando os conceitos de polimorfismo, herança e encapsulamento.
## Polimorfismo
- Polimorfismo é um conceito da programação orientada a objetos que permite que objetos de diferentes classes sejam tratados de forma uniforme. Isso significa que um objeto pode ser referenciado por um tipo mais genérico (por exemplo, a classe base), mas ainda pode executar seu próprio comportamento específico (por meio de um método com o mesmo nome) de acordo com sua implementação na classe específica. O polimorfismo facilita a extensibilidade e a flexibilidade do código.

## Herança
- A herança é um conceito fundamental da programação orientada a objetos que permite que uma classe herde atributos e métodos de outra classe, conhecida como classe base ou superclasse. A classe que herda é chamada de classe derivada ou subclasse. A herança permite que a subclasse reutilize e estenda o comportamento da superclasse, adicionando seus próprios atributos e métodos. Isso promove a reutilização de código e ajuda a organizar as classes em uma hierarquia, representando relacionamentos de "é um" entre as classes.

## Encapsulamento
- O encapsulamento é um princípio da programação orientada a objetos que combina dados (atributos) e métodos que operam nesses dados dentro de uma única unidade chamada classe. O encapsulamento protege os dados, restringindo o acesso direto a eles e fornecendo métodos públicos (getters e setters) para interagir com esses dados. Dessa forma, o encapsulamento promove a segurança dos dados e facilita a manutenção e o gerenciamento do código, pois os detalhes internos dos dados podem ser ocultados e controlados pela classe.
## Estrutura do código

O código está organizado da seguinte maneira:

- A classe base `Pokemon` define os atributos básicos de um Pokémon, como nome e tipo. Ela também implementa os métodos getter e setter usando decoradores `@property` e `@nome.setter` / `@tipo.setter` para controlar o acesso aos atributos.

- As subclasses `Pikachu`, `Charizard` e `Blastoise` herdam da classe `Pokemon` e implementam o método `atacar()` com comportamentos específicos para cada Pokémon.

- O programa principal cria instâncias de cada Pokémon e as armazena em uma lista chamada `pokemons`. Em seguida, um loop `for` é usado para chamar o método `atacar()` de cada Pokémon e exibir a mensagem de ataque correspondente.

## Polimorfismo

O polimorfismo é demonstrado no código quando chamamos o método `atacar()` em cada instância de Pokémon. Mesmo que todos os Pokémon sejam da classe base `Pokemon`, cada um deles executa sua própria implementação do método `atacar()`, fornecendo um comportamento de ataque específico.

## Herança

A herança é usada no código para criar as subclasses `Pikachu`, `Charizard` e `Blastoise`, que herdam os atributos e métodos da classe base `Pokemon`. Essas subclasses especializam os Pokémon específicos, adicionando suas próprias implementações do método `atacar()`.

## Encapsulamento

O encapsulamento é aplicado no código por meio da definição dos atributos `_nome` e `_tipo` como privados na classe base `Pokemon`. O acesso a esses atributos é feito por meio dos métodos getter e setter, garantindo um controle adequado sobre a manipulação dos dados.