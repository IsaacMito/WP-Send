import pyautogui

icon_pesq = r'util/icons/icon_pesq.png'
icon_pesq_voltar = r'util/icons/icon_pesq_voltar.png'

def get_posicao_pesq():

    local = pyautogui.locateOnScreen(icon_pesq, grayscale=True)

    if local is None:
        local = pyautogui.locateOnScreen(icon_pesq_voltar, grayscale=True)

    return local
