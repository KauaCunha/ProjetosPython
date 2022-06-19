import PySimpleGUI as sg

#Criar as janelas e estilos
def janela_login():
	layout = [
		[sg.Text('Nome')],
		[sg.Input()],
		[sg.Button('Continuar')]
	]
	return sg.Window('Login', layout,finalize=True)
	
def janela_pedido():
	layout = [
		[sg.Text('Fazer pedido')],
		[sg.Checkbox('Calabresa',key='pizza1'), 
		 sg.Checkbox('Portuguesa',key='pizza2')],
		[sg.Button('Voltar'),sg.Button('Fazer Pedido')]
	]
	return sg.Window('Montar Pedido', layout,finalize=True)
	
#Criar as janelas iniciais
janela1,janela2 = janela_login(), None

#Criar um loop de leitura de eventos
while True:
	window,event,values = sg.read_all_windows()
	#Quando a janela for fechada
	if window == janela1 and event == sg.WIN_CLOSED:
		break
	if window == janela2 and event == sg.WIN_CLOSED:
		break
	#Quando queremos ir para outra janela
	if window == janela1 and event == 'Continuar':
		janela2 = janela_pedido()
		janela1.hide()
	if window == janela2 and event == 'Voltar':
		janela2.hide()
		janela1.un_hide()
	#Lógica de o que deve acontecer ao clicar nos botões
	if window == janela2 and event == 'Fazer Pedido':
		if values['pizza1'] == True and values['pizza2'] == True:
			sg.popup('Foram solicitados uma pizza de calabresa e uma de portuguesa')
		elif values['pizza1'] == True:
			sg.popup('Foram solicitados uma pizza de calabresa')
		elif values['pizza2'] == True:
			sg.popup('Foram solicitados uma pizza de portuguesa')
	





