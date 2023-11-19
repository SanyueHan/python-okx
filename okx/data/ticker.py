

class Ticker:
    def __init__(self, doc):
        self._last = float(doc['last'])  # 最新成交价

    def __repr__(self):
        return f"Ticker(last={self._last})"

    @property
    def last(self) -> float:
        return self._last
