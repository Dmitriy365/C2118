
   class CurrencyConverter:
       def __init__(self):
           self.usd_rate = self.get_usd_rate()

       def get_usd_rate(self):
           url = 'URL'
import tkinter as tk
from tkinter import messagebox

class CurrencyConverterApp:
       def __init__(self, master):
           self.converter = CurrencyConverter()
           self.master = master
           master.title("Конвертер валюты")

           self.label = tk.Label(master, text="Введите сумму вашей валюты:")
           self.label.pack()

           self.amount_entry = tk.Entry(master)
           self.amount_entry.pack()

           self.convert_button = tk.Button(master, text="Конвертировать", command=self.convert)
           self.convert_button.pack()

           self.result_label = tk.Label(master, text="")
           self.result_label.pack()

       def convert(self):
           try:
               amount = float(self.amount_entry.get())
               result = self.converter.convert(amount)
               self.result_label.config(text=f"{amount} вашей валюты = {result:.2f} USD")
           except ValueError:messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")
if __name__ == "__main__":
       root = tk.Tk()
       app = CurrencyConverterApp(root)
       root.mainloop()