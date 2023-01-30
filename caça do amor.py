from time import sleep
enigma1 = 333666
enigma2 = 'gigante de taparacá' # 19°56’56.88″S, 69°38’1.87″W.
enigma3 = 'bicho préguiça'
enigma4 = 'banguela'
enigma5 = 4257040
#tela inicial
print('💝🦥'*34)

print('Bem-vinda ao {}CAÇA DO AMOR{}, amorzinho.'.format('\33[31m','\33[m'))
data = float(input('Digite a data mais importante do universo para continuar e, poder ganhar {}recompensas incríveis{}: '.format('\33[4;33m','\33[m'))) # 'digita a senha do programa'
sleep(1) # tempo de espera
if data == 29.03 or data == 2903 or data == 290322:

    print('Parabéns, a data do {}nosso amor, venceu!!!{}'.format('\33[;41m','\33[m'))
else:
    print('Como você pôde errar isso? Estou triste 😭')

print(' ')

sleep(1)

if data == 29.03 or data == 2903 or data == 290322: # etapa dois

    print('{}{}{}'.format('\33[33m' , '-=-'*33 , '\33[m'))
    print('{}ETAPA DOIS!!!{}'.format('\33[1;34m' , '\33[m'))
    print('{}{}{}'.format('\33[33m' , '-=-'*33 , '\33[m'))
    print('                                           {}CARREGANDO...{}'.format('\33[47m' , '\33[m'))
    sleep(2)
    print(' ')
    print('Amor, você deverá, a partir de agora, resolver os enigmas das pistas para encontrar a sua recompensa.\n{}Cada mistério revelado indica o lugar em que o próximo está escondido até chegar no grande prêmio.{}'.format('\33[4;32m' , '\33[m'))

    aceitaContinuar = input('Digite "OK" para continuar: ').lower().strip()

if aceitaContinuar !='ok':
       print('Você desistiu. Achei que me amava!!!💔')
elif aceitaContinuar == 'ok':
    sleep(1)
    print(' ')
    print('{} ENIGMAS {}'.format('-=-' * 15, '-=-' * 15))
    sleep(1)
    print(' ')
    print('{}enigma 1:{}'.format('\33[7m', '\33[m'))
    sleep(1)
    print('Lar dentro lar.\nCabeça vermelha, corpo preto.\nTatuagem representando seu valor.\nQuem é propietário, não o quer. ')

    resposta1 = int(input('Digite o código encontrado no local: '))

    if resposta1 == enigma1:
        print('{}PARABÉNS, AMOR. Você acertou{} e agora partiu para o próximo enigma.'.format('\33[4;36m', '\33[m'))
        sleep(1)

        print('PROCESSANDO...'.format('\33[47m', '\33[m'))

        sleep(2)

        print(' ')
        print('{}enigma 2:{}'.format('\33[7m', '\33[m'))
        sleep(1)
        print(' ')
        sleep(1)
        print('-.-. .- .. -..- .. -. .... .- / -.. . / -.-. --- .-. .-. . .. ---') # = caixinha de correio
        print(' ')

        resposta2 = str(input('Digite sua resposta aqui: ')).lower()

        if resposta2 == enigma2 or resposta2 == 'gigante de taparaca':
            print('{}PARABÉNS, AMOR. Você acertou{} e agora partiu para o próximo enigma.'.format('\33[4;36m', '\33[m'))
            sleep(1)

            print('PROCESSANDO...'.format('\33[47m', '\33[m'))

            sleep(2)

            print(' ')
            print('{}enigma 3:{}'.format('\33[7m', '\33[m'))
            sleep(1)
            print(' ')
            print('{}FOLIVORA{}'.format('\33[4;31m' , '\33[m'))
            print(' ')

            resposta3 = str(input('Digite sua resposta aqui: ')).lower()

            if resposta3 == enigma3 or resposta3 == 'préguiça':
                print('{}PARABÉNS, AMOR. Você acertou{} e agora partiu para o próximo enigma.'.format('\33[4;36m', '\33[m'))
                print('PROCESSANDO...'.format('\33[47m', '\33[m'))

                sleep(2)

                print(' ')
                print('{}enigma 4:{}'.format('\33[7m', '\33[m'))
                sleep(1)
                print(' ')
                print('{}A1Z26{}'.format('\33[7m' , '\33[m'))
                print('=')
                print('3 18 9 1 4 9 1 2 15 12 9 3 1 4 15 18 1 9 15 5 4 1 16 18 15 16 9 1 13 15 18 20 5')

                resposta4 = str(input('Digite sua resposta aqui: ')).lower()

                if resposta4 == enigma4 or resposta4 == 'furia da noite' or resposta4 == 'fúria da noite':
                    print('{}PARABÉNS, AMOR. Você acertou{} e agora partiu para o próximo enigma.'.format('\33[4;36m',
                                                                                                          '\33[m'))
                    print('PROCESSANDO...'.format('\33[47m', '\33[m'))

                    sleep(2)

                    print(' ')
                    print('{}enigma 5:{}'.format('\33[7m', '\33[m'))
                    sleep(1)
                    print(' ')
                    print('1.Orégano\n2.Fogo\n3.Orelha\n4.Risada\n5.Navio')

                    resposta5 = int(input('Digite sua resposta aqui: '))

                    if resposta5 == enigma5:
                        print(' ')
                        print('{}{}{}'.format('\33[33m' , '-=-'*33 , '\33[m'))
                        print(' TOPO - GUARDA - ROUPA')
                        print('{}{}{}'.format('\33[33m' , '-=-'*33 , '\33[m'))
                        sleep(10)
                        print('{}PARABÉNS, AMOR.\nVOCÊ CHEGOU ATÉ O FINAL E ENCONTROU SEU PRÊMIO;\nESPERO QUE TENHA GOSTADO.'.format('\33[4;35m' , '\33[m'))
                        sleep(3)
                        print('{}TE AMO{}{}'.format('\33[4;31m' , '\33[m' , '🤍'))
                        sleep(2)
                        print(' ')
                        print('{}FIM{}'.format('\33[47m' , '\33[m'))
                        print(' ')
                        print('💝🦥'*34)




