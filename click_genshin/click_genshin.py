import pyautogui
import keyboard
import time

# Pressiona Alt+Tab para trocar de janelas
pyautogui.hotkey('alt', 'tab')

# Define as coordenadas do local onde deseja clicar repetidamente
x, y = 1421, 768

# Função para verificar se uma tecla específica foi pressionada
def is_key_pressed():
    return keyboard.is_pressed('p')

# Loop que clica no local especificado até a tecla ser pressionada
while not is_key_pressed():
    time.sleep(2)
    pyautogui.click(x, y)
