# SPDX-FileCopyrightText: 2023 René de Hesselle <dehesselle@web.de>
#
# SPDX-License-Identifier: MIT

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
        self.grid()
        ttk.Button(self, text="Ok", command=on_ok).grid(column=0, row=0)
        ttk.Button(self, text="Cancel", command=on_cancel).grid(column=1, row=0)
