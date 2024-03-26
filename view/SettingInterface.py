from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel
from qfluentwidgets import ScrollArea, ExpandLayout, SettingCardGroup, FolderListSettingCard, InfoBar, PushSettingCard, \
    FluentIcon

from common.Config import cfg
from common.Style import StyleSheet


class SettingInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scroll_widget = QWidget()
        self.expand_layout = ExpandLayout(self.scroll_widget)

        # title label
        self.title_label = QLabel(self.tr("Settings"), self)

        # grobid setting
        self.grobid_group = SettingCardGroup(
            self.tr("Grobid Setting"), self.scroll_widget
        )
        self.grobid_server_card = PushSettingCard(
            self.tr('Edit'),
            FluentIcon.DOWNLOAD,
            self.tr('Reprinter ID'),
            cfg.get(cfg.grobid_server),
            self.grobid_group
        )

        self.__init_widget()

    def __init_widget(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setWidget(self.scroll_widget)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')

        # initialize qss sheet
        self.scroll_widget.setObjectName('scrollWidget')
        self.title_label.setObjectName('titleLabel')
        StyleSheet.SETTING.apply(self)

        # initialize layout
        self.__init_layout()
        # self.__connectSignalToSlot()

    def __init_layout(self):
        self.title_label.move(36, 30)

        # add cards to group
        self.grobid_group.addSettingCard(self.grobid_server_card)

        # add setting card group to layout
        self.expand_layout.setSpacing(28)
        self.expand_layout.setContentsMargins(36, 10, 36, 0)
        self.expand_layout.addWidget(self.grobid_group)

    def __showRestartTooltip(self):
        """ show restart tooltip """
        InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Configuration takes effect after restart'),
            duration=1500,
            parent=self
        )
