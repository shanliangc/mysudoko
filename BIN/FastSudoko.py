import random
import codecs
class FastSudokoGenerator():


    # 初始化剩余的数字
    def __init__(self,res):
        self.res = res
        self.ans = []
        # 依据要求，我的左上角第一个数字应该是2
        self.ele_sequence = ['2', '1', '3', '4', '5', '6', '7', '8', '9']
        self.init_sequence = []

    def ele_sequence_generator(self,start):
        if start >= 9:
            # print(self.sequence_res)
            # print(self.ele_sequence)
            self.sequence_res -= 1
        for i in range(start+1, 8):
            self.ele_sequence[i], self.ele_sequence[start] = self.ele_sequence[start], self.ele_sequence[i]
            if self.sequence_res >= 0:
                self.ele_sequence_generator(start+1)
            else:
                break
            self.ele_sequence[i], self.ele_sequence[start] = self.ele_sequence[start], self.ele_sequence[i]

    def perm(self, begin):
        # 从1begin = 1 end = 9
        if begin >= 9:
            # print(ls)
            if self.res >= 0:
                self.create_puzzle(self.ele_sequence)
            else:
                return
        else:
            i = begin
            for num in range(begin, 9):
                self.ele_sequence[num], self.ele_sequence[i] = self.ele_sequence[i], self.ele_sequence[num]
                if self.res >= 0:
                    self.perm(begin + 1)
                else:
                    break
                self.ele_sequence[num], self.ele_sequence[i] = self.ele_sequence[i], self.ele_sequence[num]

    def create_puzzle(self, random_ele_sequence):
        # 初始化
        sequence = [3, 6, 1, 4, 7, 2, 5, 8]
        # 为了避免重复生成数独终局，必须使用全排列的方式进行生成random_ele_sequence


        while self.res > 0:
            # random_ele_sequence = random.sample(range(1, 10), 9)
            # # 调整成2在左上角
            # random_ele_sequence.remove(2)
            # random_ele_sequence.insert(0, 2)
            # ls = []
            # for ele in random_ele_sequence:
            #     ls.append(str(ele))
            # random_ele_sequence = ls.copy()
            table = [0, 0, 0, 0, 0, 0, 0, 0, 0]

            # print(random_ele_sequence)
            table[0] = random_ele_sequence.copy()
            for i in sequence:
                tmp = random_ele_sequence[-1]
                random_ele_sequence.pop()
                random_ele_sequence.insert(0, tmp)
                table[i] = random_ele_sequence.copy()
            # 通过交换的方式生成新的矩阵
            for i in range(1, 3):
                for tmp_i in range(1, 3):
                    if tmp_i == i:
                        continue
                    if self.res == 0:
                        break
                    table[i], table[tmp_i] = table[tmp_i], table[i]
                    for j in range(3, 6):
                        for tmp_j in range(3, 6):
                            if tmp_j == j:
                                continue
                            if self.res == 0:
                                break
                            table[j], table[tmp_j] = table[tmp_j], table[j]
                            for k in range(6, 9):
                                for tmp_k in range(6, 9):
                                    if tmp_k == k:
                                        continue
                                    if self.res == 0:
                                        break
                                    table[k], table[tmp_k] = table[tmp_k], table[k]
                                    self.res -= 1
                                    s = ''
                                    for row in table:
                                        for i in range(0,8):
                                            s += row[i]
                                            s += ' '
                                        s += row[8]
                                        s += '\n'
                                    # 按照要求一下应该省略，但是为了让调试的时候看的更清楚一些
                                    # 可以使用这样的格式
                                    # s += '\n'
                                    self.ans.append(s)
                                    table[k], table[tmp_k] = table[tmp_k], table[k]
                            #调整回原来状态
                            table[j], table[tmp_j] = table[tmp_j], table[j]
                    # 调整回原来状态
                    table[i], table[tmp_i] = table[tmp_i], table[i]
    # 将结果写入文件中，这里的写入是可覆盖型写入

    def write_sequence_to_file(self):
        file_path = "initsequence.txt"
        file = codecs.open(file_path,'w','utf-8')
        for line in self.init_sequence:
            file.write(line)
        file.close()


    def read_sequence(self):
        file = codecs.open("initsequence.txt", 'r', 'utf-8')
        for line in file.readlines():
            row = line.strip().split()
            self.create_puzzle(row)
            if self.res < 0:
                break
        file.close()

    def write_to_file(self,file_path):
        file = codecs.open(file_path,'w','utf-8')
        # print(self.res)
        # for row in self.ans:
        #     print(row)
        # print("")
        for row in self.ans:
            file.write(row)
        file.close()
        # 结尾添一行