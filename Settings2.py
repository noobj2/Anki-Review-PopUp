#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2020 Mohamad Janati (freaking stupid, right? :|)


from aqt.qt import *
import aqt
from aqt import mw
import os
from os.path import join, dirname

def refreshConfig():
    global C_show_header, C_show_image, C_play_audio, C_popUp_chance, C_headerText_fontStyle, C_headerText_fontSize, C_image_names, C_audio_names, C_header_texts, C_window_titles, C_button_texts
    config = mw.addonManager.getConfig(__name__)
    C_show_header = config["Show Header"]
    C_show_image = config["Show Image"]
    C_play_audio = config["Play Audio"]
    C_popUp_chance = config["Pop-Up Chance"]
    C_headerText_fontStyle = config["Header Text Font Style"]
    C_headerText_fontSize = config["Header Text Font Size"]
    C_image_names = config["Image Names"]
    C_audio_names = config["Audio Names"]
    C_header_texts = config["Header Texts"]
    C_window_titles = config["Window Titles"]
    C_button_texts = config["Button Texts"]

class Settings(QDialog):
    refreshConfig()
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        self.mainWindow()

    def mainWindow(self):
        addon_path = dirname(__file__)
        self.settings()
        self.loadCurrent()
        self.setFixedWidth(450)
        self.setLayout(self.layout)
        self.setWindowTitle("Review Pop-Up Settings")
        self.setWindowIcon(QIcon(addon_path + "/images/icon.png"))

    def settings(self):
        addon_path = dirname(__file__)
        images = join(addon_path, 'images')
        audio = join(addon_path, 'audio')
        self.header_checkbox = QCheckBox("Header")
        self.header_checkbox.setToolTip("""Shows a random line in \"Header Texts\" list.
        You can edit the list by pressing the \"Header Texts\" button down belw.""")
        self.image_checkbox = QCheckBox("Image")
        self.image_checkbox.setToolTip("""Shows a random image from images folder.
        You can add images by copying images to the \"images\" foler in add-on folder. open the folder by pressing \"Open Images Folder\" button down below.""")
        self.audio_checkbox = QCheckBox("Audio")
        self.audio_checkbox.setToolTip("""Plays a random audio from \"audio\" folder in add-on folder.
        You can add audio by copying them to the \"audio\" folder in add-on folder. open the folder by pressing \"Open Audio Folder\" button down below.""")
        line1 = QHBoxLayout()
        line1.addWidget(self.header_checkbox)
        line1.addWidget(self.image_checkbox)
        line1.addWidget(self.audio_checkbox)
        viewChance_label = QLabel("Pop-Up Chance")
        viewChance_label.setToolTip("Changes the posibility of pop-up window popping up.")
        viewChance_label.setFixedWidth(210)
        self.view_chance = QSpinBox()
        self.view_chance.setFixedWidth(210)
        self.view_chance.setRange(1, 100)
        self.view_chance.setSuffix("%")
        viewChance_holder = QHBoxLayout()
        viewChance_holder.addWidget(viewChance_label)
        viewChance_holder.addWidget(self.view_chance)
        headerTextSize_label = QLabel("Header Font Size")
        headerTextSize_label.setToolTip("Changes font size for the header text.")
        headerTextSize_label.setFixedWidth(210)
        self.headerText_fontSize = QSpinBox()
        self.headerText_fontSize.setFixedWidth(210)
        self.headerText_fontSize.setMinimum(1)
        self.headerText_fontSize.setSuffix("px")
        header_fontSize_holder = QHBoxLayout()
        header_fontSize_holder.addWidget(headerTextSize_label)
        header_fontSize_holder.addWidget(self.headerText_fontSize)
        headerFontStyle_label = QLabel("Header Font")
        headerFontStyle_label.setToolTip("Changes header font style.")
        headerFontStyle_label.setFixedWidth(210)
        self.headerText_fontStyle = QFontComboBox()
        self.headerText_fontStyle.setFixedWidth(210)
        header_fontStyle_holder = QHBoxLayout()
        header_fontStyle_holder.addWidget(headerFontStyle_label)
        header_fontStyle_holder.addWidget(self.headerText_fontStyle)
        imagesFolder_button = QPushButton("Open Images Folder")
        imagesFolder_button.clicked.connect(lambda: os.startfile(images))
        imageNames_button = QPushButton("Image Names")
        imageNames_window = QDialog()
        imageNames_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        imageNames_window.setWindowTitle("Image Names")
        imageNames_label = QLabel("in order for the add-on to find your images in add-on folder, you should add image name + file name extension (e.g. image.png, image.jpeg, etc.)")
        self.imageNames_textEditor = QPlainTextEdit()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Close)
        buttons.accepted.connect(self.onApply)
        buttons.accepted.connect(lambda: imageNames_window.hide())
        buttons.rejected.connect(imageNames_window.close)
        imageNames_layout = QVBoxLayout()
        imageNames_layout.addWidget(imageNames_label)
        imageNames_layout.addWidget(self.imageNames_textEditor)
        imageNames_layout.addWidget(buttons)
        imageNames_window.setLayout(imageNames_layout)
        imageNames_button.clicked.connect(lambda: imageNames_window.exec())
        images_holder = QHBoxLayout()
        images_holder.addWidget(imagesFolder_button)
        images_holder.addWidget(imageNames_button)
        audioFolder_button = QPushButton("Open Audio Folder")
        audioFolder_button.clicked.connect(lambda: os.startfile(audio))
        audioNames_button = QPushButton("Audio Names")
        audioNames_window = QDialog()
        audioNames_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        audioNames_label = QLabel("in order for the add-on to find your audio in add-on folder, you should add audio name + file name extension (e.g. audio.mp3, audio.wav, etc.)")
        audioNames_window.setWindowTitle("Audio Names")
        self.audioNames_textEditor = QPlainTextEdit()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Close)
        buttons.accepted.connect(self.onApply)
        buttons.accepted.connect(lambda: audioNames_window.hide())
        buttons.rejected.connect(audioNames_window.close)
        audioNames_layout = QVBoxLayout()
        audioNames_layout.addWidget(audioNames_label)
        audioNames_layout.addWidget(self.audioNames_textEditor)
        audioNames_layout.addWidget(buttons)
        audioNames_window.setLayout(audioNames_layout)
        audioNames_button.clicked.connect(lambda: audioNames_window.exec())
        audio_holder = QHBoxLayout()
        audio_holder.addWidget(audioFolder_button)
        audio_holder.addWidget(audioNames_button)
        headerTexts_button = QPushButton("Header Texts")
        headerTexts_window = QDialog()
        headerTexts_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        headerTexts_window.setWindowTitle("Header Texts")
        self.headerTexts_textEditor = QPlainTextEdit()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Close)
        buttons.accepted.connect(self.onApply)
        buttons.accepted.connect(lambda: headerTexts_window.hide())
        buttons.rejected.connect(headerTexts_window.close)
        headerTexts_layout = QVBoxLayout()
        headerTexts_layout.addWidget(self.headerTexts_textEditor)
        headerTexts_layout.addWidget(buttons)
        headerTexts_window.setLayout(headerTexts_layout)
        headerTexts_button.clicked.connect(lambda: headerTexts_window.exec())
        windowTtitles_button = QPushButton("Window Title Texts")
        windowTtitles_window = QDialog()
        windowTtitles_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        windowTtitles_window.setWindowTitle("Window Title Texts")
        self.windowTitlees_textEditor = QPlainTextEdit()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Close)
        buttons.accepted.connect(self.onApply)
        buttons.accepted.connect(lambda: windowTtitles_window.hide())
        buttons.rejected.connect(windowTtitles_window.close)
        windoTitles_layout = QVBoxLayout()
        windoTitles_layout.addWidget(self.windowTitlees_textEditor)
        windoTitles_layout.addWidget(buttons)
        windowTtitles_window.setLayout(windoTitles_layout)
        windowTtitles_button.clicked.connect(lambda: windowTtitles_window.exec())
        buttonTexts_button = QPushButton("Button Texts")
        buttonTexts_window = QDialog()
        buttonTexts_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        buttonTexts_window.setWindowTitle("Button Texts")
        self.buttonTexts_textEditor = QPlainTextEdit()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Close)
        buttons.accepted.connect(self.onApply)
        buttons.accepted.connect(lambda: buttonTexts_window.hide())
        buttons.rejected.connect(buttonTexts_window.close)
        buttonTexts_layout = QVBoxLayout()
        buttonTexts_layout.addWidget(self.buttonTexts_textEditor)
        buttonTexts_layout.addWidget(buttons)
        buttonTexts_window.setLayout(buttonTexts_layout)
        buttonTexts_button.clicked.connect(lambda: buttonTexts_window.exec())
        apply_button = QPushButton("&Apply")
        apply_button.clicked.connect(self.onApply)
        apply_button.clicked.connect(lambda: self.hide())
        cancel_button = QPushButton("&Cancel")
        cancel_button.clicked.connect(lambda: self.hide())
        bottom_line = QHBoxLayout()
        bottom_line.addWidget(apply_button)
        bottom_line.addWidget(cancel_button)
        self.layout = QVBoxLayout()
        self.layout.addLayout(line1)
        self.layout.addLayout(viewChance_holder)
        self.layout.addLayout(header_fontStyle_holder)
        self.layout.addLayout(header_fontSize_holder)
        self.layout.addLayout(images_holder)
        self.layout.addLayout(audio_holder)
        self.layout.addWidget(headerTexts_button)
        self.layout.addWidget(windowTtitles_button)
        self.layout.addWidget(buttonTexts_button)
        self.layout.addLayout(bottom_line)
    def loadCurrent(self):
        if C_show_header:
            self.header_checkbox.setChecked(True)
        if C_show_image:
            self.image_checkbox.setChecked(True)
        if C_play_audio:
            self.audio_checkbox.setChecked(True)
        self.view_chance.setValue(C_popUp_chance)
        self.headerText_fontStyle.setCurrentFont(QFont(C_headerText_fontStyle))
        self.headerText_fontSize.setValue(C_headerText_fontSize)
        self.imageNames_textEditor.setPlainText("{}".format("\n".join(C_image_names)))
        self.audioNames_textEditor.setPlainText("{}".format("\n".join(C_audio_names)))
        self.headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts)))
        self.windowTitlees_textEditor.setPlainText("{}".format("\n".join(C_window_titles)))
        self.buttonTexts_textEditor.setPlainText("{}".format("\n".join(C_button_texts)))
    def onApply(self):
        conf = {
        "Show Header": self.header_checkbox.isChecked(),
        "Show Image": self.image_checkbox.isChecked(),
        "Play Audio": self.audio_checkbox.isChecked(),
        "Pop-Up Chance": self.view_chance.value(),
        "Header Text Font Style": self.headerText_fontStyle.currentFont().family(),
        "Header Text Font Size": self.headerText_fontSize.value(),
        "Image Names": self.imageNames_textEditor.toPlainText().split("\n"),
        "Audio Names": self.audioNames_textEditor.toPlainText().split("\n"),
        "Header Texts": self.headerTexts_textEditor.toPlainText().split("\n"),
        "Window Titles": self.windowTitlees_textEditor.toPlainText().split("\n"),
        "Button Texts": self.buttonTexts_textEditor.toPlainText().split("\n")
        }
        mw.addonManager.writeConfig(__name__, conf)
        refreshConfig()

def open_settings():
    Settings2 = Settings()
    Settings2.exec()
settings = QAction('Review Pop-Up Settings', mw)
settings.triggered.connect(open_settings)
mw.form.menuTools.addAction(settings)
mw.addonManager.setConfigAction(__name__, open_settings)
