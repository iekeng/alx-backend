#!/usr/bin/env python3
"""0-simple_helper_function"""
from typing import List


def index_range(page: int, page_size: int) -> List[int]:
    """ Returns the a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return
        in a list for the particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
