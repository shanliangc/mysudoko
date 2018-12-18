import os
import sys
import FastSudoko
import SudoTable
import time
import codecs

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(curPath)
print(rootPath)
l = len(sys.argv)
for file in os.listdir(os.getcwd()):
    print(file)
start_time = time.time()

if l != 3:
    print("check your input!")
    print("Valid input is like:")
    print("1.")
    print("start.py -c num_of_sudoko_ending_you_want_to_generate")
    print("num should between [1,1000000]")
    print("2.")
    print("start.py -s your_sudoko_puzzle_file_path")
else:
    if sys.argv[1] == '-c':
        try:
            res = int(sys.argv[2])
        except ValueError:
            print("check your num.Input is not a int num!")
        else:
            if res < 1 or res > 1000000:
                print("Your input is out of our range!")
                print("It must between 1 to 1000000!")
            else:
                sudoko_generator = FastSudoko.FastSudokoGenerator(res)
                sudoko_generator.create_puzzle()
                file_path = "sudoko.txt"
                sudoko_generator.write_to_file(file_path)
    elif sys.argv[1] == '-s':
        file_path = sys.argv[2]
        sudoko_puzzle = SudoTable.SudoTable(1)
        table = []
        #
        try:
            file = codecs.open(file_path, 'r', 'utf-8')
        except FileNotFoundError:
            print("You should input sudopuzzle.txt for your file path!")
            print("Or you could create a puzzle file ended with '.txt'!")

            pass
        else:
            num = 0
            for line in file.readlines():
                if num == 9:
                    break
                row = line.strip().split()
                for i in range(0, 9):
                    row[i] = int(row[i])
                table.append(row)
                num += 1
            file.close()
            # 将待解决的传入table中
            sudoko_puzzle.solve_a_puzzle(table)
            # 将结果写入sudoko.txt中
            sudoko_puzzle.write_to_file("sudoko.txt")
        pass
    else:
        pass
    end_time = time.time()
    print("time consumed = ", end_time-start_time, 's')


