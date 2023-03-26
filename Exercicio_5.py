# Definindo a string a ser invertida
string = "Exemplo de string para inverter"

# Criando uma pilha vazia
pilha = []

# Adicionando cada caractere da string na pilha
for i in range(len(string)):
    pilha.append(string[i])

# Criando uma nova string com os caracteres invertidos
nova_string = ""
while len(pilha) > 0:
    nova_string += pilha.pop()

# Imprimindo a nova string
print(nova_string)