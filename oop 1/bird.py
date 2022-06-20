#ตัวแปร Global variable
bird_type = 'Parrot'

class Bird:
    #class variable
    bird_name = 'Peter'

    def __init__(self,color) -> None:
        self.color = color

        #Local variable
        country = 'Thailand'
        print(country)
    
    def show(self):
        return f'{bird_type} {Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    #เรียกใช้ Global variable
    print(f'===== {bird_type} ======')
    my_bird = Bird('Red-Yellow')
    print(my_bird.show())

    #เรียก Class variable 
    #print(bird_name) Error

    #เรียกจากชื่อคลาส Class
    print(Bird.bird_name)

    #เรียกจากชื่อ Object
    print(my_bird.bird_name)

    #เรียกใช้ instance variable
    #print(Bird.color) Error

    #ชื่อวัตถุ.isinstance_variable
    print(my_bird.color)

