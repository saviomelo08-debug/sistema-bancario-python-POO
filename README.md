# sistema-bancario-python-POO
Pastas (banco/, clientes/, contas/, operacoes/): Representam os pacotes lógicos exigidos .

Arquivos __init__.py: criei esse arquivo dentro de cada uma das quatro pastas. É um critério do Python para reconhecer que aquele diretório não é apenas uma pasta comum, mas sim um "pacote" do qual você pode importar códigos.

Arquivos das Classes (conta.py, cliente.py, etc): Cada arquivo contém exclusivamente a classe correspondente ao seu nome. Essa separação garante que o projeto atenda diretamente à regra de não usar apenas um único arquivo para o código-fonte.

Arquivos na Raiz: O main.py e o README.md devem ficar soltos na pasta principal. O main.py servirá como o ponto de partida do programa, importando os pacotes e rodando o menu do terminal , enquanto o README.md conterá o texto de documentação e as instruções de execução do projeto

# Conceitos de POO Aplicados
- **Pacotes:** Separação lógica em `banco`, `clientes`, `contas` e `operacoes`.
- **Encapsulamento:** Saldo da conta protegido (`__saldo`).
- **Herança:** `ContaCorrente` e `ContaPoupanca` herdam da classe base `Conta`.
- **Polimorfismo:** Método `sacar()` possui regras diferentes para cada tipo de conta.
- **Composição:** A `Conta` possui e gerencia diretamente o seu `Historico`.
- **Agregação:** A classe `Banco` armazena múltiplas `Contas`.