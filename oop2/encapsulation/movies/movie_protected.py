class Movie:
    def __init__(self) -> None:
        #protected attribute
        self._title = ''
        self._year = 0
        self._genre = ''
        self._rating = 6

    def _add_movie(self,title,year,genre,rating=6):
        self._title = title
        self._year = year
        self._genre = genre
        self._rating = rating

    def _get_movie(self):
        print(f'Title : {self._title}\nYear : {self._year}\nRating : {self._rating}')




