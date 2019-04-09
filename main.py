import pyautogui, time

try:
    pyautogui.hotkey('win', 'r')
    pyautogui.hotkey('delete')
    pyautogui.typewrite('chrome')
    pyautogui.hotkey('enter')
    # pyautogui.hotkey('ctrl', 'l', interval=0.25)m.br
    pyautogui.click(50, 350)
    time.sleep(.1)
    pyautogui.typewrite('https://app.pontonow.com.br/login')
    pyautogui.hotkey('enter')
    time.sleep(.10)
    pyautogui.click(1000,550) # x , y
    # pyautogui.typewrite('oh que doidera')
    # pyautogui.hotkey('enter')

except KeyboardInterrupt:
    print('\nDone.')
