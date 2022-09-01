import yaml

config_file_dev = "C:/Users/HP/PycharmProjects/apiFramework/config/config.yml"

with open(config_file_dev, 'r')as stream:
    cfg = yaml.safe_load(stream)
    BASE_URL = cfg['base_url']

