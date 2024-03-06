import tkinter as tk
import requests
import json
import os

class JSONPlaceholderRequester:
    def __init__(self, master):
        self.master = master
        master.title("JSON Placeholder Requester")
        
        self.id_label = tk.Label(master, text="Введите ID:")
        self.id_entry = tk.Entry(master)
        self.request_button = tk.Button(master, text="Запрос", command=self.make_request)
        self.result_text = tk.Text(master, height=10, width=50)
        self.save_button = tk.Button(master, text="Сохранить", command=self.save_result)
        
        self.id_label.grid(row=0, column=0, padx=10, pady=10)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.request_button.grid(row=0, column=2, padx=10, pady=10)
        self.result_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.save_button.grid(row=2, column=0, columnspan=3, pady=10)

    def make_request(self):
        try:
            id_value = int(self.id_entry.get())
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id_value}')
            self.result_text.delete(1.0, tk.END) 
            self.result_text.insert(tk.END, json.dumps(response.json(), indent=4))
        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Введите корректный ID (целое число).")

    def save_result(self):
        result = self.result_text.get(1.0, tk.END)
        if result.strip():
            id_value = self.id_entry.get()
            file_path = os.path.join('saved_results', f'result_{id_value}.json')
            with open(file_path, 'w') as file:
                file.write(result)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Результат сохранен в {file_path}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Нет данных для сохранения.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONPlaceholderRequester(root)
    root.mainloop()
