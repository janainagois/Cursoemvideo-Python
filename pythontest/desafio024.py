#ler um nome da cidade e dizer se começa com SANTO

cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')






'''if cidade = SANTO,
    print('Sua cidade começa com SANTO!')
else cidade != SANTO,
    print('Sua cidade não começa com SANTO!')'''