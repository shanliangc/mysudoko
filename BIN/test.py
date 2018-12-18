import FastSudoko

sudoko_generator = FastSudoko.FastSudokoGenerator(10)
sudoko_generator.create_puzzle()
file_path = "sudoko.txt"
sudoko_generator.write_to_file(file_path)
