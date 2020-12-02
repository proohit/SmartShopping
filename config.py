import yaml


class DbConfig():
    def check_config(self, config_file):
        if 'db' not in config_file:
            raise AttributeError('No DB item in config')
        if not config_file['db']['host']:
            raise AttributeError('No host configured in config')
        if not config_file['db']['user']:
            raise AttributeError('No user configured in config')
        # if not config_file['db']['password']:
        #     raise AttributeError('No password configured in config')
        if not config_file['db']['port']:
            raise AttributeError('No port configured in config')
        if not config_file['db']['database']:
            raise AttributeError('No database configured in config')

    def __init__(self, config_file) -> None:
        self.check_config(config_file)
        self.host = config_file['db']['host']
        self.user = config_file['db']['user']
        self.password = config_file['db']['password']
        self.port = config_file['db']['port']
        self.database = config_file['db']['database']


class Config():
    def __init__(self) -> None:
        configfile = yaml.safe_load(open('config.yaml'))
        self.db = DbConfig(configfile)


config = Config()
