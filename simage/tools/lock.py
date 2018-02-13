from os import chmod
from stat import S_IRUSR
from filelock import SoftFileLock
from simage.tools.logger import log
from simage.tools.readThePath import ReadThePath


class LockFile(object):
    def __init__(self, path):
        self.path = path
        self.file_path = self.path
        self.lock_path = self.path + '.lock'
        content = ReadThePath(path)
        self.stable_file_path = content.dir() + 'stable.' + \
            content.name() + '.' + content.type()
        self.curing_file()

    def curing_file(self):
        """Curing a stable file: stable.[filename].[type] and it's read only by owner."""
        try:
            lock = SoftFileLock(self.lock_path, timeout=1)
            with lock:
                with open(self.file_path, "r") as file:
                    content = file.read(4096)
                with open(self.stable_file_path, 'w+') as file:
                    file.write(content)
                chmod(self.stable_file_path, S_IRUSR)
                log('Curing stable config file.')
        except FileNotFoundError:
            log('Unable to find the file to lock.')

