from utils.filesystem import read_file, write_file

filename = "test.txt"
filename_result = "../result.txt"

data = read_file(filename)

lines = data.splitlines()
lines.append("NEW LINE???")

write_file(filename_result, lines)

print("2", __name__)