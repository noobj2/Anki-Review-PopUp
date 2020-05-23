#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2020 Mohamad Janati (freaking stupid, right? :|)


from anki.hooks import wrap
from aqt.reviewer import Reviewer
import aqt
from aqt import mw
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
    title_list = ['Youre Doing Great', 'Good Job', 'Keep Going', 'You\'re the Best']
    button_list = ['I\'m Gonna Finish Them', 'Reviews Are Easy', 'I Enjoy Doing My Reviews', 'I Love Anki', 'I\'m not Gonna let Anything Distract me', 'I\'m Gonna Stay Focused', 'just a Few Reviews left, Finishing Them is The Easiest Thing Ever']
    title_text = random.choice(title_list)
    button_text = random.choice(button_list)
    image_list = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png']
    image_path = '/{}'.format(random.choice(image_list))
    window = QDialog(mw)
    window.setWindowTitle(title_text)
    window.setWindowIcon(QIcon(images + "/icon.png"))
    picture = QLabel()
    picture.setText("<img src='{}' style='max-height:450px; max-width:450px;'>".format(images + image_path))
    button = QPushButton(button_text)
    button.clicked.connect(lambda: window.hide())
    layout = QVBoxLayout()
    layout.addWidget(picture)
    layout.addWidget(button)
    window.setLayout(layout)
    return window.exec_()


Reviewer._answerCard = wrap(Reviewer._answerCard, myPopUp, 'before')
