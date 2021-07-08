import tkinter as tk
import random as rd

def num_checker(index, grid_step):
  # side_checker
  for x1 in range(0, grid_step):
    for x2 in range(0, grid_step):
      if x1 == x2:
        continue
      if grid[index][x1] == grid[index][x2]:
        return False
  # vertical_checker
  for y1 in range(0, grid_step):
    for y2 in range(0, grid_step):
      if y1 == y2:
        continue
      if grid[y1][index] == grid[y2][index]:
        return False
  return True

def create_vacant(vacant_numbers, grid_step):
  random_num_list = []
  for i in range(grid_step):
    for j in range(grid_step):
      random_num_list.append([i, j])
  for n in range(vacant_numbers):
    [x, y] = random_num_list.pop(rd.randint(0, len(random_num_list) - 1))
    grid[y][x] = ''

def create_grid(grid_step):
  cvs = tk.Canvas(
    width = 40 + grid_step * 80,
    height = 40 + grid_step * 80,
    bg='white'
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
        width = 3
      )
  for q in range(grid_step):
    for p in range(grid_step):
      label = tk.Label(root, text=grid[q][p], font=('System', 56))
      label.place(
        x = 20 + p * 80 + 40,
        y = 20 + q * 80 + 40,
        anchor = tk.CENTER
      )

grid = [[0 for j in range(4)] for i in range(4)]

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

  if num_checker(0, 4):
    for [y, x] in [[1, 2], [1, 3], [2, 1], [3, 1]]:
      if y == 1:
        grid[y][x] = number_list2.pop(rd.randint(0, len(number_list2)-1))
      else:
        grid[y][x] = number_list3.pop(rd.randint(0, len(number_list3)-1))

    if num_checker(1, 4):
      number_list4 = [i for i in range(1, 5)]
      for y in range(2, 4):
        for x in range(2, 4):
          grid[y][x] = number_list4.pop(rd.randint(0, len(number_list4)-1))

      if num_checker(2, 4) and num_checker(3, 4):
        break
  grid = [[0 for j in range(4)] for i in range(4)]

create_vacant(1, 4)

root = tk.Tk()
root.title('2✕2マスの数独生成')
create_grid(4)
root.mainloop()
