from src.tkdialogs import ListboxDialog


def listboxdialog():
    listboxdialog = ListboxDialog(
        "name selection", "Please choose a name.", ["Adam", "Mary"]
    )
    result = listboxdialog.show()
    print(result)


if __name__ == "__main__":
    listboxdialog()
