class Movie:
    def __init__(self,title,year,genre) -> None:
        #Private attribute
        self.__title = title
        self.__year = year
        self.__genre = genre
    
    #private method
    def __get_movie(self):
        print(f'Title : {self.__title}\nGenre : {self.__genre}')
    
    #เตรียม Public สำหรับการเข้าถึง Private method
    def print_detail(self):
        self.__get_movie()


    