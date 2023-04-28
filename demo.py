# SPDX-FileCopyrightText: 2023 René de Hesselle <dehesselle@web.de>
#
# SPDX-License-Identifier: MIT

from src.tkdialogs import ListboxDialog


def listboxdialog():
    listboxdialog = ListboxDialog(
        "name selection", "Please choose a name.", ["Adam", "Mary"]
    )
    result = listboxdialog.show()
    print(result)
    if result.button == ListboxDialog.Button.OK:
        print(f"You have chosen {result.item}")


if __name__ == "__main__":
    listboxdialog()
