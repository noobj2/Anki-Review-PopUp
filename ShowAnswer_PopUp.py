#// auth_ Mamad
#// Copyright (c) 2020 - 2023 Mamad


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
popUp_type = config["Pop-Up Type"]
ordered_number = 0


def _play_tags(self, tags):
    self._enqueued = tags[:]
    self._play_next_if_idle()

def myPopUp(self):
    global ordered_number
    SA_popUp_Chance = config["Show Answer Pop-Up Chance"]
    show_random = random.choice(range((101 - SA_popUp_Chance)))
    if show_random == 0 and SA_popUp_Chance != 0:
        play_audio = config["Play Audio"]
        play_videoGif = config["Play Video/GIF"]
        # 0: random, 1: ordered
        folder = 'show_answer'
        if play_audio:
            audio_folder = join(addon_path, 'user_files/audio', folder)
            audioName_list = os.listdir(audio_folder)
            if popUp_type == 1:
                audio_name = '/{}'.format(audioName_list[min(ordered_number, len(audioName_list) - 1)])
                ordered_number += 1
            else:
                audio_name = '/{}'.format(random.choice(audioName_list))
            audio_path = audio_folder + audio_name
            AVPlayer.play_tags=_play_tags
            clearAudioQueue()
            play(audio_path)
        if play_videoGif:
            video_folder = join(addon_path, 'user_files/video_gif', folder)
            videoName_list = os.listdir(video_folder)
            video_name = '/{}'.format(random.choice(videoName_list))
            video_path = video_folder + video_name
            AVPlayer.play_tags=_play_tags
            clearAudioQueue()
            play(video_path)
        show_popUp()

def show_popUp():
    global ordered_number
    headerText_fontSize = config["Header Text Font Size"]
    headerText_fontStyle = config["Header Text Font Style"]
    show_header = config["Show Header"]
    show_image = config["Show Image"]
    header_list_SA = config["Header Texts_ Show Answer"]

    folder = 'show_answer'
    header_text = random.choice(header_list_SA)

    image_folder = join(addon_path, 'user_files/images', folder)
    imageName_list = os.listdir(image_folder)
    if popUp_type == 1:
        image_name = '/{}'.format(imageName_list[min(ordered_number, len(imageName_list) - 1)])
        ordered_number += 1
    else:
        image_name = '/{}'.format(random.choice(imageName_list))

    window = QDialog(mw)
    window.setWindowIcon(QIcon(join(addon_path, 'user_files/images') + "/icon.png"))
    header = QLabel()
    header.setAlignment(Qt.AlignmentFlag.AlignCenter)
    header.setText("<div style='font-size: {}px; font-family: {};'> {} </div>".format(headerText_fontSize, headerText_fontStyle, header_text))
    image = QLabel()
    pixmap = QPixmap(image_folder + image_name)
    max_height = min(pixmap.height(), 1024)
    max_width = min(pixmap.width(), 1024)
    picture = pixmap.scaled(max_width, max_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    image.setAlignment(Qt.AlignmentFlag.AlignCenter)
    image.setPixmap(picture)
    image.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout = QVBoxLayout()
    if show_header:
        layout.addWidget(header)
    if show_image:
        layout.addWidget(image)
    window.setLayout(layout)
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup | Qt.WindowType.NoDropShadowWindowHint)
    window.keyPressEvent = lambda event: window.hide() if event.key() != Qt.Key.Key_unknown else None
    if not show_image and not show_header:
        return
    else:
        window.exec()


Reviewer._showAnswer = wrap(Reviewer._showAnswer, myPopUp, 'after')
