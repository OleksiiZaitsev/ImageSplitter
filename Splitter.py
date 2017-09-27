from PIL import Image, ImageDraw
import os
from PyQt4 import QtCore, QtGui
import myUI
import sys
import threading
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
UI = myUI.Ui_ImageSplitter()
UI.setupUi(window)
app.setWindowIcon(QtGui.QIcon('icon.ico'))

UI.label_image.setPixmap(QPixmap(r"img\image.jpg"))




#Oculus_Cubemap_Generator_Left_Hand
#OpenGL_Stereoscopic_Cube_Map
#Spherical_Stereoscopic
#Cube_Map_Unity
#Cube_Map
#OpenGL_CubeW
#Unity_Cube_Stereoscopic

def get_max_number_name(path, map_type) -> "return max number in name from dirs or files by path":
    dirs_names = os.listdir(path)
    list_of_numbers = []
    clear_list_names = []

    for i,n in enumerate(dirs_names):
        
        if os.path.isdir(os.path.join(path, n)) and re.findall("{} -[0-9]*".format(map_type), n):
            clear_list_names.append(n)
            

    for i in clear_list_names:
        number = re.findall('.*([-_][0-9]+).*', i)
        if number:
            list_of_numbers.append(*number)


    try:
        max_number = max([int(re.sub('[-_]', '', i)) for i in list_of_numbers])
    except:
        max_number = 0


    return str(max_number + 1)



def CubeW_Stereoscopic():
    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'OpenGL_Stereoscopic_Cube_Map -' + get_max_number_name(path, "OpenGL_Stereoscopic_Cube_Map")

    if not os.path.exists(os.path.join(path, dir_name, r"right")):
        os.makedirs(os.path.join(path, dir_name, r'right'))

    image.crop((  0,     h/4, w/6,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"right\left.png"), "PNG")
    image.crop((w/6,     h/4, w/3,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"right\front.png"), "PNG")
    image.crop((w/3,     h/4, w/2,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"right\right.png"), "PNG")
    UI.progressBar.setProperty("value", 25)
    image.crop((w/6,       0, w/3,  h/4)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"right\top.png"), "PNG")
    image.crop((w/6, (h/4)*2, w/3, (h/4)*3)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"right\bot.png"), "PNG")
    image.crop((w/6, (h/4)*3, w/3,  h)).transpose(Image.FLIP_LEFT_RIGHT).rotate(180).save(os.path.join(path, dir_name, r"right\back.png"), "PNG")
    UI.progressBar.setProperty("value", 50)

    if not os.path.exists(os.path.join(path, dir_name, r"left")):
        os.makedirs(os.path.join(path, dir_name, r'left'))

    image.crop((    w/2,     h/4, (w/6)*4,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"left\left.png"), "PNG")
    image.crop(((w/6)*4,     h/4, (w/6)*5,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"left\front.png"), "PNG")
    image.crop(((w/6)*5,     h/4,      w,   h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"left\right.png"), "PNG")
    UI.progressBar.setProperty("value", 75)
    image.crop(((w/6)*4,       0, (w/6)*5,  h/4)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"left\top.png"), "PNG")
    image.crop(((w/6)*4,     h/2, (w/6)*5, (h/4)*3)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"left\bot.png"), "PNG")
    image.crop(((w/6)*4, (h/4)*3, (w/6)*5,  h)).transpose(Image.FLIP_LEFT_RIGHT).rotate(180).save(os.path.join(path, dir_name, r"left\back.png"), "PNG")
    UI.progressBar.setProperty("value", 100)
    del image

def Spherical_Stereoscopic():
    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'Spherical_Stereoscopic -' + get_max_number_name(path, "Spherical_Stereoscopic")

    if not os.path.exists(os.path.join(path, dir_name)):
        os.makedirs(os.path.join(path, dir_name))
    image.crop((  0, 0, w/2, h)).save(os.path.join(path, dir_name, r"left.png"), "PNG")
    UI.progressBar.setProperty("value", 50)
    image.crop((w/2, 0,  w,  h)).save(os.path.join(path, dir_name, r"right.png"), "PNG")
    UI.progressBar.setProperty("value", 100)
    del image

def Unity_CubeW():
    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'Cube_Map_Unity -' + get_max_number_name(path, "Cube_Map_Unity")

    if not os.path.exists(os.path.join(path, dir_name)):
        os.makedirs(os.path.join(path, dir_name))
    image.crop((      0,     h/4,     w/3,  h/2)).save(os.path.join(path, dir_name, r"right.png"), "PNG")   #LEFT
    image.crop((    w/3,     h/4, (w/3)*2,  h/2)).save(os.path.join(path, dir_name, r"front.png"), "PNG")
    image.crop(((w/3)*2,     h/4,       w,  h/2)).save(os.path.join(path, dir_name, r"left.png"), "PNG")    #RIGHT
    UI.progressBar.setProperty("value", 50)
    image.crop((    w/3,       0, (w/3)*2,  h/4)).save(os.path.join(path, dir_name, r"top.png"), "PNG")
    image.crop((    w/3,     h/2, (w/3)*2, (h/4)*3)).save(os.path.join(path, dir_name, r"bot.png"), "PNG")
    image.crop((    w/3, (h/4)*3, (w/3)*2,  h)).rotate(180).save(os.path.join(path, dir_name, r"back.png"), "PNG")
    UI.progressBar.setProperty("value", 100)
    del image

def CubeW():
    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'Cube_Map -' + get_max_number_name(path, "Cube_Map")

    if not os.path.exists(os.path.join(path, dir_name)):
        os.makedirs(os.path.join(path, dir_name))
    image.crop((      0,     h/4,     w/3,  h/2)).save(os.path.join(path, dir_name, r"left.png"), "PNG")
    image.crop((    w/3,     h/4, (w/3)*2,  h/2)).save(os.path.join(path, dir_name, r"front.png"), "PNG")
    image.crop(((w/3)*2,     h/4,       w,  h/2)).save(os.path.join(path, dir_name, r"right.png"), "PNG")
    UI.progressBar.setProperty("value", 50)
    image.crop((    w/3,       0, (w/3)*2,  h/4)).save(os.path.join(path, dir_name, r"top.png"), "PNG")
    image.crop((    w/3,     h/2, (w/3)*2, (h/4)*3)).save(os.path.join(path, dir_name, r"bot.png"), "PNG")
    image.crop((    w/3, (h/4)*3, (w/3)*2,  h)).rotate(180).save(os.path.join(path, dir_name, r"back.png"), "PNG")
    UI.progressBar.setProperty("value", 100)
    del image

def OpenGL_CubeW():

    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'OpenGL_CubeW -' + get_max_number_name(path, "OpenGL_CubeW")

    if not os.path.exists(os.path.join(path, dir_name)):
        os.makedirs(os.path.join(path, dir_name))
    image.crop((      0,     h/4,     w/3,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"left.png"), "PNG")
    image.crop((    w/3,     h/4, (w/3)*2,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"front.png"), "PNG")
    image.crop(((w/3)*2,     h/4,       w,  h/2)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"right.png"), "PNG")
    UI.progressBar.setProperty("value", 50)
    image.crop((    w/3,       0, (w/3)*2,  h/4)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"top.png"), "PNG")
    image.crop((    w/3,     h/2, (w/3)*2, (h/4)*3)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"bot.png"), "PNG")
    image.crop((    w/3, (h/4)*3, (w/3)*2,  h)).transpose(Image.FLIP_LEFT_RIGHT).rotate(180).save(os.path.join(path, dir_name, r"back.png"), "PNG")
    UI.progressBar.setProperty("value", 100)
    del image

def Unity_Cube_Stereoscopic():
    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'Unity_Cube_Stereoscopic -' + get_max_number_name(path, "Unity_Cube_Stereoscopic")

    if not os.path.exists(os.path.join(path, dir_name, r"right")):
        os.makedirs(os.path.join(path, dir_name, r'right'))

    image.crop((  0,     h/4, w/6,  h/2)).save(os.path.join(path, dir_name, r"right\right.png"), "PNG")
    image.crop((w/6,     h/4, w/3,  h/2)).save(os.path.join(path, dir_name, r"right\front.png"), "PNG")
    image.crop((w/3,     h/4, w/2,  h/2)).save(os.path.join(path, dir_name, r"right\left.png"), "PNG")
    UI.progressBar.setProperty("value", 25)
    image.crop((w/6,       0, w/3,  h/4)).save(os.path.join(path, dir_name, r"right\top.png"), "PNG")
    image.crop((w/6, (h/4)*2, w/3, (h/4)*3)).save(os.path.join(path, dir_name, r"right\bot.png"), "PNG")
    image.crop((w/6, (h/4)*3, w/3,  h)).rotate(180).save(os.path.join(path, dir_name, r"right\back.png"), "PNG")
    UI.progressBar.setProperty("value", 50)

    if not os.path.exists(os.path.join(path, dir_name, r"left")):
        os.makedirs(os.path.join(path, dir_name, r'left'))

    image.crop((    w/2,     h/4, (w/6)*4,  h/2)).save(os.path.join(path, dir_name, r"left\right.png"), "PNG")
    image.crop(((w/6)*4,     h/4, (w/6)*5,  h/2)).save(os.path.join(path, dir_name, r"left\front.png"), "PNG")
    image.crop(((w/6)*5,     h/4,      w,   h/2)).save(os.path.join(path, dir_name, r"left\left.png"), "PNG")
    UI.progressBar.setProperty("value", 75)
    image.crop(((w/6)*4,       0, (w/6)*5,  h/4)).save(os.path.join(path, dir_name, r"left\top.png"), "PNG")
    image.crop(((w/6)*4,     h/2, (w/6)*5, (h/4)*3)).save(os.path.join(path, dir_name, r"left\bot.png"), "PNG")
    image.crop(((w/6)*4, (h/4)*3, (w/6)*5,  h)).rotate(180).save(os.path.join(path, dir_name, r"left\back.png"), "PNG")
    UI.progressBar.setProperty("value", 100)
    del image

# def Oculus_Cubemap_Generator():
#
#     UI.progressBar.setProperty("value", 0)
#     image = Image.open(UI.lineEdit_IMAGE_PATH.text())
#     path = (UI.lineEdit_SAVE_PATH.text())
#
#     draw = ImageDraw.Draw(image)
#     width = image.size[0]
#     height = image.size[1]
#     pix = image.load()
#     w, h = image.size
#     dir_name = r'Oculus_Cubemap_Generator -' + get_max_number_name(path, "Oculus_Cubemap_Generator")
#
#     if not os.path.exists(os.path.join(path, dir_name)):
#         os.makedirs(os.path.join(path, dir_name))
#
#     image.crop((0,       0,      w/6,  h)).save(os.path.join(path, dir_name, r"Left_PX.png"), "PNG")
#     image.crop((    w/6, 0,  (w/6)*2,  h)).save(os.path.join(path, dir_name, r"Right_NX.png"), "PNG")
#     image.crop(((w/6)*2, 0,  (w/6)*3,  h)).save(os.path.join(path, dir_name, r"Up_PY.png"), "PNG")
#
#     UI.progressBar.setProperty("value", 50)
#
#     image.crop(((w/6)*3,     0,     (w/6)*4,  h)).save(os.path.join(path, dir_name, r"Down_NY.png"), "PNG")
#     image.crop(((w/6)*4,     0,     (w/6)*5,  h)).save(os.path.join(path, dir_name, r"Back_PZ.png"), "PNG")
#     image.crop(((w/6)*5,     0,     (w/6)*6,  h)).save(os.path.join(path, dir_name, r"Front_NZ.png"), "PNG")
#
#     # int(UI.lineEdit_X.text())
#     # int(UI.lineEdit_Y.text())
#
#     const_X_size = int(int(UI.lineEdit_X.text())/6)
#
#
#     images = [[os.path.join(path, dir_name, r"Left_PX.png"),  int(0),   int(0)]
#             , [os.path.join(path, dir_name, r"Right_NX.png"), const_X_size,   int(0)]
#             , [os.path.join(path, dir_name, r"Up_PY.png"),    const_X_size*2, int(0)]
#             , [os.path.join(path, dir_name, r"Down_NY.png"),  const_X_size*3, int(0)]
#             , [os.path.join(path, dir_name, r"Back_PZ.png"),  const_X_size*4, int(0)]
#             , [os.path.join(path, dir_name, r"Front_NZ.png"), const_X_size*5, int(0)]]
#
#     UI.progressBar.setProperty("value", 75)
#
#     background = Image.new("RGB", (int(UI.lineEdit_X.text()), int(UI.lineEdit_Y.text())), (0, 0, 0, 0))
#     for image, x, y in images:
#         print("image :", image, "position x:", x, "position y:", y)
#         image = Image.open(image).convert('RGB')
#
#         if h != int(UI.lineEdit_Y.text()) or w != int(UI.lineEdit_X.text()):
#             background.paste(image.resize((int(UI.lineEdit_X.text()) // 6, int(UI.lineEdit_Y.text()))), (x, y))
#         else:
#          background.paste(image, (x, y))
#
#     background.save(os.path.join(path, dir_name, r"Oculus_Cubemap.png"), "PNG")
#
#     UI.progressBar.setProperty("value", 100)
#     del image

def Oculus_Cubemap_Generator_Left_Hand():

    UI.progressBar.setProperty("value", 0)
    image = Image.open(UI.lineEdit_IMAGE_PATH.text())
    path = (UI.lineEdit_SAVE_PATH.text())

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    w, h = image.size
    dir_name = r'Oculus_Cubemap_Generator_Left_Hand -' + get_max_number_name(path, "Oculus_Cubemap_Generator_Left_Hand")

    if not os.path.exists(os.path.join(path, dir_name)):
        os.makedirs(os.path.join(path, dir_name))

    image.crop((0,       0,      w/6,  h)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"Left_PX.png"), "PNG")
    image.crop((    w/6, 0,  (w/6)*2,  h)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"Right_NX.png"), "PNG")
    image.crop(((w/6)*2, 0,  (w/6)*3,  h)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"Up_PY.png"), "PNG")

    UI.progressBar.setProperty("value", 50)

    image.crop(((w/6)*3,     0,     (w/6)*4,  h)).transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, dir_name, r"Down_NY.png"), "PNG")
    image.crop(((w/6)*4,     0,     (w/6)*5,  h)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"Back_PZ.png"), "PNG")
    image.crop(((w/6)*5,     0,     (w/6)*6,  h)).transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, dir_name, r"Front_NZ.png"), "PNG")


    const_X_size = int(int(UI.lineEdit_X.text())/6)


    images = [[os.path.join(path, dir_name, r"Left_PX.png"),  int(0),   int(0)]
            , [os.path.join(path, dir_name, r"Right_NX.png"), const_X_size,   int(0)]
            , [os.path.join(path, dir_name, r"Up_PY.png"),    const_X_size*2, int(0)]
            , [os.path.join(path, dir_name, r"Down_NY.png"),  const_X_size*3, int(0)]
            , [os.path.join(path, dir_name, r"Back_PZ.png"),  const_X_size*4, int(0)]
            , [os.path.join(path, dir_name, r"Front_NZ.png"), const_X_size*5, int(0)]]

    UI.progressBar.setProperty("value", 75)

    background = Image.new("RGB", (int(UI.lineEdit_X.text()), int(UI.lineEdit_Y.text())), (0, 0, 0, 0))
    for image, x, y in images:
        print("image :", image, "position x:", x, "position y:", y)
        image = Image.open(image).convert('RGB')

        if h != int(UI.lineEdit_Y.text()) or w != int(UI.lineEdit_X.text()):
            background.paste(image.resize((int(UI.lineEdit_X.text()) // 6, int(UI.lineEdit_Y.text()))), (x, y))
        else:
         background.paste(image, (x, y))

    background.save(os.path.join(path, dir_name, r"Oculus_Cubemap.png"), "PNG")

    UI.progressBar.setProperty("value", 100)
    del image

class programThreads():
    def __init__(self, func):
        self.func = func

    def START(self):
        self.Thread = threading.Thread(target=lambda: self.func())
        self.Thread.start()


# ICONS
UI.pushButton_CubeW_Stereoscopic.setIcon(QIcon(r"img\OpenGL_CubeW_Stereoscopic.png"))
UI.pushButton_Spherical_Stereoscopic.setIcon(QIcon(r"img\Spherical_Stereoscopic.png"))
UI.pushButton_Unity_CubeW.setIcon(QIcon(r"img\Unity_CubeW.png"))
UI.pushButton_CubeW.setIcon(QIcon(r"img\CubeW.png"))
UI.pushButton_OpenGL_CubeW.setIcon(QIcon(r"img\OpenGL_CubeW.png"))
UI.pushButton_Unity_Cube_Stereoscopic.setIcon(QIcon(r"img\Unity_Cube_Stereoscopic.png"))
UI.pushButton_Oculus_Cubemap_Generator.setIcon(QIcon(r"img\Oculus_Cubemap_Generator.png"))

# THREADS
Thread_CubeW_Stereoscopic = programThreads(CubeW_Stereoscopic)
Thread_Spherical_Stereoscopic = programThreads(Spherical_Stereoscopic)
Thread_CubeW = programThreads(CubeW)
Thread_Unity_CubeW = programThreads(Unity_CubeW)
Thread_OpenGL_CubeW = programThreads(OpenGL_CubeW)
Thread_Unity_Cube_Stereoscopic = programThreads(Unity_Cube_Stereoscopic)
Thread_Oculus_Cubemap_Generator = programThreads(Oculus_Cubemap_Generator_Left_Hand)

# BUTTONS
QtCore.QObject.connect(UI.pushButton_Spherical_Stereoscopic, QtCore.SIGNAL("clicked()"), lambda: Thread_Spherical_Stereoscopic.START())
QtCore.QObject.connect(UI.pushButton_CubeW_Stereoscopic, QtCore.SIGNAL("clicked()"), lambda: Thread_CubeW_Stereoscopic.START())
QtCore.QObject.connect(UI.pushButton_Unity_CubeW, QtCore.SIGNAL("clicked()"), lambda: Thread_Unity_CubeW.START())
QtCore.QObject.connect(UI.pushButton_CubeW, QtCore.SIGNAL("clicked()"), lambda: Thread_CubeW.START())
QtCore.QObject.connect(UI.pushButton_OpenGL_CubeW, QtCore.SIGNAL("clicked()"), lambda: Thread_OpenGL_CubeW.START())
QtCore.QObject.connect(UI.pushButton_Unity_Cube_Stereoscopic, QtCore.SIGNAL("clicked()"), lambda: Thread_Unity_Cube_Stereoscopic.START())
QtCore.QObject.connect(UI.pushButton_Oculus_Cubemap_Generator, QtCore.SIGNAL("clicked()"), lambda: Thread_Oculus_Cubemap_Generator.START())

def set_image_path():

    fileName = QtGui.QFileDialog.getOpenFileName(filter="Images (*.png *.bmp *.jpg)")
    UI.label_image.setPixmap(QPixmap(fileName))
    UI.lineEdit_IMAGE_PATH.setText(fileName)

def set_save_path():
    fileName = QtGui.QFileDialog.getExistingDirectory()
    UI.lineEdit_SAVE_PATH.setText(fileName)



UI.toolButton_get_Image.clicked.connect(lambda: set_image_path())
UI.toolButton_get_Path.clicked.connect(lambda: set_save_path())




# COLORS



if __name__ == '__main__':
    UI.progressBar.setProperty("value", 0)
    window.show()
    sys.exit(app.exec_())
