from BIN import FastSudoko
import time
start = time.time()
sudoko_generator = FastSudoko.FastSudokoGenerator(1000000)
# 改了！！请注意
sudoko_generator.perm(1)
sudoko_generator.write_to_file("sudoko.txt")
end = time.time()
print("time consumed = ", end-start, "s")