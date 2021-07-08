import tkinter as tk
import random as rd

def create_grid(grid_step):
  cvs = tk.Canvas(
    width = 40 + grid_step * 80,
    height = 40 + grid_step * 80,
    bg = 'white'
  )
  cvs.pack()
  for y in range(grid_step):
    for x in range(grid_step):
      cvs.create_rectangle(
        20 + x * 80,
        20 + y * 80,
        20 + (x + 1) * 80,
        20 + (y + 1) * 80
      )
  grid_big_step = int(grid_step ** 0.5)
  for y in range(grid_big_step):
    for x in range(grid_big_step):
      cvs.create_rectangle(
        20 + x * 80 * grid_big_step,
        20 + y * 80 * grid_big_step,
        20 + (x + 1) * 80 * grid_big_step,
        20 + (y + 1) * 80 * grid_big_step,
        width=3
      )
  for q in range(grid_step):
    for p in range(grid_step):
      label = tk.Label(root, text=grid[q][p], font=('System', 56))
      label.place(
        x = 20 + p * 80 + 40,
        y = 20 + q * 80 + 40,
        anchor=tk.CENTER
      )


grid = [[0 for j in range(9)] for i in range(9)]

root = tk.Tk()
root.title('3✕3マスの数独')
create_grid(9)
root.mainloop()
