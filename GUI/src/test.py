import pyautogui as pag

# current position of mouse
print(pag.position())

# size of screen
print(pag.size())

pag.moveTo(1194, 190)
pag.PAUSE = 10
pag.moveTo(100, 100)
pag.PAUSE = 2

# move mouse 100 by 100 positions in 2 secs from current position
pag.moveRel(100, 100, 2)

pag.moveTo(1267, 56)
pag.click(1267, 56, 1, 0, 'left')
