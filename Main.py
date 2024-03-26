# enable dpi scale
import os
import sys

from PySide6.QtCore import Qt, QTranslator
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

from Path import BASE_DIR
from common.Config import cfg
from view.MainWindow import MainWindow

if cfg.get(cfg.dpi_scale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

# create application
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

# internationalization
locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)
gallery_translator = QTranslator()
gallery_translator.load(locale, '', '', f':/app/i18n')

app.installTranslator(translator)
app.installTranslator(gallery_translator)

# create main window
w = MainWindow()
w.show()

app.exec()
