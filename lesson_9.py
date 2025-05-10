import ast
import re

from settings import REGEX_FILENAME, REGEX_PAGE_INFO, REGEX_PAGE_DATA
from utils.filesystem import get_lines_from_txt_file


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
        self.text_data = self._get_text_data()

    def __repr__(self) -> str:
        return f"page{self.page_number}:({self.page_width}, {self.page_height}), data: {len(self.data)}"

    def _get_text_data(self) -> list[str]:
        return [self._build_text_line(data_line) for data_line in self.data]

    @staticmethod
    def _build_text_line(data_line) -> str:
        return " ".join([line[-1] for line in data_line])


class TifInfo:
    def __init__(self, filename: str, pages: list[PageInfo]) -> None:
        self.filename = filename
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.filename}, pages: {self.pages}"


class LogsInfo:
    def __init__(self, filename: str,
                 regex_filename: str = REGEX_FILENAME,
                 regex_page_info: str = REGEX_PAGE_INFO,
                 regex_page_data: str = REGEX_PAGE_DATA,
                 ) -> None:
        self.data = get_lines_from_txt_file(filename)
        self.logs_info = []
        self.regex_filename = regex_filename
        self.regex_page_info = regex_page_info
        self.regex_page_data = regex_page_data

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


if __name__ == "__main__":
    filename = "lesson_9.txt"
    logs_info = LogsInfo(filename)
    logs_info.process_data()
    for tif_data in logs_info.logs_info[:10]:
        print(f"================={tif_data.filename}===================")
        for page in tif_data.pages:
            # fake_data = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))
            # print(page._build_text_line(fake_data))
            for line in page.text_data:
                print(line)
