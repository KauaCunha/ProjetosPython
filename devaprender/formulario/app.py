import PySimpleGUI as sg

class TelaPython:
	def __init__(self):
		sg.change_look_and_feel('DefaultNoMoreNagging')
		#layout
		layout = [
			[sg.Text('Nome',size=(5,0)),sg.Input(size=(50,0),key='nome')],
			[sg.Text('Idade',size=(5,0)),sg.Input(size=(50,0),key='idade')],
			
			[sg.Text('Quais provedores de e-mail são aceitos?')],
			[sg.Checkbox('Gmail',key='gmail'),
			sg.Checkbox('Outlook',key='outlook'),
			sg.Checkbox('Yahoo',key='yahoo'),
			sg.Checkbox('Nenhum/Outro',key='nenhumOuOutro')],
			
			[sg.Text('Aceita cartão?')],
			[sg.Radio('Sim','cartões',key='aceitaCartao'),
			sg.Radio('Não','cartões',key='naoAceitaCartao')],
			
			[sg.Button('Enviar dados')],
			
			[sg.Output(size=(55,8))]
			
			
		]
		
		#janela			
		self.janela = sg.Window("Dados do Usuário").layout(layout)
		
		
		
		
	def Iniciar(self):
		while True:
			#extrair os dados da janela
			self.Button,self.values = self.janela.Read()
			nome = self.values['nome']
			idade = self.values['idade']
			aceita_gmail = self.values['gmail']
			aceita_outlook = self.values['outlook']
			aceita_yahoo = self.values['yahoo']
			aceita_cartao = self.values['aceitaCartao']
			nenhum_ou_outro = self.values['nenhumOuOutro']
			nao_aceita_cartao = self.values['naoAceitaCartao']
			print(f'nome: {nome}')
			print(f'idade: {idade}')
			print(f'aceita gmail: {aceita_gmail}')
			print(f'aceita outlook: {aceita_outlook}')
			print(f'aceita yahoo: {aceita_yahoo}')
			print(f'Outros ou Nenhum? {nenhum_ou_outro}')
			if( self.values['aceitaCartao'] == True ):
				print(f'aceita cartão: Sim')
			else:
				print(f'aceita cartão: Não')
		
		
tela = TelaPython()
tela.Iniciar()







