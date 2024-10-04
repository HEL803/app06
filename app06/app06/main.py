import flet as ft
import random




#fuincion principal
def main(page: ft.Page):
    #variables globales
    global numero_secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title="adivina el numero"
    
    #generar un numero aleatorio
    numero_secreto=random.randint(1,100)
    
    #crear elementos de la interfaz
    titulo=ft.Text("adivina el numero entre 1 y 100",size=20,color="red")
    entrada_numero=ft.TextField(label="tu adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("adivinar")
    texto_resultado=ft.Text("",color="red")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        bgcolor="blue",
        width=page.window.width,
        height=page.window.height,
        padding=20
            
        
    )
    page.add(contenedor_principal)


ft.app(main)
