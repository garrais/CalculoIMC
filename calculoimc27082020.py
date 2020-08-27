print ('Desenvolvido por Gabriel Degarrais')
peso = float(input('Qual é seu peso (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('0 IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5: 
    print ('Parabéns você está no peso ideal')
elif 18.5 <= imc < 25:
    print ('PARABÉNS, Você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print ('você está em SOBREPESO')
elif 30 <= imc < 40: 
    print ('você está OBESO')
elif imc >= 40:
    print ('você está com OBESIDADE MÓRBIDA')
print ('Obrigado por testar o Aplicativo.')
