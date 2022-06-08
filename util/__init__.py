import os
from urllib import request
import zipfile

try:
    import openpyxl
    import pyautogui
    import PIL
    import clipboard
    import cv2
    import numpy
    import cx_Oracle
except ModuleNotFoundError:
    os.system('pip install openpyxl')
    os.system('pip install pyautogui')
    os.system("pip install Pillow")
    os.system("pip install clipboard")
    os.system("pip install opencv-python==4.5.5.64")
    os.system("pip install numpy")
    os.system("python -m pip install cx_Oracle --upgrade")

    url_file = 'https://download.oracle.com/otn_software/nt/instantclient/213000/instantclient-basiclite-windows.x64-21.3.0.0.0.zip'
    file_zip = r'client.zip'

    request.urlretrieve(url_file, file_zip)

    with zipfile.ZipFile(file_zip, "r") as zip_ref:
        zip_ref.extractall("client")

    os.remove(file_zip)
