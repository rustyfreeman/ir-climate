
class Resolver:
    def __init__(self, db):
        self.db = db

    def get_code(self, mode, temp=None):
        c = self.db["commands"]

        if mode == "off":
            return c["off"]["code"]

        if mode == "cool":
            return c["cool"]["auto"][temp]["code"]

        if mode == "heat":
            return c["heat"]["auto"][temp]["code"]

        if mode == "dry":
            return c["dry"]["code"]

        if mode == "fan":
            return c["fan"]["auto"]["code"]

        if mode == "auto":
            return c["auto"]["code"]

        raise ValueError(mode)
