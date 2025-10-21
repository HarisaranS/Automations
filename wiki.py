import wikipedia
import tkinter as tk

def on_press():
    q = get_q.get()
    text.insert(tk.INSERT,wikipedia.summary(q))

root = tk.Tk()
root.title("Wiki summary")


question = tk.Label(root,text='Question')
question.pack()

get_q = tk.Entry(root,bd=5)
get_q.pack()

submit = tk.Button(root,text='GetSummary',command=on_press)
submit.pack()

text = tk.Text(root,width=100)
text.pack()

root.mainloop()
