import flet as ft
from formula_calculo import calcular, status


def main(page: ft.Page):
    def button_clicked(e):

        tx = calcular(int(tb1.value), float(tb2.value), int(tb3.value), int(tb4.value))

        t1.value = f'A taxa de descarga da bateria: {tx[0]:.3f} volts por minuto'

        t2.value = status(tx[0])

        t3.value = f'Tempo de autonomia para o consumo médio atual {tx[1]:.2f} horas {cg.value}'

        page.update()


    cg = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="1000w", label="Inversor de 1000W"),
                ft.Radio(value="2000w", label="Inversor de 2000W"),
            ]
        )
    )
    
    t1 = ft.Text()
    t2 = ft.Text()
    t3 = ft.Text()
    tb1 = ft.TextField(label="Tensão Saída Inversor", hint_text="Tensão de operação do inversor")
    tb2 = ft.TextField(label="Corrente Saída Inversor", hint_text="Corrente de operação do inversor")
    tb3 = ft.TextField(label="Capacidade da Bateria", hint_text="Capacidade em Ah da bateria")
    tb4 = ft.TextField(label="Voltagem da Bateria", hint_text="Voltagem de operação da bateria")
    b = ft.ElevatedButton(text="Calcular", on_click=button_clicked)
    page.add(cg, tb1, tb2, tb3, tb4, b, t1, t2, t3)

ft.app(target=main)
