
# import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.bind("<Return>", self.add_task)
        self.root.bind("c", self.mark_as_completed)
        self.root.bind("d", self.delete_task)
        self.root.bind("<Escape>", self.close_app)

        self.task_list = tk.Listbox(root, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_as_completed)
        self.complete_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def mark_as_completed(self, event=None):
        selected_task = self.task_list.curselection()
        if selected_task:
            task = self.task_list.get(selected_task)
            self.task_list.delete(selected_task)
            self.task_list.insert(tk.END, f"[COMPLETED] {task}")

    def delete_task(self, event=None):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)

    def close_app(self, event=None):
        if messagebox.askokcancel("Close App", "Are you sure you want to close the app?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()