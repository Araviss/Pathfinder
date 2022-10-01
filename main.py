import tkinter as tk

root = tk.Tk()

def cell_click(row, column):
    pass


def initiate_GUI():
    for i in range(64):
        root.columnconfigure(i, weight=1, minsize=10)
        root.rowconfigure(i, weight=1, minsize=15)

        for j in range(30):
            label = tk.Label(master=root,
                             height=3,
                             width=3,
                             highlightthickness=1,
                             highlightbackground="#aaddcc"
                             )
            label.grid(row=i, column=j)
            # label.pack(fill=tk.BOTH)
            label.bind("<Button-1>",
                       lambda x, row=i, column=j: cell_click(row, column))

    root.mainloop()

initiate_GUI()

