def read_file(filename: str) -> str:
    with open(filename, "r") as txt_file:
        data = txt_file.read()
    return data


def write_file(filename: str, lines: list) -> None:
    content = "\n".join(lines)
    with open(filename, "w") as txt_file:
        txt_file.write(content)


def get_lines_from_txt_file(filename: str) -> list[str]:
    with open(filename, "r") as file:
        data = file.read()
    return data.split("\n")

if __name__ == "__main__":
    filename = "../1 course/test.txt"
    data = read_file(filename)
    print(data)