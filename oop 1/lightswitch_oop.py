#lightswitch_oop
class LightSwitch():
    def _init_(self) -> None:
        self.switch_status = False

    def turnon(self):
        self.switch_status = True

    def turnoff(self):
        self.switch_status = False

    def show(self):
        print(f"Status = {self.switch_status}")

#สร้างวัตถุ (Object) จากแม่พิมพ์ (Class)
switch_obj = LightSwitch()

#เรียกใช้เมธอด (ฟังก์ชั่น) 
switch_obj.show()
switch_obj.turnon()
switch_obj.show()
switch_obj.turnoff()
switch_obj.show()
switch_obj.turnoff()
switch_obj.show()