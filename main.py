# # Taxa de variação do tempo de descarga
# variacao_taxa_descarga = 5

# # Dados de saída do inversor
# tensao_inversor = 127
# corrente_inversor = 3.937

# # Dados da bateria
# capacidade_bateria = 100
# volt_bateria = 48

# # Formulá de Cálculo
# potencia_inversor = (tensao_inversor * corrente_inversor) * 1
# potencia_bateria = (capacidade_bateria * volt_bateria)

# tempo_descarga_hora = potencia_bateria / potencia_inversor

# tempo_descarga_min = tempo_descarga_hora * 60

# taxa_descarga = volt_bateria / tempo_descarga_min

# # Cálcula o valor de referencia da % de variação
# percentual_taxa_descarga = taxa_descarga * variacao_taxa_descarga / 100

# print(f'A taxa de descarga da bateria é igual: {taxa_descarga:.3f}')

# if taxa_descarga >= (0.083 - percentual_taxa_descarga):
#     print('Valor considerado: BOM')

# else:
#     print('Valor considerado: RUIM')


'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()







