from tkinter import *
import codecs
from tkinter import messagebox

table = []

def read_puzzle():
    file_path = "sudokopuzzle1.txt"
    file = codecs.open(file_path, 'r', 'utf-8')
    num = 0
    for line in file.readlines():
        if num == 9:
            break
        row = line.strip().split()
        for i in range(0, 9):
            row[i] = row[i]
        table.append(row)
        num += 1

read_puzzle()
for row in table:
    print(row)
window = Tk()
window.title('sudoko')
window.geometry('600x600')
entry_list = []
coordinate_list = []
# ele = ['1','2','3','4','5','6','7','8','9']
def check():
    flag = True
    ele = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0,9):
        # 检查行
        for j in range(0,9):
            # 检查行是否有相同
            ele = table[i][j]
            for tmp_row in range(i+1,9):
                tmp_ele = table[tmp_row][j]
                if ele == tmp_ele:
                    print("wrong row!")
                    return False
            # 检查列是否有相同
            for tmp_col in range(j+1,9):
                tmp_ele = table[i][tmp_col]
                if ele == tmp_ele:
                    print("wrong col!")
                    return False
            # 检查block里面是否有相同的
            a = int(i / 3)
            b = int(j / 3)
            tmp_block_num = a * 3 + b
            for m in range(0,3):
                tmp_row = a*3 + m
                for n in range(0,3):
                    tmp_col = b*3 + n
                    if tmp_row == i and tmp_col == j:
                        continue
                    else:
                        tmp_ele = table[tmp_row][tmp_col]
                        if tmp_ele == ele:
                            print("wrong block!")
                            return False
    return True
def submit():
    ele = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for entry in entry_list:
        print(entry.get())
        if str(entry.get()) == '':
            messagebox.showinfo(title="wrong",message="please fill all the blank")
            return
        if str(entry.get()) not in ele:
            messagebox.showinfo(title="wrong",message="input should be integer and between[1,9]")
            return
    for i in range(0,len(entry_list)):
        tmp_ele = entry_list[i].get()
        (tmp_row, tmp_col) = coordinate_list[i]
        table[tmp_row][tmp_col] = tmp_ele
    jud = check()
    if jud:
        messagebox.showinfo(title="CONGRATULATIONS!", message="you've completed this sudoko puzzle!")
    else:
        messagebox.showinfo(title="SORRY:(", message="you don't finish this puzzle!")


for i in range(9):
    for j in range(9):
        ele = table[i][j]
        ele = str(ele)
        if ele == '0':
            entry = Entry(window,show=None,width=1)
            entry.grid(row=i,column=j)
            entry_list.append(entry)
            coordinate_list.append((i,j))
        else:
            label = Label(window,text=ele)
            label.grid(row=i,column=j,padx=10,pady=10)
button = Button(window,text='submit',command = submit)
button.grid(row=10,column=10)


window.mainloop()
