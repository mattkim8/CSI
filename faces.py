from Tkinter import *
window = Tk()
ps2_canvas = Canvas(window, width=500, height=500)
ps2_canvas.grid(row=0, column=0)
# These next four statements are the ones you should play with for your
# program. LEAVE EVERYTHING ELSE (apart from the comments) ALONE

# draw the face
ps2_canvas.create_oval(100, 100, 400, 400, fill='yellow')
# Draw the mouth
ps2_canvas.create_arc(175, 175, 325, 325, start=225, extent=90, style=ARC)
# Draw the left eye
ps2_canvas.create_oval(200, 205, 202, 207, fill='black')
# Draw the right eye
ps2_canvas.create_oval(298, 205, 300, 207, fill='black')
# Keep this line at the end of your program
window.mainloop()
