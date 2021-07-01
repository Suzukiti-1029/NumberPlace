import tkinter as tk
root = tk.Tk()
root.title('3✕3マスの生成')
cvs = tk.Canvas(width=760, height=760, bg='white')
cvs.pack()
grid = [[0 for j in range(9)] for i in range(9)]
for y in range(9):
  for x in range(9):
    cvs.create_rectangle(
        20 + x * 80, 20 + y * 80, 20 + x * 80 + 80, 20 + y * 80 + 80
    )
for y in range(3):
  for x in range(3):
    cvs.create_rectangle(
        20 + x * 240, 20 + y * 240, 20 + x * 240 + 240, 20 + y * 240 + 240,
        width=3
    )

for q in range(9):
  for p in range(9):
    label = tk.Label(root, text=grid[q][p], font=('System', 56))
    label.place(x=20 + p * 80 + 40, y=20 + q * 80 + 40, anchor=tk.CENTER)

root.mainloop()
