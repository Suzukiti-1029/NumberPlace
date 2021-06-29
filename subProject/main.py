import tkinter as tk

root = tk.Tk()
root.title('2✕2マスの生成')
cvs = tk.Canvas(width=360, height=360, bg='white')
cvs.pack()

grid = [[0 for j in range(4)] for i in range(4)]

for y in range(4):
  for x in range(4):
    cvs.create_rectangle(
        20 + x * 80, 20 + y * 80, 20 + x * 80 + 80, 20 + y * 80 + 80
    )

for y in range(2):
  for x in range(2):
    cvs.create_rectangle(
        20 + x * 160, 20 + y * 160, 20 + x * 160 + 160, 20 + y * 160 + 160,
        width=3
    )

root.mainloop()
