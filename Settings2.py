#// auth_ Mamad
#// Copyright (c) 2020 - 2023 Mamad

from aqt.qt import *
from aqt.utils import showInfo
import aqt
from aqt import mw
import os
import platform
import subprocess
import webbrowser
from os.path import join, dirname

def refreshConfig():
    global C_show_header, C_show_image, C_play_audio, C_play_videoGif, C_show_onAgain, C_show_onHard, C_show_onGood, C_show_onEasy, C_popUp_chance, C_SA_popUp_chance, C_popUp_type, C_headerText_fontStyle, C_headerText_fontSize, C_header_texts_SA, C_header_texts_again, C_header_texts_hard, C_header_texts_good, C_header_texts_easy
    config = mw.addonManager.getConfig(__name__)
    C_show_header = config["Show Header"]
    C_show_image = config["Show Image"]
    C_play_audio = config["Play Audio"]
    C_play_videoGif = config["Play Video/Gif"]
    C_show_onAgain = config["Show on Again"]
    C_show_onHard = config["Show on Hard"]
    C_show_onGood = config["Show on Good"]
    C_show_onEasy = config["Show on Easy"]
    C_popUp_chance = config["Pop-Up Chance"]
    C_SA_popUp_chance = config["Show Answer Pop-Up Chance"]
    C_popUp_type = config["Pop-Up Type"]
    C_headerText_fontStyle = config["Header Text Font Style"]
    C_headerText_fontSize = config["Header Text Font Size"]
    C_header_texts_SA = config["Header Texts_ Show Answer"]
    C_header_texts_again = config["Header Texts_ Again"]
    C_header_texts_hard = config["Header Texts_ Hard"]
    C_header_texts_good = config["Header Texts_ Good"]
    C_header_texts_easy = config["Header Texts_ Easy"]

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
        self.setWindowIcon(QIcon(addon_path + "/icon.png"))

    def settings(self):
        addon_path = dirname(__file__)
        images = join(addon_path, 'user_files/images')
        audio = join(addon_path, 'user_files/audio')
        video_gif = join(addon_path, 'user_files/video_gif')
        def video_gif_state_changed():
            if self.videoGif_checkbox.isChecked():
                self.image_checkbox.setChecked(False)
                self.header_checkbox.setChecked(False)
        def image_state_changed():
            if self.image_checkbox.isChecked():
                self.videoGif_checkbox.setChecked(False)
        def header_state_changed():
            if self.header_checkbox.isChecked():
                self.videoGif_checkbox.setChecked(False)
        self.header_checkbox = QCheckBox("Header")
        self.header_checkbox.setFixedWidth(102)
        self.header_checkbox.setToolTip("""Shows a random line in \"Header Texts\" list.
        You can edit the list by pressing the \"Header Texts\" button down belw.""")
        self.header_checkbox.stateChanged.connect(header_state_changed)
        self.image_checkbox = QCheckBox("Image")
        self.image_checkbox.setFixedWidth(102)
        self.image_checkbox.setToolTip("""Shows a random image from images folder.
        You can add images by copying images to the \"images\" folder in add-on folder. open the folder by pressing \"Open Images Folder\" button down below.""")
        self.image_checkbox.stateChanged.connect(image_state_changed)
        self.videoGif_checkbox = QCheckBox("Video/Gif")
        self.videoGif_checkbox.setFixedWidth(102)
        self.videoGif_checkbox.setToolTip("""Plays a Video/gif from the \"Video/Gif\" folder in add-on folder.
        You can add videos/gifs by copying them to the \"Video/Gif\" folder in add-on folder. open the folder by pressing \"Open Video/Gif Folder\" button down below.""")
        self.videoGif_checkbox.stateChanged.connect(video_gif_state_changed)
        self.audio_checkbox = QCheckBox("Audio")
        self.audio_checkbox.setFixedWidth(102)
        self.audio_checkbox.setToolTip("""Plays a random audio from \"audio\" folder in add-on folder.
        You can add audio by copying them to the \"audio\" folder in add-on folder. open the folder by pressing \"Open Audio Folder\" button down below.""")
        line1 = QHBoxLayout()
        line1.addWidget(self.header_checkbox)
        line1.addWidget(self.image_checkbox)
        line1.addWidget(self.videoGif_checkbox)
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
        SA_view_chance_label = QLabel("Show Answer Pop-Up Chance")
        SA_view_chance_label.setToolTip("Changes the posibility of pop-up window popping up on show answer.\nSet on 0 to disable.")
        SA_view_chance_label.setFixedWidth(210)
        self.SA_view_chance = QSpinBox()
        self.SA_view_chance.setFixedWidth(210)
        self.SA_view_chance.setRange(0, 100)
        self.SA_view_chance.setSuffix("%")
        SA_view_chance_holder = QHBoxLayout()
        SA_view_chance_holder.addWidget(SA_view_chance_label)
        SA_view_chance_holder.addWidget(self.SA_view_chance)
        popUp_type_label = QLabel("Pop-Up Type")
        popUp_type_label.setToolTip("Changes the type of pop-up window.")
        popUp_type_label.setFixedWidth(210)
        self.popUp_type = QComboBox()
        self.popUp_type.setFixedWidth(210)
        self.popUp_type.addItems(["Random", "Ordered"])
        popUp_type_holder = QHBoxLayout()
        popUp_type_holder.addWidget(popUp_type_label)
        popUp_type_holder.addWidget(self.popUp_type)
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
        imagesFolder_button.clicked.connect(lambda: self.open_file(images))
        audioFolder_button = QPushButton("Open Audio Folder")
        audioFolder_button.clicked.connect(lambda: self.open_file(audio))
        videoGifFolder_button = QPushButton("Open Video/Gif Folder")
        videoGifFolder_button.clicked.connect(lambda: self.open_file(video_gif))
        headerTexts_button = QPushButton("Header Texts")
        headerTexts_window = QDialog()
        headerTexts_window.setWindowIcon(QIcon(addon_path + "/icon.png"))
        headerTexts_window.setWindowTitle("Header Texts")

        header_tabs = QTabWidget()
        self.SA_headerTexts_textEditor = QPlainTextEdit()
        self.SA_headerTexts_textEditor.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        SA_layout = QVBoxLayout()
        SA_layout.addWidget(self.SA_headerTexts_textEditor)
        SA_tab = QWidget()
        SA_tab.setLayout(SA_layout)
        header_tabs.addTab(SA_tab, "Show Answer")
        self.again_headerTexts_textEditor = QPlainTextEdit()
        self.again_headerTexts_textEditor.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        again_layout = QVBoxLayout()
        again_layout.addWidget(self.again_headerTexts_textEditor)
        again_tab = QWidget()
        again_tab.setLayout(again_layout)
        header_tabs.addTab(again_tab, "Again")
        self.hard_headerTexts_textEditor = QPlainTextEdit()
        self.hard_headerTexts_textEditor.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        hard_layout = QVBoxLayout()
        hard_layout.addWidget(self.hard_headerTexts_textEditor)
        hard_tab = QWidget()
        hard_tab.setLayout(hard_layout)
        header_tabs.addTab(hard_tab, "Hard")
        self.good_headerTexts_textEditor = QPlainTextEdit()
        self.good_headerTexts_textEditor.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        good_layout = QVBoxLayout()
        good_layout.addWidget(self.good_headerTexts_textEditor)
        good_tab = QWidget()
        good_tab.setLayout(good_layout)
        header_tabs.addTab(good_tab, "Good")
        self.easy_headerTexts_textEditor = QPlainTextEdit()
        self.easy_headerTexts_textEditor.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        easy_layout = QVBoxLayout()
        easy_layout.addWidget(self.easy_headerTexts_textEditor)
        easy_tab = QWidget()
        easy_tab.setLayout(easy_layout)
        header_tabs.addTab(easy_tab, "Easy")
        headers_vbox = QVBoxLayout()
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(headerTexts_window.close)
        headers_vbox.addWidget(header_tabs)
        headers_vbox.addWidget(buttons)
        headerTexts_window.setLayout(headers_vbox)
        headerTexts_button.clicked.connect(lambda: headerTexts_window.exec())

        contactMe_button = QPushButton("Contant Me")
        contactMe_button.clicked.connect(lambda: webbrowser.open('https://noobj2.t.me'))
        reportIssue_button = QPushButton("Report an Issue")
        reportIssue_button.clicked.connect(lambda: webbrowser.open('https://github.com/noobj2/Anki-Review-PopUp/issues/new'))
        likeAddon_button = QPushButton("Like this Add-on")
        likeAddon_button.clicked.connect(lambda: webbrowser.open('https://ankiweb.net/shared/review/976516370'))
        contact_report_line = QHBoxLayout()
        contact_report_line.addWidget(contactMe_button)
        contact_report_line.addWidget(likeAddon_button)
        contact_report_line.addWidget(reportIssue_button)
        
        changeLog_window = QDialog()
        changeLog_window.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowMinimizeButtonHint)
        changeLog_window.setWindowTitle("Changelog")
        changeLog_button = QPushButton("Show Changelog")
        self.changeLog_webView = QWebEngineView()
        self.loadChangeLog()
        changeLog_layout = QVBoxLayout()
        changeLog_layout.addWidget(self.changeLog_webView)
        changeLog_window.setLayout(changeLog_layout)
        changeLog_button.clicked.connect(lambda: changeLog_window.exec())
        changelog_like_line = QHBoxLayout()
        changelog_like_line.addWidget(changeLog_button)
        
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
        self.layout.addLayout(SA_view_chance_holder)
        self.layout.addLayout(popUp_type_holder)
        self.layout.addLayout(header_fontStyle_holder)
        self.layout.addLayout(header_fontSize_holder)
        self.layout.addWidget(imagesFolder_button)
        self.layout.addWidget(audioFolder_button)
        self.layout.addWidget(videoGifFolder_button)
        self.layout.addWidget(headerTexts_button)
        self.layout.addLayout(contact_report_line)
        self.layout.addLayout(changelog_like_line)
        self.layout.addLayout(bottom_line)
    def loadChangeLog(self):
        addon_path = dirname(__file__)
        file = "{}/changelog.html".format(addon_path)
        with open(file, 'r') as f:
            html = f.read()
            self.changeLog_webView.setHtml(html)
    def loadCurrent(self):
        if C_show_header:
            self.header_checkbox.setChecked(True)
        if C_show_image:
            self.image_checkbox.setChecked(True)
        if C_play_audio:
            self.audio_checkbox.setChecked(True)
        if C_play_videoGif:
            self.videoGif_checkbox.setChecked(True)
        if C_show_onAgain:
            self.show_onAgain.setChecked(True)
        if C_show_onHard:
            self.show_onHard.setChecked(True)
        if C_show_onGood:
            self.show_onGood.setChecked(True)
        if C_show_onEasy:
            self.show_onEasy.setChecked(True)
        self.view_chance.setValue(C_popUp_chance)
        self.SA_view_chance.setValue(C_SA_popUp_chance)
        self.popUp_type.setCurrentIndex(C_popUp_type)
        self.headerText_fontStyle.setCurrentFont(QFont(C_headerText_fontStyle))
        self.headerText_fontSize.setValue(C_headerText_fontSize)
        self.SA_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_SA)))
        self.again_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_again)))
        self.hard_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_hard)))
        self.good_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_good)))
        self.easy_headerTexts_textEditor.setPlainText("{}".format("\n".join(C_header_texts_easy)))
    def onApply(self):
        conf = {
        "Show Header": self.header_checkbox.isChecked(),
        "Show Image": self.image_checkbox.isChecked(),
        "Play Audio": self.audio_checkbox.isChecked(),
        "Play Video/Gif": self.videoGif_checkbox.isChecked(),
        "Show on Again": self.show_onAgain.isChecked(),
        "Show on Hard": self.show_onHard.isChecked(),
        "Show on Good": self.show_onGood.isChecked(),
        "Show on Easy": self.show_onEasy.isChecked(),
        "Pop-Up Chance": self.view_chance.value(),
        "Show Answer Pop-Up Chance": self.SA_view_chance.value(),
        "Pop-Up Type": self.popUp_type.currentIndex(),
        "Header Text Font Style": self.headerText_fontStyle.currentFont().family(),
        "Header Text Font Size": self.headerText_fontSize.value(),
        "Header Texts_ Show Answer": self.SA_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Again": self.again_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Hard": self.hard_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Good": self.good_headerTexts_textEditor.toPlainText().split("\n"),
        "Header Texts_ Easy": self.easy_headerTexts_textEditor.toPlainText().split("\n")
        }
        mw.addonManager.writeConfig(__name__, conf)
        refreshConfig()
    def open_file(self, path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

def open_settings():
    Settings2 = Settings()
    Settings2.exec()
settings = QAction('Review Pop-Up Settings', mw)
settings.triggered.connect(open_settings)
mw.form.menuTools.addAction(settings)
mw.addonManager.setConfigAction(__name__, open_settings)
