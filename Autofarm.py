import PySimpleGUI as Psg
import pause
import webbrowser
from pynput.keyboard import Key, Controller

brows = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAYCAMAAAA4a6b0AAAB6VBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABoapWh' \
        'AAAAo3RSTlMAKoG/5fTu06FWB7Tslm3t/Kd0yOZqA3oLG9tm4m88ysMZiNkpEIDHPyTkXQSK3h8XAraaMDd81Qwm9' \
        '6iCpPnF3+uVr7CJpYum3Jsc7xqDfhLxuSAFvk5BeDklddc15yE2UMaxbFKMhdoGUZjdqzGS6WQPXPByeX3oNL0Uwm' \
        'LA4VNITWjYqroIzFTRaw3WcDtnn1qzKyNgFQrjdkctjgE6uM5VQkgeAwAAAc5JREFUeJxjgAJGJmYWVjZ2Dk4umAh' \
        'UnJuHl49fQEBQSFhEVAxJgo9NXEJSiklYWkaWQU5eQREuoaSswqDKrsagrqGppc2go6unD5UQVTZgMDQyZgDKMJjw' \
        'mDIwmJlbgCUsraxtbGztlGxstDhsbOwdbGxsHJ3AMs4urq5uVu6urq4sHkBCwRNI8KiAtPAAtXrpgtQATWNg8PbxZ' \
        'WDwA5rN4A/UGRBoAJIJ0gSRxmoMDMFsIQwMoWEMDNrcYHPDGSMidRiiooHMmFgGhrh4BgZeIbBMQqJPEn9yiiWQyZ' \
        'TKwCCQlp6e4ZwOAtyZLFGqWbxSDtmpqkBZkExOLlhGK88mH6Q3Xjq3wL4QbJpbIdg0dQ1J/iKI78WKS8AuiAY5Eux' \
        'qt1IwK7NMJouhnBcY1BWZUJnKHHBIV1VVQ31aUwvzaV0WiBVZ3wANnSAWYJCAQqexqQ5oeDODZksKKERbbWzaCoAB' \
        'CQzRWsMYk3aWDnfDzi6gpm4pRYae3j6wab79EyZOEpRwmayVAI45qSkMU0WmAWWms/fNmBkjxyA2azY0tn3MLOaIp' \
        'Khr986dJzEfZDkcqHDzZ4uz2tktEBJeKIGaeBgYbZi1QKlqETxVAQBoal828ps5DgAAAABJRU5ErkJggg=='

lgrid = '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'

chand = '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' \
        'AAABH1L3NAAAAABJRU5ErkJggg=='

p1s1g = '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'

sorow = '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'

loop = 0
cancel_loop = 0
punch_wait = 0
punch_time = 0
keyboards = Controller()

Psg.theme('LightGreen10')

layout = [[Psg.Text("Welcome to David0J's auto-farming menu!")],
          [Psg.Text("Farming:")],
          [Psg.Button(image_data=lgrid, button_color=(Psg.theme_background_color(), Psg.theme_background_color()),
                      border_width=0, key='Laser Grids'),
           Psg.Button(image_data=chand, button_color=(Psg.theme_background_color(), Psg.theme_background_color()),
                      border_width=0, key='Chandeliers'),
           Psg.Button(image_data=p1s1g, button_color=(Psg.theme_background_color(), Psg.theme_background_color()),
                      border_width=0, key='Grass/Pepper/Sugar')],
          [Psg.Text("Harvesting:")],
          [Psg.Button(image_data=sorow, button_color=(Psg.theme_background_color(), Psg.theme_background_color()),
                      border_width=0, key='Harvesting With Sorrow')],
          [Psg.Button("Tutorial"), Psg.Button('', image_data=brows, button_color=(Psg.theme_background_color(),
                                                                                  Psg.theme_background_color()),
                                              border_width=0,
                                              key='web')],
          [Psg.Button("Close")]]

window = Psg.Window("Auto-Farmer", font="Arial, 12", grab_anywhere=True).Layout(layout)


def cancel():
    if event == "Close":
        pass


def d_press():
    keyboards.press(Key.right)
    pause.milliseconds(punch_time)
    keyboards.release(Key.right)
    pause.milliseconds(punch_wait)
    keyboards.release(Key.space)
    return event


def space_press():
    keyboards.press(Key.space)
    pause.milliseconds(1)


def movement():
    d_press()
    space_press()


while True:
    event, values = window.read()
    if event == Psg.WIN_CLOSED:
        break
    if event == "Close":
        break
    if event == "Chandeliers":
        punch_wait = 300
        punch_time = 70
        loop = 1
    if event == "Grass/Pepper/Sugar":
        punch_wait = 300
        punch_time = 100
        loop = 1
    if event == "Laser Grids":
        punch_wait = 300
        punch_time = 85
        loop = 1
    if event == "Harvesting With Sorrow":
        punch_wait = 0
        punch_time = 500
        loop = 1
    if event == 'web':
        webbrowser.open(r'gtauto.ga')
    if event == 'Tutorial':
        webbrowser.open_new('youtube.com')
    while loop == 1:
        movement()
        cancel()
