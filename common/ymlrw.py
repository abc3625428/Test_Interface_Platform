import yaml
import os


path  = os.path.abspath(os.path.dirname(__file__)).replace('common','\\request_api\set.yml')
path1 = os.path.abspath(os.path.dirname(__file__)).replace('common',r'\setting\pdq_request_data_login.yml')



class YamlUtils:

    @staticmethod
    def load_yaml_file(file_path):
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
            return yaml_data

    @staticmethod
    def write_yaml_file(file_path, data):
        with open(file_path, 'w') as file:
            yaml.dump(data, file)

    @staticmethod
    def read_key_from_yaml_file(file_path, key):
        try:
            value = YamlUtils.load_yaml_file(file_path)
            return value.get(key, "")
        except FileNotFoundError:
            return ""

    @staticmethod
    def write_key_to_yaml_file(file_path,key, data):
        if key in data:
            YamlUtils.write_yaml_file(file_path, data)

    @staticmethod
    def change_yml_only_data(key, datavalue):
        with open(path1, "r") as fr:
            ya = yaml.safe_load(fr)
            print(ya)
        ya['DATA'][key] = datavalue
        with open(path1, 'w', encoding='utf-8') as fw:
            yaml.safe_dump(ya, fw, allow_unicode=True)

    @staticmethod
    def rade_yml_cookie_data(target):
        with open(path1, "r") as fr:
            ya = yaml.safe_load(fr)
            cookie = ya['DATA'][target]

            return cookie


