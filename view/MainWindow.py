from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, SplashScreen, NavigationItemPosition, FluentIcon

from common.Config import cfg
from common import resource
from view.SettingInterface import SettingInterface


class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()

        self.splash_screen: SplashScreen = None
        self.init_window()

        self.navigationInterface.setAcrylicEnabled(True)

        self.settingInterface = SettingInterface(self)

        self.init_navigation()
        self.splash_screen.finish()

    def init_window(self):
        self.resize(960, 780)
        self.setMinimumWidth(760)
        self.setWindowTitle('PyQt-Fluent-Widgets')

        self.setMicaEffectEnabled(cfg.get(cfg.mica_enabled))

        # create splash screen
        self.splash_screen = SplashScreen(self.windowIcon(), self)
        self.splash_screen.setIconSize(QSize(106, 106))
        self.splash_screen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def init_navigation(self):
        self.addSubInterface(
            self.settingInterface, FluentIcon.SETTING, self.tr('Settings'), NavigationItemPosition.BOTTOM)
