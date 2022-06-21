import os
import sys
import random

from PySide2.QtWidgets import QMainWindow, QApplication, QAbstractButton, QComboBox, QSpinBox, QListView, QLineEdit, QCheckBox, \
    QRadioButton, QFileDialog, QMessageBox, QErrorMessage
from PySide2.QtCore import QFile, Qt, QTimer, QEvent, QStringListModel
from yaml.loader import FullLoader

from gui.ui_randomizer import Ui_randomizer
from randoscript import randomize
from paths import RANDO_ROOT_PATH

import yaml

class randomizer(QMainWindow):
    def __init__(self):
        super(randomizer, self).__init__()

        self.ui = Ui_randomizer()
        self.ui.setupUi(self)

        self.setWindowTitle("MCBE Loot Randomizer")

        self.ui.output_folder_browse_button.clicked.connect(self.browse_for_output_dir)
        self.ui.seed_button.clicked.connect(self.gen_new_seed)
        self.ui.randomize_button.clicked.connect(self.randomize)
        #self.set_option_description(None)

        self.options = {'output_folder': None, 'seed': -1}

        self.override_ui_options = [
            "output_folder",
            "output_folder_browse_button",
            "seed",
            "seed_button",
            "randomize_button"
        ]

        self.init_settings()

    def gen_new_seed(self):
        self.ui.seed.setText(str(random.randrange(0, 1_000_000)))

    def browse_for_output_dir(self):

        if self.ui.output_folder.text():
            default_dir = self.ui.output_folder.text()
        else:
            default_dir = None

        output_folder = QFileDialog.getExistingDirectory(self, "Select output folder", default_dir)
        if not output_folder:
            return
        self.ui.output_folder.setText(output_folder)
    
    def init_settings(self):

        if os.path.isdir(os.path.expanduser('~/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs')):
            default_dir = os.path.expanduser('~/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs')
            default_dir = default_dir.replace('\\', '/')
        else:
            self.randomization_complete = QMessageBox(self)
            self.randomization_complete.setText('Could not find the MCBE behavior pack output directory. Please ensure that you have MCBE installed.')
            self.randomization_complete.setWindowTitle('Could not find folder')
            self.randomization_complete.show()
            default_dir = None

        self.help_descriptions = {}
        self.ui_options = []

        self.ui.output_folder.setText(default_dir)
        self.ui.seed.setText('-1')

        with (RANDO_ROOT_PATH / 'gui/options.yaml').open('r') as optf:
            self.option_data = yaml.load(optf, Loader=FullLoader)

        for opt in self.option_data:
            widget = getattr(self.ui, opt['ui'])
            widget.installEventFilter(self)
            widget.setEnabled(opt['enabled'])

            self.help_descriptions[opt['ui']] = opt['description']

            if opt['ui'] in self.override_ui_options:
                continue

            self.ui_options.append(opt)
            self.options[opt['option']] = opt['default']

            if isinstance(widget, QAbstractButton):
                widget.setChecked(opt['default'])
                widget.clicked.connect(self.update_settings)
                if opt['option'].startswith('randomized_all'):
                    widget.clicked.connect(self.update_ui)
            elif isinstance(widget, QComboBox):
                for option_val in opt['choices']:
                    widget.addItem(str(option_val))
                widget.setCurrentIndex(opt['choices'].index(opt['default']))
                widget.currentIndexChanged.connect(self.update_settings)
                if opt['option'] == 'preset':
                    widget.currentIndexChanged.connect(self.update_preset)
            elif isinstance(widget, QListView):
                pass
            elif isinstance(widget, QSpinBox):
                if 'min' in opt:
                    widget.setMinimum(opt['min'])
                if 'max' in opt:
                    widget.setMaximum(opt['max'])
                widget.setValue(opt['default'])
                widget.valueChanged.connect(self.update_settings)

    def randomize(self):

        rdir = self.ui.output_folder.text()
        rseed = self.ui.seed.text()

        if os.path.isdir(rdir) == False:
            err = "Could not find output directory!"
            self.on_error(err)
            return

        if rseed == '-1':
            rseed = str(random.randrange(0, 1_000_000))
        else:
            try:
                v = int(rseed)
            except ValueError:
                rseed = str(random.randrange(0, 1_000_000))

        self.update_settings()
        self.options['output_folder'] = rdir
        self.options['seed'] = rseed
    
        (self.randomization_return, self.r_options) = randomize.__randomize__(self, self.options)
        self.rhash = self.r_options['hash']
        self.rpreset = self.r_options['preset']
        self.rpermalink = self.r_options['permalink']

        if self.randomization_return == True:
            self.randomization_complete = QMessageBox(self)
            self.randomization_complete.setText(f'Randomization complete!\nSeed: {rseed}\nRando hash: {self.rhash}\nSettings: {self.rpreset} [Permalink: {self.rpermalink}]')
            self.randomization_complete.setWindowTitle('Randomization Complete')
            self.randomization_complete.show()
        else:
            self.randomization_error = QErrorMessage(self)
            self.randomization_error.showMessage('Randomization failed. Please try again and report this if it continues.')
            
    def eventFilter(self, target, event):
        if event.type() == QEvent.Enter:
            ui_name = target.objectName()

            if self.help_descriptions[ui_name]:
                self.set_option_description(self.help_descriptions[ui_name])

            return True
        elif event.type() == QEvent.Leave:
            self.set_option_description(None)
            return True

        return QMainWindow.eventFilter(self, target, event)

    def set_option_description(self, new_description):
        if new_description is None:
            self.ui.option_description.setText("(Hover over an option to see a description of what it does)")
            self.ui.option_description.setStyleSheet("color: grey;")
        else:
            self.ui.option_description.setText(new_description)
            self.ui.option_description.setStyleSheet("")

    def update_settings(self):
        for opt in self.ui_options:
            widget = getattr(self.ui, opt['ui'])

            if isinstance(widget, QAbstractButton):
                self.options[opt['option']] = widget.isChecked()
            elif isinstance(widget, QComboBox):
                self.options[opt['option']] = widget.currentText()
            elif isinstance(widget, QListView):
                pass # no list boxes
            elif isinstance(widget, QSpinBox):
                self.options[opt['option']] = widget.value()

    def update_ui(self):
        if self.ui.option_randomized_all.isChecked() == True:
            for opt in self.option_data:
                widget = getattr(self.ui, opt['ui'])
                if opt['ui'].startswith('option_randomized_') and not opt['ui'].endswith('chests') and opt['ui'] != 'option_randomized_all':
                    widget.setChecked(True)
                    widget.setEnabled(False)
        else:
            for opt in self.option_data:
                widget = getattr(self.ui, opt['ui'])
                if opt['ui'].startswith('option_randomized_') and not opt['ui'].endswith('chests') and opt['ui'] != 'option_randomized_all':
                    widget.setEnabled(True)

        if self.ui.option_randomized_all_chests.isChecked() == True:
            for opt in self.option_data:
                widget = getattr(self.ui, opt['ui'])
                if opt['ui'].startswith('option_randomized_') and opt['ui'].endswith('chests') and not opt['ui'] == 'option_randomized_all_chests':
                    widget.setChecked(True)
                    widget.setEnabled(False)
        else:
            for opt in self.option_data:
                widget = getattr(self.ui, opt['ui'])
                if opt['ui'].startswith('option_randomized_') and opt['ui'].endswith('chests') and not opt['ui'] == 'option_randomized_all_chests':
                    widget.setEnabled(True)

    def update_preset(self):
        with (RANDO_ROOT_PATH / 'gui/preset_options.yaml').open('r') as preset_opts:
            self.preset_options = yaml.load(preset_opts, Loader=FullLoader)
        
        if not self.preset_options[self.ui.option_preset.currentText()]:
            raise Exception("Invalid selection! This error should not occur. [main_UI.py 187]")

        for optset in self.preset_options[self.ui.option_preset.currentText()]:
            widget = getattr(self.ui, optset['ui'])
            
            widget.setEnabled(optset['enabled'])

            if 'value' in optset:
                if isinstance(widget, QAbstractButton):
                    widget.setChecked(optset['value'])
                elif isinstance(widget, QComboBox):
                    widget.setCurrentText(optset['value'])
                elif isinstance(widget, QListView):
                    pass # not impletmented
                elif isinstance(widget, QSpinBox):
                    widget.setValue(optset['value'])
                elif isinstance(widget, QLineEdit):
                    widget.setText(optset['value'])

    def on_error(self, message):
        self.error_msg = QErrorMessage(self)
        self.error_msg.showMessage(message)

def run_randomizer_UI():
    app = QApplication([])
    widget = randomizer()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_randomizer_UI()
