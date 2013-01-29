from ConfigParser import ConfigParser

class QuickSyncConfigParser(ConfigParser):

    def __init__(self):
        ConfigParser.__init__(self, allow_no_value=True)

    def get_folders(self):
        folders = []
        for item in self.items('folders'):
            split = item[0].split(';')
            folders.append((split[0], split[1]))

        return folders
    
    def get_config(self):
        return dict(self.items('config'))
