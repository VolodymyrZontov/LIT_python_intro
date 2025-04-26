import re


# my_str = "My e_mail: zontov_v2025@gmail.com.ua, my new e-mail: 45_vz@dlit.dp.ua"
#
# reg_ex = r"[a-z0-9_.]+@[a-z0-9_.]+"
#
# result = re.findall(reg_ex, my_str)
# print(result)

class TifInfo:
    def __init__(self, filename: str, pages_count: int) -> None:
        self.filename = filename
        self.pages_count = pages_count

    def __repr__(self) -> str:
        return f"{self.filename}, {self.pages_count} pages"


class LogsInfo:
    def __init__(self, filename: str, ) -> None:
        self.data = self.get_data_from_txt(filename)
        self.logs_info = []
        self.regex_filename = r"cedTifTest/\d+\.\d+\.\d+\.\d+M\.TIF"
        self.regex_page_number = r"page[ ]+\d+"

    def process_data(self) -> None:
        page_numbers = []
        for line in self.data:
            if page_number := re.findall(self.regex_page_number, line):
                page_numbers.append(int(page_number[0].split(" ")[-1]))
            if res := re.findall(self.regex_filename, line):
                self.logs_info.append(TifInfo(res[0], max(page_numbers)))
                page_numbers = []

    def get_data_from_txt(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            data = file.read()
        return data.split("\n")


if __name__ == "__main__":
    filename = "lesson_9.txt"
    logs_info = LogsInfo(filename)
    logs_info.process_data()
    [print(line) for line in logs_info.logs_info[:10]]
