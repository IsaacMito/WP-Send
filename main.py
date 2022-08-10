from util.excel import Excel
from util.send import Send

mensagem = """🚨🚨🚨🚨🚨🚨🚨🚨
*DIA DOS PAIS*
*CALCE PERFEITO*

Presentes incríveis 
para o seu pai, veja!

*Mocassim* comfort
*100% couro*
*R$ 99,99* 

Na Calce você ainda encontra:
✅ Carteiras, sapatos, tênis e muito mais;
✅ Suas compras em até 10x sem juros.

Venha tomar um delicioso café conosco e saia daqui com seu presente prontinho.
🎁🍾🥂"""

cod_campanha = 9

excel = Excel(r'C:\Users\DEV\Documents\Received Files\AsaNorte.xlsx')

send = Send(excel, mensagem, cod_campanha)

send.run()