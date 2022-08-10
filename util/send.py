import subprocess
import time

import clipboard
import pyautogui
from cv2 import cv2
import numpy
import numpy as np

from util import icon
from util.bss import Bss
from util.excel import Excel


class Send:

    def __init__(self, excel: Excel, mensagem: str, cod_campanha, sleep=0.1):
        self.bss = Bss()
        self.excel = excel
        self.mensagem: str = mensagem
        self.sleep = sleep
        self.cod_campanha = cod_campanha

    def run(self):

        for row in range(1, self.excel.max_row + 1):

            celular = self.excel.get_celular(row)
            nome = self.excel.get_nome(row)
            status = self.excel.get_status(row)

            entity = self.bss.get_entity("619" + celular, self.cod_campanha)

            if status is None and len(entity) == 0:

                self.validaTela()

                if self.pesquisar(celular):

                    self.mensagem = self.mensagem.replace('{nome}', nome)

                    self.colar(self.mensagem)
                    pyautogui.press("enter")

                    self.bss.create("619" + celular, self.cod_campanha)
                    self.excel.set_status('Enviado', row)
                else:
                    self.excel.set_status('Nao encontrado', row)
            else:
                self.excel.set_status('Já enviado', row)

            self.excel.salvar()
            time.sleep(self.sleep)

    def pesquisar(self, celular: str):

        posicao_pesq = icon.get_posicao_pesq()

        pyautogui.moveTo(posicao_pesq)
        pyautogui.move(50, 0)
        pyautogui.click()

        pyautogui.hotkey("ctrl", "a")
        self.colar(celular)
        time.sleep(0.5)

        pyautogui.press("enter")
        time.sleep(0.5)

        return self.verificaContato(posicao_pesq)

    def validaTela(self):

        if (icon.get_posicao_pesq() is None):
            subprocess.call(r'C:\Users\DEV\AppData\Local\WhatsApp\WhatsApp.exe')

        while True:
            if (icon.get_posicao_pesq() is not None):
                break
            time.sleep(0.1)

    def colar(self, str):
        clipboard.copy(str)
        pyautogui.hotkey("ctrl", "v")

    def verificaContato(self, posicao):

        pyautogui.screenshot(region=[posicao.left, posicao.top + 40, 350, 150]).save("img_com_pesq.png")
        time.sleep(0.1)

        img1 = cv2.imread("img_com_pesq.png", 0)
        img2 = cv2.imread("img_compare.png", 0)

        t = cv2.absdiff(img1, img2)
        res = t.astype(np.uint8)
        porcent = (numpy.count_nonzero(res) * 100) / res.size

        if porcent > 8:
            return True
        else:
            return False
