frase = input('Digite uma frase: ').lower().strip()
print('sua frase possui', frase.count('a'), 'a letra "a"')
print('ela aparece, pela primeira vez, na {}° casa'.format(frase.find('a')+1))
print('ela aparece, pela última vez, na {}° casa'.format(frase.rfind('a')+1))
