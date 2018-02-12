"""Connect to the MongoDB."""
from simage.tools.logger import log
from pymongo import MongoClient
from pprint import pprint
import config


class Mongo(object):
    def __init__(self):
        """Get database."""
        client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
        try:
            self.db = client[config.MONGO_DB]
        except ConnectionError:
            log("Failed to connecting MongoDB. HOST: %s, DB: %s" %
                (config.MONGO_HOST + config.MONGO_PORT, config.MONGO_DB))

    def files(self):
        """Get files collection."""
        files = self.db['files']
        return files

    def cluster(self):
        """Get cluster collection."""
        cluster = self.db['cluster']
        return cluster
