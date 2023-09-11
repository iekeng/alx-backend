#!/usr/bin/env python3
"""1-simple_pagination.py"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        data = self.dataset()
        # data_length = len(data)
        try:
            limit = self.index_range(page, page_size)
            return data[limit[0]:limit[1]]
        except IndexError:
            return []

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ Returns the a tuple of size two containing a start index
            and an end index corresponding to the range of indexes to return
            in a list for the particular pagination parameters
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index
