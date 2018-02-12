from simage.tools.logger import log
from hashlib import md5


def md5_sum(path):
    """Get file md5sums."""
    hash_md5 = md5()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except FileNotFoundError:
        log("File does not found. Path: %s" % path)

    return hash_md5.hexdigest()


def md5_check(path, md5):
    """Check the file md5 value."""
    md5_check = md5_sum(path)
    if md5_check != md5:
        return False
    else:
        return True
