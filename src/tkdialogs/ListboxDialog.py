# SPDX-FileCopyrightText: 2023 René de Hesselle <dehesselle@web.de>
#
# SPDX-License-Identifier: MIT

import tkinter as tk
import tkinter.ttk as ttk
from dataclasses import dataclass
from typing import List
from .internals import Label, OkCancelButtons


class ListboxDialog:
    Button = OkCancelButtons.Button

    @dataclass
    class Result:
        """
        The return type used by ListboxDialog.show().

        Attributes
        ----------
        button : OkCancelButton.Button
            The button that has been clicked.
        item : str
            The selected item if the OK button has been clicked. Otherwise empty string.
        """

        button: OkCancelButtons.Button = OkCancelButtons.Button.CANCEL
        item: str = ""

    def __init__(self, title: str, description: str, items: List[str]):
        """
        Construct a ListboxDialog object.

        Parameters
        ----------
        title : str
            The window title.
        description : str
            The text to show as description in `self.label`.
        items : List[str]
            The list of strings to be used as selectable items in `self.listbox`.
        """
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("250x200")
        self.window.grid()
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.label = Label(self.window, text=description, anchor=tk.CENTER)
        self.label.grid(row=0, sticky="news")

        self.listbox = tk.Listbox(height=5)
        self.listbox.grid(row=1, padx=5, sticky="news")
        for item in items:
            self.listbox.insert(tk.END, item)
        self.listbox.selection_set(0)

        self.okcancelbuttons = OkCancelButtons(
            self.window, on_ok=self.on_button_ok, on_cancel=self.on_button_cancel
        )
        self.okcancelbuttons.grid(row=2, sticky="e", padx=5)

        self.window.after(
            0,
            lambda: self.window.minsize(
                self.okcancelbuttons.winfo_width(), self.listbox.winfo_height()
            ),
        )

        self.result = self.Result()

    def on_button_ok(self):
        self.result.button = self.Button.OK
        self.result.item = self.listbox.get(self.listbox.curselection())
        self.window.destroy()

    def on_button_cancel(self):
        self.window.destroy()

    def show(self) -> Result:
        self.window.mainloop()
        return self.result
