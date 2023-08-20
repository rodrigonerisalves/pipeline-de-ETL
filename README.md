# Pipeline de ETL com Python

Desafio de projeto Explorando IA Generativa em um Pipeline de ETL com Python

## 🚀 Começando


### 📋 Pré-requisitos

Em resumo, a biblioteca csv é uma ótima opção para lidar com arquivos CSV, enquanto a biblioteca time é essencial para controlar o tempo de execução e criar atrasos em seu código Python.

```
import csv import time
```

### 🔧 Instalação

Portanto, você não precisa usar o comando "pip install time" para instalá-la. Ela já está disponível para uso em qualquer instalação padrão do Python.

#### Função de Limpar o Arquivo

```python
def limpar_arquivo():
    with open('campanha.csv', 'w', newline='') as arquivo_csv:
        arquivo_csv.truncate()
```

A função `limpar_arquivo()` é responsável por limpar o conteúdo do arquivo "campanha.csv" antes de cadastrar novos clientes. Ela utiliza a função `truncate()` para apagar o conteúdo do arquivo.

#### Função de Cadastrar Clientes

```python
def cadastrar_cliente():
    contador = 1
    clientes = []

    while contador <= 3:
        nome = input(f"Cadastre o cliente {contador}: ")

        if nome.isalpha() or nome.isspace():
            clientes.append([nome])
            contador += 1
        else:
            print("ATENÇÃO! Opção inválida, digite apenas primeiro nome.")

    with open('campanha.csv', 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(clientes)

    print("Todos clientes cadastrados com sucesso!")
```

A função `cadastrar_cliente()` permite cadastrar até 3 clientes para receber a campanha. Ela utiliza um loop `while` para solicitar o nome de cada cliente e realizar algumas verificações antes de adicioná-los à lista `clientes`. Essa lista é então gravada no arquivo "campanha.csv" utilizando a função `writerows()` do módulo `csv`.

#### Função de Enviar Campanha

```python
def enviar_campanha(mensagem):
    with open('campanha.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        nomes = [row[0] for row in reader]

        if mensagem == 1:
            for nome in nomes:
                print(f"{nome}! Invista hoje para um futuro ser seguro e estável!, {nome}! Seu futuro financeiro depende disso!")
        elif mensagem == 2:
            for nome in nomes:
                print(f"Oi, {nome}! Investir cérto é a chave para multiplicar seu dinheiro. Não deixe sua grana parada!")
        elif mensagem == 3:
            for nome in nomes:
                print(f"Invista hoje para garantir um futuro seguro e próspero. {nome}! Seu futuro agradece!")

    print("\nCampanha enviada com sucesso! Santander Agradece...")
    time.sleep(5)
```

A função `enviar_campanha()` recebe como parâmetro a mensagem a ser enviada (1, 2 ou 3). Ela lê o arquivo "campanha.csv" utilizando a função `reader()` do módulo `csv` e armazena os nomes dos clientes em uma lista. Em seguida, ela imprime a mensagem correspondente para cada cliente, utilizando o nome deles. Por fim, exibe uma mensagem informando que a campanha foi enviada com sucesso e aguarda 5 segundos antes de retornar.

Espero que essa apresentação tenha sido útil para entender o funcionamento do sistema de envio de mensagem de campanha Santander. 

## 📦 Implantação

Adicione notas adicionais sobre como implantar

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Visual Studio Code](https://code.visualstudio.com/download) - Editor


## ✒️ Autores


* **Rodrigo Neris** -  [*Trabalho Inicial*](https://github.com/rodrigonerisalves)
---
⌨️ com ❤️ por [Rodrigo Neris](www.linkedin.com/in/rodrigo-neris) 😊