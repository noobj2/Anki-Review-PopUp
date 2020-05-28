#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2020 Mohamad Janati (freaking stupid, right? :|)


from aqt.qt import *
from aqt.utils import showInfo
import aqt
from aqt import mw
import os
from os.path import join, dirname

def refreshConfig():
    global C_show_header, C_show_image, C_play_audio, C_show_onAgain, C_show_onHard, C_show_onGood, C_show_onEasy, C_popUp_chance, C_headerText_fontStyle, C_headerText_fontSize, C_image_names_again, C_image_names_hard, C_image_names_good, C_image_names_easy, C_audio_names_again, C_audio_names_hard, C_audio_names_good, C_audio_names_easy, C_header_texts_again, C_header_texts_hard, C_header_texts_good, C_header_texts_easy, C_window_titles_again, C_window_titles_hard, C_window_titles_good, C_window_titles_easy, C_button_texts_again, C_button_texts_hard, C_button_texts_good, C_button_texts_easy
    config = mw.addonManager.getConfig(__name__)
    C_show_header = config["Show Header"]
    C_show_image = config["Show Image"]
    C_play_audio = config["Play Audio"]
    C_show_onAgain = config["Show on Again"]
    C_show_onHard = config["Show on Hard"]
    C_show_onGood = config["Show on Good"]
    C_show_onEasy = config["Show on Easy"]
    C_popUp_chance = config["Pop-Up Chance"]
    C_headerText_fontStyle = config["Header Text Font Style"]
    C_headerText_fontSize = config["Header Text Font Size"]
    C_image_names_again = config["Image Names_ Again"]
    C_image_names_hard = config["Image Names_ Hard"]
    C_image_names_good = config["Image Names_ Good"]
    C_image_names_easy = config["Image Names_ Easy"]
    C_audio_names_again = config["Audio Names_ Again"]
    C_audio_names_hard = config["Audio Names_ Hard"]
    C_audio_names_good = config["Audio Names_ Good"]
    C_audio_names_easy = config["Audio Names_ Easy"]
    C_header_texts_again = config["Header Texts_ Again"]
    C_header_texts_hard = config["Header Texts_ Hard"]
    C_header_texts_good = config["Header Texts_ Good"]
    C_header_texts_easy = config["Header Texts_ Easy"]
    C_window_titles_again = config["Window Titles_ Again"]
    C_window_titles_hard = config["Window Titles_ Hard"]
    C_window_titles_good = config["Window Titles_ Good"]
    C_window_titles_easy = config["Window Titles_ Easy"]
    C_button_texts_again = config["Button Texts_ Again"]
    C_button_texts_hard = config["Button Texts_ Hard"]
    C_button_texts_good = config["Button Texts_ Good"]
    C_button_texts_easy = config["Button Texts_ Easy"]

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
        self.header_checkbox.setFixedWidth(102)
        self.header_checkbox.setToolTip("""Shows a random line in \"Header Texts\" list.
        You can edit the list by pressing the \"Header Texts\" button down belw.""")
        self.image_checkbox = QCheckBox("Image")
        self.image_checkbox.setFixedWidth(102)
        self.image_checkbox.setToolTip("""Shows a random image from images folder.
        You can add images by copying images to the \"images\" foler in add-on folder. open the folder by pressing \"Open Images Folder\" button down below.""")
        self.audio_checkbox = QCheckBox("Audio")
        self.audio_checkbox.setFixedWidth(102)
        self.audio_checkbox.setToolTip("""Plays a random audio from \"audio\" folder in add-on folder.
        You can add audio by copying them to the \"audio\" folder in add-on folder. open the folder by pressing \"Open Audio Folder\" button down below.""")
        line1 = QHBoxLayout()
        line1.addWidget(self.header_checkbox)
        line1.addWidget(self.image_checkbox)
        line1.addWidget(self.audio_checkbox)
        line1.addStretch()
        self.show_onAgain = QCheckBox("Again")
        self.show_onHard = QCheckBox("Hard")
        self.show_onGood = QCheckBox("Good")
        self.show_onEasy = QCheckBox("Easy")
        line2 = QHBoxLayout()
        line2.addWidget(self.show_onAgain)
        line2.addWidget(self.show_onHard)
        line2.addWidget(self.show_onGood)
        line2.addWidget(self.show_onEasy)
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

        image_tabs = QTabWidget()
        self.again_imageNames_textEditor = QPlainTextEdit()
        self.again_imageNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        again_layout = QVBoxLayout()
        again_layout.addWidget(self.again_imageNames_textEditor)
        again_tab = QWidget()
        again_tab.setLayout(again_layout)
        image_tabs.addTab(again_tab, "Again")
        self.hard_imageNames_textEditor = QPlainTextEdit()
        self.hard_imageNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        hard_layout = QVBoxLayout()
        hard_layout.addWidget(self.hard_imageNames_textEditor)
        hard_tab = QWidget()
        hard_tab.setLayout(hard_layout)
        image_tabs.addTab(hard_tab, "Hard")
        self.good_imageNames_textEditor = QPlainTextEdit()
        self.good_imageNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        good_layout = QVBoxLayout()
        good_layout.addWidget(self.good_imageNames_textEditor)
        good_tab = QWidget()
        good_tab.setLayout(good_layout)
        image_tabs.addTab(good_tab, "Good")
        self.easy_imageNames_textEditor = QPlainTextEdit()
        self.easy_imageNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        easy_layout = QVBoxLayout()
        easy_layout.addWidget(self.easy_imageNames_textEditor)
        easy_tab = QWidget()
        easy_tab.setLayout(easy_layout)
        image_tabs.addTab(easy_tab, "Easy")
        images_vbox = QVBoxLayout()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Close)
        buttons.rejected.connect(imageNames_window.close)
        images_vbox.addWidget(image_tabs)
        images_vbox.addWidget(buttons)
        imageNames_window.setLayout(images_vbox)

        imageNames_button.clicked.connect(lambda: imageNames_window.exec())
        images_holder = QHBoxLayout()
        images_holder.addWidget(imagesFolder_button)
        images_holder.addWidget(imageNames_button)
        audioFolder_button = QPushButton("Open Audio Folder")
        audioFolder_button.clicked.connect(lambda: os.startfile(audio))
        audioNames_button = QPushButton("Audio Names")
        audioNames_window = QDialog()
        audioNames_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        audioNames_window.setWindowTitle("Audio Names")
        audioNames_label = QLabel("in order for the add-on to find your audio in add-on folder, you should add audio name + file name extension (e.g. audio.mp3, audio.wav, etc.)")

        audio_tabs = QTabWidget()
        self.again_audioNames_textEditor = QPlainTextEdit()
        self.again_audioNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        again_layout = QVBoxLayout()
        again_layout.addWidget(self.again_audioNames_textEditor)
        again_tab = QWidget()
        again_tab.setLayout(again_layout)
        audio_tabs.addTab(again_tab, "Again")
        self.hard_audioNames_textEditor = QPlainTextEdit()
        self.hard_audioNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        hard_layout = QVBoxLayout()
        hard_layout.addWidget(self.hard_audioNames_textEditor)
        hard_tab = QWidget()
        hard_tab.setLayout(hard_layout)
        audio_tabs.addTab(hard_tab, "Hard")
        self.good_audioNames_textEditor = QPlainTextEdit()
        self.good_audioNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        good_layout = QVBoxLayout()
        good_layout.addWidget(self.good_audioNames_textEditor)
        good_tab = QWidget()
        good_tab.setLayout(good_layout)
        audio_tabs.addTab(good_tab, "Good")
        self.easy_audioNames_textEditor = QPlainTextEdit()
        self.easy_audioNames_textEditor.setWordWrapMode(QTextOption.NoWrap)
        easy_layout = QVBoxLayout()
        easy_layout.addWidget(self.easy_audioNames_textEditor)
        easy_tab = QWidget()
        easy_tab.setLayout(easy_layout)
        audio_tabs.addTab(easy_tab, "Easy")
        audio_vbox = QVBoxLayout()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Close)
        buttons.rejected.connect(audioNames_window.close)
        audio_vbox.addWidget(audio_tabs)
        audio_vbox.addWidget(buttons)
        audioNames_window.setLayout(audio_vbox)

        audioNames_button.clicked.connect(lambda: audioNames_window.exec())
        audio_holder = QHBoxLayout()
        audio_holder.addWidget(audioFolder_button)
        audio_holder.addWidget(audioNames_button)
        headerTexts_button = QPushButton("Header Texts")
        headerTexts_window = QDialog()
        headerTexts_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        headerTexts_window.setWindowTitle("Header Texts")

        header_tabs = QTabWidget()
        self.again_headerTexts_textEditor = QPlainTextEdit()
        self.again_headerTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        again_layout = QVBoxLayout()
        again_layout.addWidget(self.again_headerTexts_textEditor)
        again_tab = QWidget()
        again_tab.setLayout(again_layout)
        header_tabs.addTab(again_tab, "Again")
        self.hard_headerTexts_textEditor = QPlainTextEdit()
        self.hard_headerTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        hard_layout = QVBoxLayout()
        hard_layout.addWidget(self.hard_headerTexts_textEditor)
        hard_tab = QWidget()
        hard_tab.setLayout(hard_layout)
        header_tabs.addTab(hard_tab, "Hard")
        self.good_headerTexts_textEditor = QPlainTextEdit()
        self.good_headerTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        good_layout = QVBoxLayout()
        good_layout.addWidget(self.good_headerTexts_textEditor)
        good_tab = QWidget()
        good_tab.setLayout(good_layout)
        header_tabs.addTab(good_tab, "Good")
        self.easy_headerTexts_textEditor = QPlainTextEdit()
        self.easy_headerTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        easy_layout = QVBoxLayout()
        easy_layout.addWidget(self.easy_headerTexts_textEditor)
        easy_tab = QWidget()
        easy_tab.setLayout(easy_layout)
        header_tabs.addTab(easy_tab, "Easy")
        headers_vbox = QVBoxLayout()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Close)
        buttons.rejected.connect(headerTexts_window.close)
        headers_vbox.addWidget(header_tabs)
        headers_vbox.addWidget(buttons)
        headerTexts_window.setLayout(headers_vbox)

        headerTexts_button.clicked.connect(lambda: headerTexts_window.exec())
        windowTtitles_button = QPushButton("Window Title Texts")
        windowTitles_window = QDialog()
        windowTitles_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        windowTitles_window.setWindowTitle("Window Title Texts")

        windowTitle_tabs = QTabWidget()
        self.again_windowTitles_textEditor = QPlainTextEdit()
        self.again_windowTitles_textEditor.setWordWrapMode(QTextOption.NoWrap)
        again_layout = QVBoxLayout()
        again_layout.addWidget(self.again_windowTitles_textEditor)
        again_tab = QWidget()
        again_tab.setLayout(again_layout)
        windowTitle_tabs.addTab(again_tab, "Again")
        self.hard_windowTitles_textEditor = QPlainTextEdit()
        self.hard_windowTitles_textEditor.setWordWrapMode(QTextOption.NoWrap)
        hard_layout = QVBoxLayout()
        hard_layout.addWidget(self.hard_windowTitles_textEditor)
        hard_tab = QWidget()
        hard_tab.setLayout(hard_layout)
        windowTitle_tabs.addTab(hard_tab, "Hard")
        self.good_windowTitles_textEditor = QPlainTextEdit()
        self.good_windowTitles_textEditor.setWordWrapMode(QTextOption.NoWrap)
        good_layout = QVBoxLayout()
        good_layout.addWidget(self.good_windowTitles_textEditor)
        good_tab = QWidget()
        good_tab.setLayout(good_layout)
        windowTitle_tabs.addTab(good_tab, "Good")
        self.easy_windowTitles_textEditor = QPlainTextEdit()
        self.easy_windowTitles_textEditor.setWordWrapMode(QTextOption.NoWrap)
        easy_layout = QVBoxLayout()
        easy_layout.addWidget(self.easy_windowTitles_textEditor)
        easy_tab = QWidget()
        easy_tab.setLayout(easy_layout)
        windowTitle_tabs.addTab(easy_tab, "Easy")
        windowTitles_vbox = QVBoxLayout()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Close)
        buttons.rejected.connect(windowTitles_window.close)
        windowTitles_vbox.addWidget(windowTitle_tabs)
        windowTitles_vbox.addWidget(buttons)
        windowTitles_window.setLayout(windowTitles_vbox)

        windowTtitles_button.clicked.connect(lambda: windowTitles_window.exec())
        buttonTexts_button = QPushButton("Button Texts")
        buttonTexts_window = QDialog()
        buttonTexts_window.setWindowIcon(QIcon(addon_path + "/images/icon.png"))
        buttonTexts_window.setWindowTitle("Button Texts")

        button_tabs = QTabWidget()
        self.again_buttonTexts_textEditor = QPlainTextEdit()
        self.again_buttonTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        again_layout = QVBoxLayout()
        again_layout.addWidget(self.again_buttonTexts_textEditor)
        again_tab = QWidget()
        again_tab.setLayout(again_layout)
        button_tabs.addTab(again_tab, "Again")
        self.hard_buttonTexts_textEditor = QPlainTextEdit()
        self.hard_buttonTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        hard_layout = QVBoxLayout()
        hard_layout.addWidget(self.hard_buttonTexts_textEditor)
        hard_tab = QWidget()
        hard_tab.setLayout(hard_layout)
        button_tabs.addTab(hard_tab, "Hard")
        self.good_buttonTexts_textEditor = QPlainTextEdit()
        self.good_buttonTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        good_layout = QVBoxLayout()
        good_layout.addWidget(self.good_buttonTexts_textEditor)
        good_tab = QWidget()
        good_tab.setLayout(good_layout)
        button_tabs.addTab(good_tab, "Good")
        self.easy_buttonTexts_textEditor = QPlainTextEdit()
        self.easy_buttonTexts_textEditor.setWordWrapMode(QTextOption.NoWrap)
        easy_layout = QVBoxLayout()
        easy_layout.addWidget(self.easy_buttonTexts_textEditor)
        easy_tab = QWidget()
        easy_tab.setLayout(easy_layout)
        button_tabs.addTab(easy_tab, "Easy")
        buttons_vbox = QVBoxLayout()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Close)
        buttons.rejected.connect(buttonTexts_window.close)
        buttons_vbox.addWidget(button_tabs)
        buttons_vbox.addWidget(buttons)
        buttonTexts_window.setLayout(buttons_vbox)

        buttonTexts_button.clicked.connect(lambda: buttonTexts_window.exec())
        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(self.onApply)
        apply_button.clicked.connect(lambda: showInfo("<div style='color: red;\
        font-size: 15px;'> Changes will take effect after you restart anki. </div>", title="Review Pop-Up Settings"))
        apply_button.clicked.connect(lambda: self.hide())
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(lambda: self.hide())
        bottom_line = QHBoxLayout()
        bottom_line.addWidget(apply_button)
        bottom_line.addWidget(cancel_button)
        self.layout = QVBoxLayout()
        self.layout.addLayout(line1)
        self.layout.addLayout(line2)
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
        if C_show_onAgain:
            self.show_onAgain.setChecked(True)
        if C_show_onHard:
            self.show_onHard.setChecked(True)
        if C_show_onGood:
            self.show_onGood.setChecked(True)
        if C_show_onEasy:
            self.show_onEasy.setChecked(True)
        self.view_chance.setValue(C_popUp_chance)
        self.headerText_fontStyle.setCurrentFont(QFont(C_headerText_fontStyle))
        self.headerText_fontSize.setValue(C_headerText_fontSize)
        self.again_imageNames_textEditor.setPlainText("{}".format("\n".join(C_image_names_again)))
        self.hard_imageNames_textEditor.setPlainText("{}".format("\n".join(C_image_names_hard)))
        self.good_imageNames_textEditor.setPlainText("{}".format("\n".join(C_image_names_good)))
        self.easy_imageNames_textEditor.setPlainText("{}".format("\n".join(C_image_names_easy)))
        self.again_audioNames_textEditor.setPlainText("{}".format("\n".join(C_audio_names_again)))
        self.hard_audioNames_textEditor.setPlainText("{}".format("\n".join(C_audio_names_hard)))
        self.good_audioNames_textEditor.setPlainText("{}".format("\n".join(C_audio_names_good)))
        self.easy_audioNames_textEditor.setPlainText("{}".format("\n".join(C_audio_names_easy)))
        self.again_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_again)))
        self.hard_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_hard)))
        self.good_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_good)))
        self.easy_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_easy)))
        self.again_windowTitles_textEditor.setPlainText("{}".format("\n".join(C_window_titles_again)))
        self.hard_windowTitles_textEditor.setPlainText("{}".format("\n".join(C_window_titles_hard)))
        self.good_windowTitles_textEditor.setPlainText("{}".format("\n".join(C_window_titles_good)))
        self.easy_windowTitles_textEditor.setPlainText("{}".format("\n".join(C_window_titles_easy)))
        self.again_buttonTexts_textEditor.setPlainText("{}".format("\n".join(C_button_texts_again)))
        self.hard_buttonTexts_textEditor.setPlainText("{}".format("\n".join(C_button_texts_hard)))
        self.good_buttonTexts_textEditor.setPlainText("{}".format("\n".join(C_button_texts_good)))
        self.easy_buttonTexts_textEditor.setPlainText("{}".format("\n".join(C_button_texts_easy)))
    def onApply(self):
        conf = {
        "Show Header": self.header_checkbox.isChecked(),
        "Show Image": self.image_checkbox.isChecked(),
        "Play Audio": self.audio_checkbox.isChecked(),
        "Show on Again": self.show_onAgain.isChecked(),
        "Show on Hard": self.show_onHard.isChecked(),
        "Show on Good": self.show_onGood.isChecked(),
        "Show on Easy": self.show_onEasy.isChecked(),
        "Pop-Up Chance": self.view_chance.value(),
        "Header Text Font Style": self.headerText_fontStyle.currentFont().family(),
        "Header Text Font Size": self.headerText_fontSize.value(),
        "Image Names_ Again": self.again_imageNames_textEditor.toPlainText().split("\n"),
        "Image Names_ Hard": self.hard_imageNames_textEditor.toPlainText().split("\n"),
        "Image Names_ Good": self.good_imageNames_textEditor.toPlainText().split("\n"),
        "Image Names_ Easy": self.easy_imageNames_textEditor.toPlainText().split("\n"),
        "Audio Names_ Again": self.again_audioNames_textEditor.toPlainText().split("\n"),
        "Audio Names_ Hard": self.hard_audioNames_textEditor.toPlainText().split("\n"),
        "Audio Names_ Good": self.good_audioNames_textEditor.toPlainText().split("\n"),
        "Audio Names_ Easy": self.easy_audioNames_textEditor.toPlainText().split("\n"),
        "Header Texts_ Again": self.again_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Hard": self.hard_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Good": self.good_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Easy": self.easy_headerTexts_textEditor.toPlainText().split("\n"),
        "Window Titles_ Again": self.again_windowTitles_textEditor.toPlainText().split("\n"),
        "Window Titles_ Hard": self.hard_windowTitles_textEditor.toPlainText().split("\n"),
        "Window Titles_ Good": self.good_windowTitles_textEditor.toPlainText().split("\n"),
        "Window Titles_ Easy": self.easy_windowTitles_textEditor.toPlainText().split("\n"),
        "Button Texts_ Again": self.again_buttonTexts_textEditor.toPlainText().split("\n"),
        "Button Texts_ Hard": self.hard_buttonTexts_textEditor.toPlainText().split("\n"),
        "Button Texts_ Good": self.good_buttonTexts_textEditor.toPlainText().split("\n"),
        "Button Texts_ Easy": self.easy_buttonTexts_textEditor.toPlainText().split("\n")
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
