#Titulo Nattzap
#Botão Iniciar
    #Pop Up
        #Bem vindo ao Nattzap 
        #Escreva seu nome
        #Entrar no chat
#Chat
    #Usuário entrou no chat
    #Mensagem do usuário
#Campo para enviar mensagem
#Botão de enviar

#Passo  - Importar o flet
import flet as ft 


#Passo 2- Criar uma função
def main(pagina):

    pagina.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.PINK,
            primary_container=ft.colors.PINK_300
            
        ),
    )

    logo =  ft.Image("logozap.png")

    titulo = ft.Text("Chat Nattzap")

    nome_usuario = ft.TextField(label="Escreva seu nome")


    chat = ft.Column()
    
    #Função do tunel
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    #Para criar o tunel
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
      

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        
        #Qdo o usuário clicar em enviar mensagem ENVIAR para o tunel a mensagem para todos verem
        pagina.pubsub.send_all(texto_campo_mensagem)

        #Limpar o campo da mensagem após enviar a mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui:", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)


    def entrar_chat(evento):
        #Fechar o PopUp
        popup.open = False
        #Tirar o titulo
        pagina.remove(titulo)
        #Tire o botão Iniciar Chat da tela
        pagina.remove(botao_iniciar)        
        #Adicionar o Chat
        pagina.add(chat)
        #Crie o campo de enviar mensagem e botão de enviar mensagem um na frente do outro.
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )

        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)

        pagina.update()

  
    popup =ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Chat Nattzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)])
    #title - é o título do PopUp, content - é o conteúdo dele e actions - são as ações dele.


    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        #Sempre editar uma página dentro de uma função, tem que escrever "pagina.update()" para atualizar a página
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Inciar Chat", on_click=iniciar_chat)



    pagina.add(logo)
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    





    

#Passo 3 - Diz qual é a função
    
#ft.app(main, view=ft.WEB_BROWSER)
ft.app(main)

