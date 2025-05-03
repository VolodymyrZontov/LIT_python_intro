import ast
import re


# my_str = "My e_mail: zontov_v2025@gmail.com.ua, my new e-mail: 45_vz@dlit.dp.ua"
#
# reg_ex = r"[a-z0-9_.]+@[a-z0-9_.]+"
#
# result = re.findall(reg_ex, my_str)
# print(result)

class PageInfo:
    def __init__(self, page_number: str, page_height: str, page_width: str, data: str) -> None:
        self.page_number = page_number
        self.page_height = page_height
        self.page_width = page_width
        self.data = ast.literal_eval(data)

    def __repr__(self) -> str:
        return f"page{self.page_number}:({self.page_width}, {self.page_height}), data: {len(self.data)}"

    def print_data(self) -> None:
        [print(self.build_text_line(data_line)) for data_line in self.data]

    def build_text_line(self, data_line) -> str:
        return " ".join([line[-1] for line in data_line])


class TifInfo:
    def __init__(self, filename: str, pages: list[PageInfo]) -> None:
        self.filename = filename
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.filename}, pages: {self.pages}"


class LogsInfo:
    def __init__(self, filename: str, ) -> None:
        self.data = self.get_data_from_txt(filename)
        self.logs_info = []
        self.regex_filename = r"cedTifTest/\d+\.\d+\.\d+\.\d+M\.TIF"
        self.regex_page_info = r"page\s+(\d+)\s+pageHeight\s+(\d+)\s+pageWidth\s+(\d+)"
        self.regex_page_data = r"page\s+(\d+)\s+(\[+.*\]+)$"

    def process_data(self) -> None:
        pages = []
        pages_data_dict = {}
        for line in self.data:
            if page_match := re.search(self.regex_page_info, line):
                page_num, page_height, page_width = page_match.groups()
                page_info = PageInfo(page_number=page_num,
                                     page_height=page_height,
                                     page_width=page_width,
                                     data=pages_data_dict.get(page_num, ""))
                pages.append(page_info)
            elif page_data_match := re.search(self.regex_page_data, line):
                page_num, page_data = page_data_match.groups()
                pages_data_dict[page_num] = page_data
            if res := re.findall(self.regex_filename, line):
                self.logs_info.append(TifInfo(res[0], pages))
                pages = []
                pages_data_dict = {}

    def get_data_from_txt(self, filename: str) -> list[str]:
        with open(filename, "r") as file:
            data = file.read()
        return data.split("\n")


if __name__ == "__main__":
    filename = "lesson_9.txt"
    logs_info = LogsInfo(filename)
    logs_info.process_data()
    for tif_data in logs_info.logs_info[:10]:
        print(f"================={tif_data.filename}===================")
        for page in tif_data.pages:
            page.print_data()
