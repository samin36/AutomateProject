from tkinter import *


class CreateGUI:
    def __init__(self, window):
        self.window = window
        self.create_gui()

    def create_gui(self):
        frame = Frame(self.window, width=480, height=640).grid(row=0, column=1, rowspan=11, columnspan=4)

        name = Label(frame, text="Name: ", font="Helvetica 14").grid(
            row=0, column=0, sticky=E)
        description = Label(frame, text="Description: ", height=5, font="Helvetica 14").grid(
            row=1, column=0, rowspan=2, sticky=E)
        directory = Label(frame, text="Directory: ", font="Helvetica 14").grid(
            row=3, column=0, sticky=E)
        auth = Label(frame, text="AuthKey: ", font="Helvetica 16").grid(row=4, column=0)
        verified_status = Label(frame, text="Status: Not verified", font="Helvetica 16").grid(row=5, column=1, pady=(3, 0),sticky=N)

        name_entry = Text(frame, width=25, height=1, font="Helvetica 16").grid(
            row=0, column=1, columnspan=2, sticky=W)
        description_entry = Text(frame, width=40, height=10, font="Helvetica 12").grid(
            row=1, column=1, columnspan=2, rowspan=2, sticky=W)
        directory_chosen = Text(frame, width=26, height=1, font="Helvetica 14").grid(
            row=3, column=1, columnspan=2, sticky=W)
        auth_entry = Text(frame, width=26, height=1, font="Helvetica 14").grid(row=4, column=1, columnspan=2, sticky=W)

        browse_button = Button(frame, text="Browse", command=self.browse_directory, width=6, font="Helvetica 13").grid(row=3, column=2, padx=(0, 10), sticky=E)
        verify_button = Button(frame, text="Verify", command=self.verify_auth, width=6, font="Helvetica 13").grid(row=4, column=2, padx=(0, 10), sticky=E)
        self.upload_var = IntVar(value=1)
        upload_to_github = Checkbutton(frame, text="Upload to Github", variable=self.upload_var, font="Helvetica 16").grid(row=3, column=1, sticky=S, pady=(40, 0))

        self.upload_mode = StringVar(value="Public")
        upload_mode_public = Radiobutton(frame, text="Public", value="Public", variable=self.upload_mode, font="Helvetica 14").grid(row=5, column=1, padx=(0, 100), sticky=S)
        upload_mode_private = Radiobutton(frame, text="Private", value="Private", variable=self.upload_mode, font="Helvetica 14").grid(row=5, column=1, padx=(100, 0), sticky=S)

    def browse_directory(self):
        pass

    def verify_auth(self):
        pass

if __name__ == "__main__":
    create = Tk()
    create.title("Project Auto-Creater")
    create.geometry("480x640")
    # create.option_add("*Font", "Helvetica 12")
    create.resizable(FALSE, FALSE)
    gui = CreateGUI(create)
    create.mainloop()
