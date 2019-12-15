import pyautogui as pag

print(pag.position())

# pag.click(1179, 750, 1, 0, 'left')

# pag.moveRel(-100, -100, .5)
# pag.moveRel(50, 0, .5)

print("position of endpoint vpn")
print(pag.position())

pag.click(265, 747, 1, 0, 'left')
# pag.PAUSE = 10
pag.moveRel(0, -135, .5)
pag.moveRel(15, 0, .5)

print("position of endpoint vpn connect option")
print(pag.position())

# pag.click(1144, 515, 1, 0, 'right')

# pag.PAUSE = 10

# print(pag.KEYBOARD_KEYS)
pag.PAUSE = 10
pag.moveRel(-100, 100, 3)
# password here for connecting VPN 
pag.typewrite("", 1)
pag.hotkey('enter')
