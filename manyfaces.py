# Problem Set 2, Part II
# Kim, Matthew

from Tkinter import *
window = Tk()
ps2_canvas = Canvas(window, width=500, height=500)
ps2_canvas.grid(row=0, column=0)
# These next four statements are the ones you should play with for your
# program. LEAVE EVERYTHING ELSE (apart from the comments) ALONE

# draw the face
#ps2_canvas.create_rectangle(90, 100, 400, 400, fill='yellow')
# Draw the mouth
#ps2_canvas.create_arc(175, 400, 325, 325, start=400, extent=110, style=ARC)
# Draw the left eye
#ps2_canvas.create_oval(175, 180, 202, 207, fill='black')
# Draw the right eye
#ps2_canvas.create_oval(270, 180, 300, 207, fill='black')
# Keep this line at the end of your program
#window.mainloop()

def right_eye():
    ps2_canvas.create_oval(270, 180, 300, 207, fill='white')
    ps2_canvas.create_oval(273, 185, 295, 205, fill='black')
    return
def left_eye():
    ps2_canvas.create_oval(175, 180, 202, 207, fill='white')
    ps2_canvas.create_oval(178, 185, 200, 205, fill='black')
    return
    
    




def emotion():
    print "Hello,there. I'm a robot that understands these emotions: Happy,Sad, Indifferent,Angry, and Like Spongebob."
    emot = str(raw_input('How are you doing today? '))
    if emot == 'Happy':
        ps2_canvas.create_oval(90, 100, 400, 400, fill='yellow')
        ps2_canvas.create_arc(175, 175, 325, 325, start=225, extent=90, style=ARC)
        right_eye()
        left_eye()
    elif emot == 'Sad':
        ps2_canvas.create_oval(90, 100, 400, 400, fill='yellow')
        ps2_canvas.create_arc(175, 400, 325, 325, start=400, extent=110, style=ARC)
        right_eye()
        left_eye()
    elif emot == 'Indifferent':
        ps2_canvas.create_oval(90, 100, 400, 400, fill='yellow')
        ps2_canvas.create_arc(175, 325, 325, 325, start=400, extent=110, style=ARC)
        right_eye()
        left_eye()
    elif emot == 'Angry':
        ps2_canvas.create_oval(90, 100, 400, 400, fill='yellow')
        ps2_canvas.create_arc(175, 400, 325, 325, start=400, extent=110, style=ARC)
        right_eye()
        left_eye()
        ps2_canvas.create_line(170,160,220,200)
        ps2_canvas.create_line(250,200,310,160)  
    elif emot == 'Like Spongebob':
        ps2_canvas.create_rectangle(90, 100, 400, 400, fill='yellow')
        ps2_canvas.create_arc(175, 175, 325, 325, start=225, extent=90, style=ARC)
        right_eye()
        left_eye()
    else:
        return 'I do not understand this emotion'
    
print emotion()
window.mainloop()

