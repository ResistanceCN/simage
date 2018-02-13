class ReadThePath(object):
    def __init__(self, path):
        self.path = path
        self.path_list = self.path.split('/')

    def dir(self):
        """Get the file dir."""
        if self.path_list == ['']:
            file_dir = self.path
        else:
            file_dir = ''.join(self.path_list[:-1])
        return file_dir

    def name(self):
        if len(self.path_list) == 1:
            filename = '.'.join(self.path_list[0].split('.')[:-1])
        else:
            filename = '.'.join(self.path_list[-1].split('.')[:-1])
        return filename

    def type(self):
        if len(self.path_list) == 1:
            type = ''.join(self.path_list[0].split('.')[-1])
        else:
            type = ''.join(self.path_list[-1].split('.')[-1])
        return type

