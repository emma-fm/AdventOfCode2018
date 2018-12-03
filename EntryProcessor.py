import os.path as p
class EntryProcessor:

    @staticmethod
    def getEntryArray(entry_file):
        dirname = p.dirname(__file__)
        file = open(p.join(dirname, entry_file), "r")
        lines = file.read()
        lines = lines.split("\n")
        return lines