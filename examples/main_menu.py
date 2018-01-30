#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

import betterdialogs as bd

class DateTest(bd.DateDialog):
    def execute(self):
        bd.DateDialog.execute(self)
        print("TEST:")
        print(self.datestamp)

class Main(bd.MainFrame):
    def content(self, master):
        self.button_example = ttk.Button(
            master,
            text = "Example",
            command = self.on_click_example
        )
        self.button_example2 = tk.Button(
            master,
            text = "Example Two",
            command = self.on_click_example
        )

        # Pack widgets into content frame
        self.button_example.pack(padx=2, pady=2, fill="x")
        self.button_example2.pack(padx=2, pady=2, fill="x")


    def on_click_example(self):
        print("example clicked.")
        DateTest(self.parent, self)

if __name__ == "__main__":
    Main(tk.Tk(), "Main menu example")

