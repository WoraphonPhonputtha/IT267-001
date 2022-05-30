#สร้างฟังก์ชั่นเปิด-ปิดไฟ

#ฟังก์ชั่นเปิดไฟ
def turnon():
    global switch_status
    switch_status = True #เปลี่ยนสถานะเป็นเปิดไฟ

#ฟังก์ชั่นปิดไฟ
def turnoff():
    global switch_status
    switch_status = False #เปลี่ยนสถานะเป็นปิดไฟ

switch_status = False #ปิด

print(f'Status = {switch_status}')
turnon()
print(f'Status = {switch_status}')
turnoff()
print(f'Status = {switch_status}')
turnoff()
print(f'Status = {switch_status}')