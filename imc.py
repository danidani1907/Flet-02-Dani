# Calculadora de IMC - Versão Renovada
import flet as ft

def main(page: ft.Page):
    page.title = "IMC Fácil"
    page.padding = ft.padding.all(30)
    page.theme_mode = ft.ThemeMode.LIGHT

    # Campos de entrada
    campo_peso = ft.TextField(label="Peso (kg) ⚖️", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    campo_altura = ft.TextField(label="Altura (m) 📏", width=200, keyboard_type=ft.KeyboardType.NUMBER)

    # Texto de resultado
    texto_resultado = ft.Text(
        "Insira os valores e pressione 'Calcular'",
        size=18,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLUE_GREY
    )

    # Função de cálculo
    def calcular_imc(e):
        try:
            p = float(campo_peso.value)
            a = float(campo_altura.value)
            if a <= 0:
                texto_resultado.value = "⚠️ Altura inválida!"
                texto_resultado.color = ft.Colors.RED
            else:
                imc = p / (a * a)
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                    cor = ft.Colors.ORANGE_400
                elif 18.5 <= imc < 25:
                    classificacao = "Peso normal"
                    cor = ft.Colors.GREEN_700
                elif 25 <= imc < 30:
                    classificacao = "Sobrepeso"
                    cor = ft.Colors.YELLOW_800
                else:
                    classificacao = "Obesidade"
                    cor = ft.Colors.RED_700
                texto_resultado.value = f"📊 IMC: {imc:.2f} → {classificacao}"
                texto_resultado.color = cor
        except ValueError:
            texto_resultado.value = "⚠️ Digite números válidos!"
            texto_resultado.color = ft.Colors.RED
        page.update()

    # Alternar tema
    def alternar_tema(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.appbar = criar_appbar()
        page.update()

    # AppBar personalizada
    def criar_appbar():
        cor_texto = ft.Colors.BLACK if page.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.WHITE
        return ft.AppBar(
            leading=ft.Icon(ft.Icons.FAVORITE, color=cor_texto),
            title=ft.Text("IMC Fácil", color=cor_texto),
            bgcolor=ft.Colors.CYAN_100,
            actions=[
                ft.Row(
                    controls=[
                        ft.Text("🌙", color=cor_texto),
                        ft.Switch(value=(page.theme_mode == ft.ThemeMode.DARK), on_change=alternar_tema),
                        ft.Text("☀️", color=cor_texto),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )

    page.appbar = criar_appbar()

    # Função limpar campos
    def limpar(e):
        campo_peso.value = ""
        campo_altura.value = ""
        texto_resultado.value = "Insira os valores e pressione 'Calcular'"
        texto_resultado.color = ft.Colors.BLUE_GREY
        page.update()

    # Layout principal
    page.add(
        ft.Column([
            ft.Text("🧮 IMC Fácil", size=26, weight=ft.FontWeight.BOLD),
            campo_altura,
            campo_peso,
            ft.Row([
                ft.ElevatedButton("Calcular ✅", on_click=calcular_imc, width=150, bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE),
                ft.ElevatedButton("Limpar 🧹", on_click=limpar, width=150, bgcolor=ft.Colors.GREY_500, color=ft.Colors.WHITE)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Divider(),
            texto_resultado
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
    )

ft.app(target=main)
