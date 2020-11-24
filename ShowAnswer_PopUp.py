#// auth_ Mohamad Janati
#// Copyright (c) 2020 Mohamad Janati (freaking stupid, right? :|)


from anki.hooks import wrap
from anki.sound import play, clearAudioQueue, AVPlayer
from aqt.reviewer import Reviewer
import aqt
from aqt import mw
from aqt.qt import *
import os
from os.path import join, dirname
import random
addon_path = dirname(__file__)
config = mw.addonManager.getConfig(__name__)


def _play_tags(self, tags):
    self._enqueued = tags[:]
    if self.interrupt_current_audio and False:
        self._stop_if_playing()
    self._play_next_if_idle()


def myPopUp(self):
    SA_popUp_Chance = config["Show Answer Pop-Up Chance"]
    show_random = random.choice(range((101 - SA_popUp_Chance)))
    if show_random == 0:
        play_audio = config["Play Audio"]
        # if self.state == "review":
        folder = 'show_answer'
        audio_folder = join(addon_path, 'user_files/audio_video', folder)
        audioName_list = os.listdir(audio_folder)
        audio_name = '/{}'.format(random.choice(audioName_list))
        audio_path = audio_folder + audio_name
        if play_audio:
            AVPlayer.play_tags=_play_tags
            clearAudioQueue()
            play(audio_path)
        if SA_popUp_Chance != 0:
            show_popUp()

def show_popUp():
    headerText_fontSize = config["Header Text Font Size"]
    headerText_fontStyle = config["Header Text Font Style"]
    show_header = config["Show Header"]
    show_image = config["Show Image"]
    header_list_SA = config["Header Texts_ Show Answer"]
    title_list_SA = config["Window Titles_ Show Answer"]
    button_list_SA = config["Button Texts_ Show Answer"]

    folder = 'show_answer'
    header_text = random.choice(header_list_SA)
    title_text = random.choice(title_list_SA)
    button_text = random.choice(button_list_SA)

    image_folder = join(addon_path, 'user_files/images', folder)
    imageName_list = os.listdir(image_folder)
    image_name = '/{}'.format(random.choice(imageName_list))

    window = QDialog(mw)
    window.setWindowTitle(title_text)
    window.setWindowIcon(QIcon(join(addon_path, 'user_files/images') + "/icon.png"))
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
    if not show_image and not show_header:
        return
    else:
        window.exec()


Reviewer._showAnswer = wrap(Reviewer._showAnswer, myPopUp, 'after')
