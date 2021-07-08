import tkinter as tk
import random as rd

root = tk.Tk()
root.title('2✕2マスの数独生成')
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

def side14_num_checker(W_x_index, W_y_index):
  for x1 in range(W_x_index, W_x_index + 4):
    for x2 in range(W_x_index, W_x_index + 4):
      if x1 == x2:
        continue
      if grid[W_y_index][x1] == grid[W_y_index][x2]:
        return False
  return True

def vertical41_num_checker(N_x_index, N_y_index):
  for y1 in range(N_y_index, N_y_index + 4):
    for y2 in range(N_y_index, N_y_index + 4):
      if y1 == y2:
        continue
      if grid[y1][N_x_index] == grid[y2][N_x_index]:
        return False
  return True

while True:
  number_list1 = [i for i in range(1, 5)]
  for y in range(2):
    for x in range(2):
      grid[y][x] = number_list1.pop(rd.randint(0, len(number_list1)-1))

  number_list2 = [i for i in range(1, 5)]
  number_list3 = [i for i in range(1, 5)]
  for [y, x] in [[0, 2], [0, 3], [2, 0], [3, 0]]:
    if y == 0:
      grid[y][x] = number_list2.pop(rd.randint(0, len(number_list2)-1))
    else:
      grid[y][x] = number_list3.pop(rd.randint(0, len(number_list3)-1))

  if side14_num_checker(0, 0) and vertical41_num_checker(0, 0):
    for [y, x] in [[1, 2], [1, 3], [2, 1], [3, 1]]:
      if y == 1:
        grid[y][x] = number_list2.pop(rd.randint(0, len(number_list2)-1))
      else:
        grid[y][x] = number_list3.pop(rd.randint(0, len(number_list3)-1))

    if side14_num_checker(0, 1) and vertical41_num_checker(1, 0):
      number_list4 = [i for i in range(1, 5)]
      for y in range(2, 4):
        for x in range(2, 4):
          grid[y][x] = number_list4.pop(rd.randint(0, len(number_list4)-1))

      if side14_num_checker(0, 2) and side14_num_checker(0, 3) \
      and vertical41_num_checker(2, 0) and vertical41_num_checker(3, 0):
        break

  grid = [[0 for j in range(4)] for i in range(4)]

random_num_list = []
for i in range(4):
  for j in range(4):
    random_num_list.append([i, j])
for a in range(9):
  [x, y] = random_num_list.pop(rd.randint(0, len(random_num_list)-1))
  grid[y][x] = ''

for q in range(4):
  for p in range(4):
    label = tk.Label(root, text=grid[q][p], font=('System', 56))
    label.place(x=20 + p * 80 + 40, y=20 + q * 80 + 40, anchor=tk.CENTER)

root.mainloop()
