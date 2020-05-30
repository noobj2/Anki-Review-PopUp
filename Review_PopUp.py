#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
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


def myPopUp(self, ease):
    popUp_Chance = config["Pop-Up Chance"]
    show_random = random.choice(range((101 - popUp_Chance)))
    if show_random == 0:
        play_audio = config["Play Audio"]
        audio_list_again = config["Audio Names_ Again"]
        audio_list_hard = config["Audio Names_ Hard"]
        audio_list_good = config["Audio Names_ Good"]
        audio_list_easy = config["Audio Names_ Easy"]
        if self.state == "answer":
            if ease == 1:
                audio_folder = join(addon_path, 'audio', 'again')
                audio_name = '/{}'.format(random.choice(audio_list_again))
            elif ease == 2:
                audio_folder = join(addon_path, 'audio', 'hard')
                audio_name = '/{}'.format(random.choice(audio_list_hard))
            elif ease == 3:
                audio_folder = join(addon_path, 'audio', 'good')
                audio_name = '/{}'.format(random.choice(audio_list_good))
            elif ease == 4:
                audio_folder = join(addon_path, 'audio', 'easy')
                audio_name = '/{}'.format(random.choice(audio_list_easy))
            audio_path = audio_folder + audio_name
            if play_audio:
                AVPlayer.play_tags=_play_tags
                clearAudioQueue()
                play(audio_path)
            show_popUp(ease)

def show_popUp(ease):
    headerText_fontSize = config["Header Text Font Size"]
    headerText_fontStyle = config["Header Text Font Style"]
    show_header = config["Show Header"]
    show_image = config["Show Image"]
    image_list_again = config["Image Names_ Again"]
    image_list_hard = config["Image Names_ Hard"]
    image_list_good = config["Image Names_ Good"]
    image_list_easy = config["Image Names_ Easy"]
    header_list_again = config["Header Texts_ Again"]
    header_list_hard = config["Header Texts_ Hard"]
    header_list_good = config["Header Texts_ Good"]
    header_list_easy = config["Header Texts_ Easy"]
    title_list_again = config["Window Titles_ Again"]
    title_list_hard = config["Window Titles_ Hard"]
    title_list_good = config["Window Titles_ Good"]
    title_list_easy = config["Window Titles_ Easy"]
    button_list_again = config["Button Texts_ Again"]
    button_list_hard = config["Button Texts_ Hard"]
    button_list_good = config["Button Texts_ Good"]
    button_list_easy = config["Button Texts_ Easy"]
    if ease == 1:
        image_folder = join(addon_path, 'images', 'again')
        image_name = '/{}'.format(random.choice(image_list_again))
        header_text = random.choice(header_list_again)
        title_text = random.choice(title_list_again)
        button_text = random.choice(button_list_again)
    elif ease == 2:
        image_folder = join(addon_path, 'images', 'hard')
        image_name = '/{}'.format(random.choice(image_list_hard))
        header_text = random.choice(header_list_hard)
        title_text = random.choice(title_list_hard)
        button_text = random.choice(button_list_hard)
    elif ease == 3:
        image_folder = join(addon_path, 'images', 'good')
        image_name = '/{}'.format(random.choice(image_list_good))
        header_text = random.choice(header_list_good)
        title_text = random.choice(title_list_good)
        button_text = random.choice(button_list_good)
    elif ease == 4:
        image_folder = join(addon_path, 'images', 'easy')
        image_name = '/{}'.format(random.choice(image_list_easy))
        header_text = random.choice(header_list_easy)
        title_text = random.choice(title_list_easy)
        button_text = random.choice(button_list_easy)
    else:
        image_folder = join(addon_path, 'images', 'again')
        image_name = '/{}'.format(random.choice(image_list_again))
        header_text = "Wrong Ease?"
        title_text = "Wrong Ease."
        button_text = "Ok"

    window = QDialog(mw)
    window.setWindowTitle(title_text)
    window.setWindowIcon(QIcon(join(addon_path, 'images') + "/icon.png"))
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
    show_onAgain = config["Show on Again"]
    show_onHard = config["Show on Hard"]
    show_onGood = config["Show on Good"]
    show_onEasy = config["Show on Easy"]
    layout.addWidget(button)
    window.setLayout(layout)
    if not show_image and not show_header:
        return
    elif ease == 1 and show_onAgain:
        window.exec()
    elif ease == 2 and show_onHard:
        window.exec()
    elif ease == 3 and show_onGood:
        window.exec()
    elif ease == 4 and show_onEasy:
        window.exec()
    else:
        return


Reviewer._answerCard = wrap(Reviewer._answerCard, myPopUp, 'before')
