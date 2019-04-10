import pyautogui
# 1919, 1079 = pyautogui.size()

try:
    print('testando')
    # pyautogui.moveTo(900, 1060)
    # pyautogui.click()
    pyautogui.hotkey('win', 'r')
    pyautogui.hotkey('delete')
    pyautogui.typewrite('chrome')
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = 0.7
    # pyautogui.hotkey('alt', 'tab')
    # pyautogui.hotkey('ctrl', 'l')
    # pyautogui.PAUSE = 0.5
    pyautogui.moveTo(1000, 50)
    pyautogui.typewrite('https://www.google.com.br/')
    pyautogui.hotkey('enter')
    pyautogui.moveTo(1000, 500)
    pyautogui.PAUSE = 2.0
    pyautogui.click()


    
    # pyautogui.hotkey('ctrl', 'l', interval=0.25)m.br
    # pyautogui.click(50, 350)
    # pyautogui.PAUSE = 2.0
    # pyautogui.typewrite('https://app.pontonow.com.br/login')
    # pyautogui.hotkey('enter')
    # pyautogui.PAUSE = 6.5
    # pyautogui.move(1000,550) # x , y

except KeyboardInterrupt:
    print('\nDone.')
