import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!", size=15, weight=ft.FontWeight.W_800)
    resposta_correta = "Garfield"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "PARABÉNS! RESPOSTA CORRETA :)"
        else:
            mensagem.value = "RESPOSTA ERRADA..."
        page.update()

    page.title = "Game: Adivinha a Imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.bgcolor="#f7927c"

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a Imagem",
                    size=24,
                    weight=ft.FontWeight.W_800
                ),
                ft.Text(
                    "Qual é o nome do personagem?",
                    size=20,
                    weight=ft.FontWeight.W_800,
                    bgcolor="orange"
                ),
                ft.Image(
                    src="images/garfield.jpg",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="John Arbuckle",
                            on_click=verificar_resposta,
                            bgcolor="#f7ba7c",
                            color="black"
                        ),
                        ft.Button(
                            content="Odie",
                            on_click=verificar_resposta,
                            bgcolor="#f7ba7c",
                            color="black"
                        ),
                        ft.Button(
                            content="Garfield",
                            on_click=verificar_resposta,
                            bgcolor="#f7ba7c",
                            color="black"
                        )
                    ],
                    # Alinhar os filhos da LINHA:
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            # Elementos filhos da COLUNA também vão para o centro:
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)