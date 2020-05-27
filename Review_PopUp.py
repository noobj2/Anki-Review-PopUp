#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2020 Mohamad Janati (freaking stupid, right? :|)


from anki.hooks import wrap
from anki.sound import play
from aqt.reviewer import Reviewer
import aqt
from aqt import mw
from aqt.qt import *
import os
from os.path import join, dirname
import random
addon_path = dirname(__file__)
image_folder = join(addon_path, 'images')
audio_folder = join(addon_path, 'audio')
config = mw.addonManager.getConfig(__name__)

def myPopUp(self, ease):
    popUp_Chance = config["Pop-Up Chance"]
    show_random = random.choice(range((101 - popUp_Chance)))
    if show_random == 0:
        play_audio = config["Play Audio"]
        audio_list = config["Audio Names"]
        audio_name = '/{}'.format(random.choice(audio_list))
        audio_path = audio_folder + audio_name
        if play_audio:
            play(audio_path)
        show_popUp()

def show_popUp():
    headerText_fontSize = config["Header Text Font Size"]
    headerText_fontStyle = config["Header Text Font Style"]
    show_header = config["Show Header"]
    show_image = config["Show Image"]
    image_list = config["Image Names"]
    image_name = '/{}'.format(random.choice(image_list))
    header_list = config["Header Texts"]
    header_text = random.choice(header_list)
    title_list = config["Window Titles"]
    title_text = random.choice(title_list)
    button_list = config["Button Texts"]
    button_text = random.choice(button_list)

    window = QDialog(mw)
    window.setWindowTitle(title_text)
    window.setWindowIcon(QIcon(image_folder + "/icon.png"))
    header = QLabel()
    header.setAlignment(Qt.AlignCenter)
    header.setText("<div style='font-size: {}px; font-family: {};'> {} </div>".format(headerText_fontSize, headerText_fontStyle, header_text))
    image = QLabel()
    image.setAlignment(Qt.AlignCenter)
    image.setText("<img src='{}' style='max-height: 450px; max-width: 450px;'>".format(image_folder + image_name))
    button = QPushButton(button_text)
    button.clicked.connect(lambda: window.hide())
    layout = QVBoxLayout()
    if show_header:
        layout.addWidget(header)
    if show_image:
        layout.addWidget(image)
    layout.addWidget(button)
    window.setLayout(layout)
    return window.exec_()


Reviewer._answerCard = wrap(Reviewer._answerCard, myPopUp, 'before')
