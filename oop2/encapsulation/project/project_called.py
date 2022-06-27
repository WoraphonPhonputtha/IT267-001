from condo import Condo

ideo = Condo('IDEO5',18,'Ladphroa',80,'Condo 20 Floors')
ideo.show()

from project import Project
home = Project('Ladawan',15,'Bang Yai')
home.show()
home.update_budget(30)
print(f'Budget : {home.get_budget()} MB')