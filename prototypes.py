class User:
    def __init__(self, d=None):
        if d is not None:
            self.initdata = d
            for key, value in d.items():
                setattr(self, key, value)
    def __str__(self):
        fst = ""
        for key, value in self.initdata.items():
            fst += f"{key} - {value}\n"
        return fst