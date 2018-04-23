from utils.serializers import Jsonable, Xmlable


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)