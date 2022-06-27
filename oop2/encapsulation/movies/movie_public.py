class Movie:
    def __init__(self) -> None:
        self.title = ''
        self.year = 0
        self.genre = ''

    def add_movie(self,title:str,year:int,genre:str):
        self.title = title
        self.year = year
        self.genre = genre

    def get_movie(self):
        return self.title

if __name__ == '__main__':
    m = Movie()
    m.add_movie('Mulan', 2020, 'Action')
    print(f'Title : {m.get_movie()}')

    #access public attributes -> objec.tattribute
    print(f'Title : {m.title}')
    print(f'Year  : {m.year}')
    print(f'Genre : {m.genre}')