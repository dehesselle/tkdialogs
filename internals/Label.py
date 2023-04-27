import tkinter.ttk as ttk


class Label(ttk.Label):
    """
    A `ttk.Label` that automatically wraps text on resize.
    """

    def __init__(self, master=None, **kwargs):
        ttk.Label.__init__(self, master, **kwargs)
        self.bind(
            "<Configure>", lambda label: self.config(wraplength=self.winfo_width())
        )
