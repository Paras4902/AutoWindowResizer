from tkinter import *

root = Tk()
root.title("Auto Window Resizer")
width = 900
height = 500
root.geometry(f"{width}x{height}")
root.configure(bg="grey")

frame1 = Frame(root)
frame1.pack()

label1_frame1 = Label(frame1, text="Welcome to Auto Window Resizer", font=("Berlin Sans FB Demi", 20, "bold"), borderwidth=7, bg="grey", fg="yellow")
label1_frame1.pack()

frame2 = Frame(root)
frame2.pack()

label1_frame2 = Label(frame2, text="↓ Enter Window Width ↓", borderwidth=7, fg="grey", font=("Helvetica", 15, "bold"))
label1_frame2.pack()

entry1_frame2 = Entry(frame2, font=("Helvetica", 15, "bold"))
entry1_frame2.pack()

label2_frame2 = Label(frame2, text="↓ Enter Window height ↓", borderwidth=7, fg="grey", font=("Helvetica", 15, "bold"))
label2_frame2.pack()

entry2_frame2 = Entry(frame2, font=("Helvetica", 15, "bold"))
entry2_frame2.pack()


def applied():
    root.geometry(f"{entry1_frame2.get()}x{entry2_frame2.get()}")


button1_frame2 = Button(frame2, text="Apply", command=applied, font=("Helvetica", 15, "bold"), bg="grey", fg="sky blue")
button1_frame2.pack()

frame3 = Frame(root)
frame3.pack(side="bottom", anchor="w")

label1_frame3 = Label(frame3, text="Program@Paras4902", font=("Arial Black", 12, "bold"), relief=SUNKEN, fg="grey")
label1_frame3.pack()

frame4 = Frame(root)
frame4.pack(side="bottom", anchor="e")


def exitt():
    root.destroy()


Button(frame4, text="EXIT!!", command=exitt, font=("Helvetica", 15, "bold"), bg="grey", fg="sky blue").pack(side="bottom", anchor="e")

root.mainloop()
