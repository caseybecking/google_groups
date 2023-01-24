import os
import configparser


def get_path():
    path = os.path.dirname(__file__)
    return path

def get_google_config_dict():
    path = get_path()
    config = configparser.RawConfigParser()
    config.read(path + '/config.cfg')
    if not hasattr(get_google_config_dict, 'config_dict'):
        get_google_config_dict.config_dict = dict(config.items('google'))
    return get_google_config_dict.config_dict