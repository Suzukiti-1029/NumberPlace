import tkinter as tk
import random as rd

root = tk.Tk()
root.title('2✕2マスの生成')
cvs = tk.Canvas(width=360, height=360, bg='white')
cvs.pack()

def patch_txt(p, q, txt):
  label = tk.Label(root, text=txt, font=('System', 56))
  label.place(x=20 + p * 80 + 40, y=20 + q * 80 + 40, anchor=tk.CENTER)
  grid[q][p] = txt

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

def block22_num_checker(NW_x_index, NW_y_index):
  if grid[NW_y_index][NW_x_index] != grid[NW_y_index][NW_x_index + 1] \
  and grid[NW_y_index][NW_x_index] != grid[NW_y_index + 1][NW_x_index] \
  and grid[NW_y_index][NW_x_index] != grid[NW_y_index + 1][NW_x_index + 1] \
  and grid[NW_y_index][NW_x_index + 1] != grid[NW_y_index + 1][NW_x_index] \
  and grid[NW_y_index][NW_x_index + 1] != grid[NW_y_index + 1][NW_x_index + 1] \
  and grid[NW_y_index + 1][NW_x_index] != grid[NW_y_index + 1][NW_x_index + 1]:
    return True
  else:
    return False

def side14_num_checker(W_x_index, W_y_index):
  if grid[W_y_index][W_x_index] != grid[W_y_index][W_x_index + 1] \
  and grid[W_y_index][W_x_index] != grid[W_y_index][W_x_index + 2] \
  and grid[W_y_index][W_x_index] != grid[W_y_index][W_x_index + 3] \
  and grid[W_y_index][W_x_index + 1] != grid[W_y_index][W_x_index + 2] \
  and grid[W_y_index][W_x_index + 1] != grid[W_y_index][W_x_index + 3] \
  and grid[W_y_index][W_x_index + 2] != grid[W_y_index][W_x_index + 3]:
    return True
  else:
    return False

def vertical41_num_checker(N_x_index, N_y_index):
  if grid[N_y_index][N_x_index] != grid[N_y_index + 1][N_x_index] \
          and grid[N_y_index][N_x_index] != grid[N_y_index + 2][N_x_index] \
          and grid[N_y_index][N_x_index] != grid[N_y_index + 3][N_x_index] \
          and grid[N_y_index + 1][N_x_index] != grid[N_y_index + 2][N_x_index] \
          and grid[N_y_index + 1][N_x_index] != grid[N_y_index + 3][N_x_index] \
          and grid[N_y_index + 2][N_x_index] != grid[N_y_index + 3][N_x_index]:
    return True
  else:
    return False

number_list = [i for i in range(1, 5)]

for y in range(2):
  for x in range(2):
    if grid[y][x] == 0:
      patch_txt(x, y, number_list.pop(rd.randint(0, len(number_list)-1)))

print(block22_num_checker(0, 0))
print(side14_num_checker(0, 0))
print(vertical41_num_checker(0, 0))

root.mainloop()
