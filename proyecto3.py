# # this project will ask the user to input a text, then the user will be asked to input 3 letter of choice and then the program will process this information to return:
# 1) determine how many times are there each letter in the text
# 2) count all the words within the text
# 3) we will inform the user which is the first and the last letter of the text
# 4) the system will show the text in reverse
# 5) the program will tell us if the word 'python' exist in the text

texto = input('Escribe cualquier texto: ').lower()
letras = list(input('Por favor escribe 3 letras: ').lower())
print('\n')
letras1 = texto.count(letras[0])
letras2 = texto.count(letras[1])
letras3 = texto.count(letras[2])
palabras_totales = texto.split()
palabra = 'python' in texto
palabras_totales.reverse()
texto_alreves = " ".join(palabras_totales)
dic = {True:'si',False:'no'}
print(f'Tu primer letra {letras[0]} se encontro {letras1} veces')
print(f'Tu segunda letra {letras[1]} se encontro {letras2} veces')
print(f'Tu tercer letra {letras[2]} se encontro {letras3} veces')
print('\n')
print(f'La cantidad total de palabras en tu texto es de: {len(palabras_totales)}')
print('\n')
print(f'La primer letra de tu texto es: "{texto[0]}" y la ultima letra de tu texto es "{texto[-1]}"')
print('\n')
print('TU TEXTO AL REVES')
print(f'{texto_alreves}')
print('\n')
print(f'La parlabra "python" {dic[palabra]} se encuentra en tu texto')
print('\n')

print('\n')
print(texto,letras,letras1,letras2,letras3,len(palabras_totales),texto[0],texto[-1],list(texto.split()[::-1]),palabra)