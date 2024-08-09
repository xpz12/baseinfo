import keyboard
import pyperclip

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

keyboard.add_hotkey('alt+1', copy_text, args=('1',))
keyboard.add_hotkey('alt+2', copy_text, args=('2',))
keyboard.add_hotkey('alt+3', copy_text, args=('3',))
keyboard.add_hotkey('alt+4', copy_text, args=('4',))
keyboard.add_hotkey('alt+5', copy_text, args=('5',))

keyboard.wait('esc')
