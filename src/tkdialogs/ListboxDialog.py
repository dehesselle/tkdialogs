# SPDX-FileCopyrightText: 2023 René de Hesselle <dehesselle@web.de>
#
# SPDX-License-Identifier: MIT

import tkinter as tk
from dataclasses import dataclass
from typing import List
from .internals.Label import Label
from .internals.OkCancelButtons import OkCancelButtons


class ListboxDialog:
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
        self.window.minsize(150, 200)
        self.window.geometry("250x200")

        self.label = Label(self.window, text=description)
        self.label.pack(fill=tk.X, padx=5, pady=5)

        self.listbox = tk.Listbox(self.window, height=5)
        for item in items:
            self.listbox.insert(tk.END, item)
        self.listbox.selection_set(0)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.okcancelbuttons = OkCancelButtons(
            self.window, on_ok=self.on_button_ok, on_cancel=self.on_button_cancel
        )
        self.okcancelbuttons.pack(side=tk.RIGHT, padx=5)

        self.result = self.Result()

    def on_button_ok(self):
        self.result.button = OkCancelButtons.Button.OK
        self.result.item = self.listbox.get(self.listbox.curselection())
        self.window.destroy()

    def on_button_cancel(self):
        self.window.destroy()

    def show(self) -> Result:
        self.window.mainloop()
        return self.result
