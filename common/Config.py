import sys
from enum import Enum

from PySide6.QtCore import QLocale
from qfluentwidgets import (
    ConfigSerializer, QConfig, ConfigItem, BoolValidator, OptionsConfigItem, OptionsValidator,
    RangeValidator, Theme, qconfig, RangeConfigItem
)


class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.HongKong)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


def is_win11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


class Config(QConfig):
    """Config of grobid"""
    grobid_server = ConfigItem("Grobid", "Grobid Server", "")
    batch_size = RangeConfigItem("Grobid", "Batch Size", 100, RangeValidator(64, 128))
    sleep_time = RangeConfigItem("Grobid", "Sleep Time", 5, RangeValidator(5, 30))
    timeout = RangeConfigItem("Grobid", "Timeout", 60, RangeValidator(30, 120))

    """ Config of application """
    # main window
    mica_enabled = ConfigItem("MainWindow", "MicaEnabled", is_win11(), BoolValidator())
    dpi_scale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    language = OptionsConfigItem(
        "MainWindow", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)

    # software update
    checkUpdateAtStartUp = ConfigItem("Update", "CheckUpdateAtStartUp", True, BoolValidator())


cfg = Config()
cfg.themeMode.value = Theme.AUTO
qconfig.load('../config/config.json', cfg)
