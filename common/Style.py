from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, qconfig, FluentIconBase, getIconColor


class StyleSheet(StyleSheetBase, Enum):

    SETTING = 'setting_interface'

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme

        return f":/app/qss/{theme.value.lower()}/{self.value}.qss"


class MyIcon(FluentIconBase, Enum):
    """ Custom icons """

    KEY = 'key'
    LINK = 'link'
    NUMBER = 'number'
    PLAY = 'play'
    SERVER = 'server'
    TOOL = 'tool'

    def path(self, theme=Theme.AUTO):
        return f':/res/icons/{self.value}_{getIconColor(theme)}.svg'
