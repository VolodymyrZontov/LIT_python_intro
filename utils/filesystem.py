def read_file(filename: str) -> str:
    with open(filename, "r") as txt_file:
        data = txt_file.read()
    return data


def write_file(filename: str, lines: list) -> None:
    content = "\n".join(lines)
    with open(filename, "w") as txt_file:
        txt_file.write(content)


if __name__ == "__main__":
    filename = "../1 course/test.txt"
    data = read_file(filename)
    print(data)