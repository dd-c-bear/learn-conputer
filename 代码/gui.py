import pyautogui , time
b = 1
while b == 1:

    a = input('输入股票代码:')
    x=903
    y=591
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.typewrite(a)
    pyautogui.press('enter')
    time.sleep(1)
    x=1688
    y=543
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.typewrite(a)
    pyautogui.press('enter')
    time.sleep(1)
    x=1784
    y=1065
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.typewrite(a)
    pyautogui.press('enter')
    continue