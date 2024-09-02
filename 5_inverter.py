"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;


"""

def inverter_string(texto):

  string_invertida = ""
  for i in range(len(texto) - 1, -1, -1):
    string_invertida += texto[i]
  return string_invertida

# Entrada da string
texto = input("Digite uma string: ")

# Invertendo a string
string_invertida = inverter_string(texto)

# Imprimindo o resultado
print(f"A string invertida é: {string_invertida}")