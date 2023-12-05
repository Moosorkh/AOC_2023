
input = ".\input.txt"

lines = []
with open(input, 'r') as file:
   for line in file:
      lines.append(line.strip())
      
list = []
for line in lines:
  list2 = [char for char in line if char.isdigit()]
  list.append(list2)

sum = 0
for i in list:
   concat_num = int(i[0] + i[-1])
   sum += concat_num

print(sum) 