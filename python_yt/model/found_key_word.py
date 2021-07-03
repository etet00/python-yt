class FoundKeyWord:
    def __init__(self, yt, subtitle, time):
        self.yt = yt
        self.subtitle = subtitle
        self.time = time

    def __str__(self):
        return "<Found(" + str(self.yt) + ")>"

    def __repr__(self):
        contain=":".join([
            "yt=" + str(self.yt),
            "subtitle=" + str(self.subtitle),
            "time=" + str(self.time),
        ])
        return "<Found(" + contain + ")>"
