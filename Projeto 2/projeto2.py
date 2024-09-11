#importando as bibliotecas
import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

# pergunto os inputs que vou colocar nos códigos
ação = input("Digite o nome da ação: ")
data_inicial = input("Digite a data inicial da busca: ")
data_final = input("Digite a data final da busca: ")

# defino o código para puxar os dados que preciso
dados = yfinance.Ticker(ação)

# defino o código para gerar a tabela
tabela = dados.history(start=data_inicial, end=data_final)

# defino que quero apenas os dados de fechamento, close, da tabela
fechamento = tabela.Close

# como os dados estão com muitas casas decimais, uso um código para arredondá-los
máxima = round(fechamento.max(), 2)
mínima = round(fechamento.min(), 2)
média = round(fechamento.mean(), 2)

# definindo variáveis para a preparação do email
destinatário = "alvinopf@gmail.com"
assunto = "Análises do Projeto 2"
mensagem = f"""
Bom dia,

Segue abaixo as análises da ação {ação} no período solicitado {data_inicial} à {data_final}:

Cotação máxima: R${máxima}
Cotação mínima: R${mínima}
Cotação média: R${média}

Obrigado pela atenção e sigo à disposição.

Atenciosamente,
"""

# passo - abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(5)

# definindo uma pausa de 3 segundos entre as ações
pyautogui.PAUSE = 3

# passo - clicar no botão escrever
pyautogui.click(x=67, y=208)

#passo - digitar o email do destinatário e clicar em tab
pyperclip.copy(destinatário)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#passo - digitar o assunto do email e clicar em tab
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#passo - digitar a mensagem do email e clicar em enviar
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=843, y=692)

# passo - fechar a aba
pyautogui.hotkey("ctrl", "f4")

print("Email enviado com sucesso.")