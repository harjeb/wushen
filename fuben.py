import sele
import json

class fub(sele.webutils):
    def init_j(self):
        j = json.load(open('config.json'))
        return j

    def init_s(self):
        a = sele.webutils()
        return a