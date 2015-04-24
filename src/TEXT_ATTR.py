
class TEXT_ATTR():
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self._text

    def __add__(self, other):
        if isinstance(other, str):
            return self._text + str(other)
        else:
            return int(self._text) + int(other)

    def __int__(self):
        return int(self._text)

    def __sub__(self, other):
        return int(self._text) - int(other)

    def __mul__(self, other):
        return int(self._text) * int(other)

    def _getvalue(self):
        return self._text

    def _setvalue(self, value):
        self._text = str(value)

    text = property(_getvalue, _setvalue)