import tkinter as tk
from tkinter import messagebox

class TextCopyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый копировщик")
        self.root.geometry("800x450")

        # Создаем фрейм для надписи и кнопок
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Создаем надпись над кнопками
        self.label = tk.Label(
            self.frame,
            text="Нажмите на кнопку, чтобы скопировать текст",
            font=("Arial", 7),
            fg="#808080",
        )
        self.label.pack(pady=5)

        # Создаем фрейм для кнопок
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(pady=10)

        # Создаем кнопки с привязанным текстом
        self.buttons = [
            {"text": "Кнопка 1", "copy_text": "Текст для копирования 1"}, # После copy_text поменять текст на желаемый для копирования
            {"text": "Кнопка 2", "copy_text": "Текст для копирования 2"},
            {"text": "Кнопка 3", "copy_text": "Текст для копирования 3"},
        ]

        self.button_widgets = []
        for button in self.buttons:
            button_widget = tk.Button(
                self.button_frame,
                text=button["text"],
                command=lambda copy_text=button["copy_text"], button_widget=None: self.copy_text(copy_text, button_widget),
                width=20,
                height=2,
                bg="#007bff",
                fg="#ffffff",
                font=("Arial", 12),
            )
            button_widget.pack(pady=10)
            self.button_widgets.append(button_widget)

        for i, button_widget in enumerate(self.button_widgets):
            button_widget.config(command=lambda copy_text=self.buttons[i]["copy_text"], button_widget=button_widget: self.copy_text(copy_text, button_widget))

    def copy_text(self, text, button_widget):
        # Меняем текст кнопки на время
        original_text = button_widget.cget("text")
        button_widget.config(text="Текст скопирован")

        # Копируем текст в буфер обмена
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

        # Возвращаем текст кнопки обратно через 1 секунду
        self.root.after(1000, lambda button_widget=button_widget, original_text=original_text: button_widget.config(text=original_text))

        # Показываем информационное сообщение
        messagebox.showinfo("Текст скопирован", f"Текст '{text}' скопирован в буфер обмена")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextCopyApp(root)
    root.mainloop()