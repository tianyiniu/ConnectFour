"""Helper methods."""

def lst_int_to_str(lst: list[int]) -> list[str]:
    """Converts list of ints to list of strings"""
    return [str(num).strip() for num in lst]
    