import time
import pyautogui

def move_scroll():
    while True:
        print("Moviendo el scroll...")
        pyautogui.scroll(100)
        time.sleep(1)
        pyautogui.scroll(-100)
        print("Esperando...")
        time.sleep(100)

if __name__ == "__main__":
    move_scroll()