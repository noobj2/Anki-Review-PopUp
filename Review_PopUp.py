#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2019-2020 Mohamad Janati (freaking stupid, right? :|)


from anki.hooks import wrap
from aqt.reviewer import Reviewer
import aqt
from aqt.qt import *
import os
from os.path import join, dirname
import random
addon_path = dirname(__file__)
images = join(addon_path, 'images')

def myPopUp(self, ease):
    show_random = random.choice(range(2))
    if show_random == 0:
        showImage()
def showImage():
    image_list = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png']
    image_path = '/{}'.format(random.choice(image_list))
    window = QDialog()
    window.setWindowTitle("Review Pop Up")
    window.setWindowIcon(QIcon(images + "/icon.png"))
    picture = QLabel()
    picture.setText("<img src='{}' style='max-height:450px; max-width:450px;'>".format(images + image_path))
    button = QPushButton('Ok')
    button.clicked.connect(lambda: window.hide())
    layout = QVBoxLayout()
    layout.addWidget(picture)
    layout.addWidget(button)
    window.setLayout(layout)
    return window.exec_()


Reviewer._answerCard = wrap(Reviewer._answerCard, myPopUp, 'before')
