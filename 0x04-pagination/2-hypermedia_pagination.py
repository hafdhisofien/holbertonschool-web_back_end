#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page: page number int
        page_size: page size int
    Returns:
        return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes
        to return in a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """
        Args:
            page: page number int defaults to 1
            page_size: page size int defaults to 10
        Returns:
            return the appropriate page of the dataset
            If the input arguments are out of range for the dataset,
            an empty list should be returned.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        results = []
        if start >= len(self.dataset()):
            return results
        dataset = self.dataset()
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Args:
            page: page number int defaults to 1
            page_size: page size int defaults to 10
        Returns:
            dictionary [dict] containing the following key-value pairs:
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page
                next_page: number of the next page,None if no next page
                prev_page: number of the previous page,None if no previous page
                total_pages: the total number of pages in the dataset
        """
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {"page_size": len(self.get_page(page, page_size)),
                "page": page,
                "data": self.get_page(page, page_size),
                "next_page": page + 1 if page + 1 < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
