import flet as ft

def main(page):
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):  # Função que recebe mensagens do túnel
        chat.controls.append(ft.Text(mensagem))
        page.update()
        
    page.pubsub.subscribe(enviar_mensagem_tunel)  # Cria túnel de comunicação

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    
    chat = ft.Column()

    nome_usuario = None  # Variável para armazenar o nome do usuário

    def enviar_mensagem(evento):
        nonlocal nome_usuario
        texto = f"{nome_usuario}: {texto_mensagem.value}"
        page.pubsub.send_all(texto)  # Envia mensagem no túnel
        texto_mensagem.value = ""
        page.update()
        texto_mensagem.focus()  # Volta o foco para o campo de texto

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        nonlocal nome_usuario
        nome_usuario = campo_nome_usuario.value
        page.remove(titulo)
        page.remove(botao_iniciar)
        janela.open = False
        page.add(chat)
        page.add(linha_mensagem)

        texto_entrou_chat = f"{nome_usuario} entrou no chat"
        page.pubsub.send_all(texto_entrou_chat)  # Envia mensagem de entrada no túnel
        page.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def abrir_popup(evento):
        page.dialog = janela
        janela.open = True
        page.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    page.add(titulo)
    page.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER)