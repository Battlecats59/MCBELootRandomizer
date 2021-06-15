# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomizer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_randomizer(object):
    def setupUi(self, randomizer):
        if not randomizer.objectName():
            randomizer.setObjectName(u"randomizer")
        randomizer.resize(793, 600)
        self.centralwidget = QWidget(randomizer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_randomized_drops = QGroupBox(self.centralwidget)
        self.groupBox_randomized_drops.setObjectName(u"groupBox_randomized_drops")
        self.groupBox_randomized_drops.setEnabled(True)
        self.groupBox_randomized_drops.setGeometry(QRect(20, 220, 751, 111))
        self.gridLayoutWidget_7 = QWidget(self.groupBox_randomized_drops)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 20, 731, 83))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.option_randomized_common_hostile = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_common_hostile.setObjectName(u"option_randomized_common_hostile")
        self.option_randomized_common_hostile.setEnabled(True)

        self.gridLayout_7.addWidget(self.option_randomized_common_hostile, 1, 1, 1, 1)

        self.option_randomized_all = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_all.setObjectName(u"option_randomized_all")

        self.gridLayout_7.addWidget(self.option_randomized_all, 0, 0, 1, 1)

        self.option_randomized_common_friendly = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_common_friendly.setObjectName(u"option_randomized_common_friendly")

        self.gridLayout_7.addWidget(self.option_randomized_common_friendly, 1, 0, 1, 1)

        self.option_randomized_nether = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_nether.setObjectName(u"option_randomized_nether")

        self.gridLayout_7.addWidget(self.option_randomized_nether, 1, 2, 1, 1)

        self.option_randomized_rare_hostile = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_rare_hostile.setObjectName(u"option_randomized_rare_hostile")

        self.gridLayout_7.addWidget(self.option_randomized_rare_hostile, 2, 1, 1, 1)

        self.option_randomized_rare_friendly = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_rare_friendly.setObjectName(u"option_randomized_rare_friendly")

        self.gridLayout_7.addWidget(self.option_randomized_rare_friendly, 2, 0, 1, 1)

        self.option_randomized_end = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_end.setObjectName(u"option_randomized_end")

        self.gridLayout_7.addWidget(self.option_randomized_end, 2, 2, 1, 1)

        self.option_randomized_bosses = QCheckBox(self.gridLayoutWidget_7)
        self.option_randomized_bosses.setObjectName(u"option_randomized_bosses")

        self.gridLayout_7.addWidget(self.option_randomized_bosses, 0, 2, 1, 1)

        self.groupBox_general = QGroupBox(self.centralwidget)
        self.groupBox_general.setObjectName(u"groupBox_general")
        self.groupBox_general.setEnabled(True)
        self.groupBox_general.setGeometry(QRect(20, 90, 751, 111))
        self.gridLayoutWidget_10 = QWidget(self.groupBox_general)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 20, 731, 83))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_for_option_preset = QLabel(self.gridLayoutWidget_10)
        self.label_for_option_preset.setObjectName(u"label_for_option_preset")
        self.label_for_option_preset.setEnabled(True)

        self.horizontalLayout_17.addWidget(self.label_for_option_preset)

        self.option_preset = QComboBox(self.gridLayoutWidget_10)
        self.option_preset.setObjectName(u"option_preset")
        self.option_preset.setEnabled(True)

        self.horizontalLayout_17.addWidget(self.option_preset)


        self.gridLayout_11.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_spoiler_log = QHBoxLayout()
        self.horizontalLayout_spoiler_log.setObjectName(u"horizontalLayout_spoiler_log")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_for_option_version = QLabel(self.gridLayoutWidget_10)
        self.label_for_option_version.setObjectName(u"label_for_option_version")
        self.label_for_option_version.setEnabled(True)

        self.horizontalLayout_18.addWidget(self.label_for_option_version)

        self.option_version = QComboBox(self.gridLayoutWidget_10)
        self.option_version.setObjectName(u"option_version")
        self.option_version.setEnabled(True)

        self.horizontalLayout_18.addWidget(self.option_version)


        self.horizontalLayout_spoiler_log.addLayout(self.horizontalLayout_18)


        self.gridLayout_11.addLayout(self.horizontalLayout_spoiler_log, 1, 0, 1, 1)

        self.option_spoiler_log = QCheckBox(self.gridLayoutWidget_10)
        self.option_spoiler_log.setObjectName(u"option_spoiler_log")
        self.option_spoiler_log.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_11.addWidget(self.option_spoiler_log, 2, 0, 1, 1)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 751, 58))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.seed = QLineEdit(self.gridLayoutWidget)
        self.seed.setObjectName(u"seed")

        self.gridLayout.addWidget(self.seed, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.output_folder_browse_button = QPushButton(self.gridLayoutWidget)
        self.output_folder_browse_button.setObjectName(u"output_folder_browse_button")

        self.gridLayout.addWidget(self.output_folder_browse_button, 0, 7, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setToolTipDuration(-1)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.seed_button = QPushButton(self.gridLayoutWidget)
        self.seed_button.setObjectName(u"seed_button")

        self.gridLayout.addWidget(self.seed_button, 1, 7, 1, 1)

        self.output_folder = QLineEdit(self.gridLayoutWidget)
        self.output_folder.setObjectName(u"output_folder")

        self.gridLayout.addWidget(self.output_folder, 0, 1, 1, 1)

        self.groupBox_randomize = QGroupBox(self.centralwidget)
        self.groupBox_randomize.setObjectName(u"groupBox_randomize")
        self.groupBox_randomize.setEnabled(True)
        self.groupBox_randomize.setGeometry(QRect(20, 460, 751, 91))
        self.gridLayoutWidget_8 = QWidget(self.groupBox_randomize)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 20, 731, 61))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.randomize_button = QPushButton(self.gridLayoutWidget_8)
        self.randomize_button.setObjectName(u"randomize_button")

        self.gridLayout_8.addWidget(self.randomize_button, 1, 0, 1, 1)

        self.option_description = QLabel(self.gridLayoutWidget_8)
        self.option_description.setObjectName(u"option_description")
        self.option_description.setEnabled(True)
        self.option_description.setWordWrap(True)

        self.gridLayout_8.addWidget(self.option_description, 0, 0, 1, 1)

        self.groupBox_randomized_chests = QGroupBox(self.centralwidget)
        self.groupBox_randomized_chests.setObjectName(u"groupBox_randomized_chests")
        self.groupBox_randomized_chests.setEnabled(True)
        self.groupBox_randomized_chests.setGeometry(QRect(20, 350, 751, 91))
        self.gridLayoutWidget_9 = QWidget(self.groupBox_randomized_chests)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 20, 731, 61))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.option_randomized_end_chests = QCheckBox(self.gridLayoutWidget_9)
        self.option_randomized_end_chests.setObjectName(u"option_randomized_end_chests")

        self.gridLayout_9.addWidget(self.option_randomized_end_chests, 1, 2, 1, 1)

        self.option_randomized_overworld_chests = QCheckBox(self.gridLayoutWidget_9)
        self.option_randomized_overworld_chests.setObjectName(u"option_randomized_overworld_chests")

        self.gridLayout_9.addWidget(self.option_randomized_overworld_chests, 1, 0, 1, 1)

        self.option_randomized_nether_chests = QCheckBox(self.gridLayoutWidget_9)
        self.option_randomized_nether_chests.setObjectName(u"option_randomized_nether_chests")
        self.option_randomized_nether_chests.setEnabled(True)

        self.gridLayout_9.addWidget(self.option_randomized_nether_chests, 1, 1, 1, 1)

        self.option_randomized_all_chests = QCheckBox(self.gridLayoutWidget_9)
        self.option_randomized_all_chests.setObjectName(u"option_randomized_all_chests")

        self.gridLayout_9.addWidget(self.option_randomized_all_chests, 0, 0, 1, 1)

        randomizer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(randomizer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 20))
        randomizer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(randomizer)
        self.statusbar.setObjectName(u"statusbar")
        randomizer.setStatusBar(self.statusbar)

        self.retranslateUi(randomizer)

        QMetaObject.connectSlotsByName(randomizer)
    # setupUi

    def retranslateUi(self, randomizer):
        randomizer.setWindowTitle(QCoreApplication.translate("randomizer", u"randomizer", None))
        self.groupBox_randomized_drops.setTitle(QCoreApplication.translate("randomizer", u"What mob drops should be randomized?", None))
        self.option_randomized_common_hostile.setText(QCoreApplication.translate("randomizer", u"Common Hostile Overworld Mobs", None))
        self.option_randomized_all.setText(QCoreApplication.translate("randomizer", u"All Mobs", None))
        self.option_randomized_common_friendly.setText(QCoreApplication.translate("randomizer", u"Common Friendly/Neutral Overworld Mobs", None))
        self.option_randomized_nether.setText(QCoreApplication.translate("randomizer", u"Nether Mobs", None))
        self.option_randomized_rare_hostile.setText(QCoreApplication.translate("randomizer", u"Rare Hostile Overworld Mobs", None))
        self.option_randomized_rare_friendly.setText(QCoreApplication.translate("randomizer", u"Rare Friendly/Neutral Overworld Mobs", None))
        self.option_randomized_end.setText(QCoreApplication.translate("randomizer", u"End Mobs", None))
        self.option_randomized_bosses.setText(QCoreApplication.translate("randomizer", u"Bosses", None))
        self.groupBox_general.setTitle(QCoreApplication.translate("randomizer", u"General", None))
        self.label_for_option_preset.setText(QCoreApplication.translate("randomizer", u"Preset Setting", None))
        self.label_for_option_version.setText(QCoreApplication.translate("randomizer", u"Minecraft Version", None))
        self.option_spoiler_log.setText(QCoreApplication.translate("randomizer", u"Generate Spoiler Log", None))
        self.label_2.setText(QCoreApplication.translate("randomizer", u"Output Folder", None))
        self.output_folder_browse_button.setText(QCoreApplication.translate("randomizer", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("randomizer", u"Seed", None))
        self.seed_button.setText(QCoreApplication.translate("randomizer", u"New Seed", None))
        self.groupBox_randomize.setTitle(QCoreApplication.translate("randomizer", u"Randomize", None))
        self.randomize_button.setText(QCoreApplication.translate("randomizer", u"Randomize", None))
        self.option_description.setText("")
        self.groupBox_randomized_chests.setTitle(QCoreApplication.translate("randomizer", u"What chest loot should be randomized?", None))
        self.option_randomized_end_chests.setText(QCoreApplication.translate("randomizer", u"End Chests", None))
        self.option_randomized_overworld_chests.setText(QCoreApplication.translate("randomizer", u"Overworld Chests", None))
        self.option_randomized_nether_chests.setText(QCoreApplication.translate("randomizer", u"Nether Chests", None))
        self.option_randomized_all_chests.setText(QCoreApplication.translate("randomizer", u"All Chests", None))
    # retranslateUi

