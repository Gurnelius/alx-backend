#!/usr/bin/env python3
"""
simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Arguments:
    page -- the page number (1-indexed)
    page_size -- the number of items per page

    Returns:
    A tuple of two integers, start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
