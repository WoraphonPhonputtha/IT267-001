from movie_protected import Movie

class Documentary(Movie):
    def __init__(self) -> None:
        super().__init__()
        self.channel = None #public

    def add_channel(self,channel:str):
        self.channel = channel
