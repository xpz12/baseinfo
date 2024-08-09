import keyboard
import pyperclip

# Чтобы изменить копируемый текст на желаемый ,вставьте свой вместо Text 1.
texts = {
    '1': 'Text 1',
    '2': 'Text 2',
    '3': 'Text 3',
    '4': 'Text 4',
    '5': 'Text 5'
}

def copy_text(text_key):
    text = texts.get(text_key)
    if text:
        pyperclip.copy(text)
        print(f'Copied: {text}')

# Чтобы изменить хоткей ,вставьте свой вместо alt+1.
keyboard.add_hotkey('alt+1', copy_text, args=('1',))
keyboard.add_hotkey('alt+2', copy_text, args=('2',))
keyboard.add_hotkey('alt+3', copy_text, args=('3',))
keyboard.add_hotkey('alt+4', copy_text, args=('4',))
keyboard.add_hotkey('alt+5', copy_text, args=('5',))

# Программа работает бесконечно пока не нажмете esc
keyboard.wait('esc')
