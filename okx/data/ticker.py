

class Ticker:
    def __init__(self, last: float):
        self._last = last

    def __repr__(self):
        return f"Ticker(last={self._last})"

    @classmethod
    def from_json(cls, data) -> 'Ticker':
        return cls(last=float(data['last']))

    @property
    def last(self) -> float:
        return self._last
