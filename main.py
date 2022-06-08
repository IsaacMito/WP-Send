from util.excel import Excel
from util.send import Send

mensagem = """❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️

*DIA DOS NAMORADOS*
*CALCE PERFEITO* 

*Presentes a partir* 
*de R$ 99,99*  😱😍

Várias opções:
Sapato, Bolsa, Scarpin, 
Tênis, Bijus e muito mais 
🥿👠👡👢👞

Na Calce você ainda encontra:
✅ Melhores marcas: Usaflex, Democrata, Piccadilly, Opananken e Skechers;
✅ Suas compras em até 10x sem juros.

Venha tomar um *delicioso café* conosco e saia daqui com seu presente prontinho.
🎁🍾🥂"""

cod_campanha = 9

excel = Excel(r'C:\Users\DEV\Documents\Received Files\AsaNorte.xlsx')

send = Send(excel, mensagem, cod_campanha)

send.run()