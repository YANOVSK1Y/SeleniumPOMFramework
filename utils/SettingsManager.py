import os
import json
import platform

from utils.SingleTon import SingletonType
from utils.Logger import Logger


class SettingsManager(object, metaclass=SingletonType):

    def __init__(self, file_path=str()):

        system = platform.system()

        if system == 'Windows':
            file_path = os.getcwd() + '\\..\\settings.json'
        elif system == 'Linux' or 'Darwin':
            file_path = os.getcwd() + '/../settings.json'

        with open(file_path, 'r') as f:
            self.settings = json.loads(f.read())
            Logger.info("Import Settings for browser from file success")

    def get_value(self, field_title):
        try:
            return self.settings[field_title]
        except KeyError as e:
            Logger.warning(
                f'Can\'t import {field_title} from settings file. {e}')
            raise KeyError
