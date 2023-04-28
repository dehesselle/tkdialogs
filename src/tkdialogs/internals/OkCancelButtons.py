# SPDX-FileCopyrightText: 2023 René de Hesselle <dehesselle@web.de>
#
# SPDX-License-Identifier: MIT

import tkinter as tk
import tkinter.ttk as ttk
from enum import Enum


class OkCancelButtons(ttk.Frame):
    """
    A frame containing Ok and Cancel buttons.
    """

    Button = Enum("Button", ["OK", "CANCEL"])

    def __init__(
        self, master=None, on_ok: callable = None, on_cancel: callable = None, **kwargs
    ):
        ttk.Frame.__init__(self, master, **kwargs)
        self.button_ok = ttk.Button(self, text="Ok", command=on_ok)
        self.button_ok.pack(side=tk.LEFT)
        self.button_cancel = ttk.Button(self, text="Cancel", command=on_cancel)
        self.button_cancel.pack(side=tk.LEFT)
