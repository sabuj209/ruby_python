"""
Easy Utility Functions for Assignment.
Includes 5 essential, non-math utilities:
1. is_palindrome
2. truncate
3. compact
4. chunk
5. unique
"""

from typing import Any, Iterable, List, Sequence, TypeVar

T = TypeVar("T")


def is_palindrome(s: Any) -> bool:
    """
    Check if a string or sequence reads the same forwards and backwards.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome([1, 2, 3, 2, 1])
        True
    """
    if isinstance(s, (str, bytes, list, tuple)):
        return s == s[::-1]
    seq = list(s)
    return seq == seq[::-1]


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """
    Truncate string `s` to `max_len` characters, appending `suffix` if truncated.

    Examples:
        >>> truncate("Hello World", 8)
        'Hello...'
        >>> truncate("Short", 10)
        'Short'
    """
    if not isinstance(s, str):
        raise TypeError(f"truncate() argument must be str, not {type(s).__name__}")
    if len(s) <= max_len:
        return s
    cut = max_len - len(suffix)
    if cut <= 0:
        return suffix[:max_len]
    return s[:cut] + suffix


def compact(iterable: Iterable[Any]) -> List[Any]:
    """
    Filter out None values from an iterable and return a new list.

    Examples:
        >>> compact([1, None, 2, None, 3])
        [1, 2, 3]
        >>> compact([None, None])
        []
    """
    return [item for item in iterable if item is not None]


def chunk(iterable: Iterable[T], size: int) -> List[List[T]]:
    """
    Split an iterable into sub-lists of length `size`.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk([10, 20], 5)
        [[10, 20]]
    """
    if size <= 0:
        raise ValueError("chunk() size must be greater than 0")
    items = list(iterable) if not isinstance(iterable, (list, tuple)) else iterable
    return [list(items[i : i + size]) for i in range(0, len(items), size)]


def unique(iterable: Iterable[T]) -> List[T]:
    """
    Return a list with duplicate elements removed while strictly preserving original order.

    Examples:
        >>> unique([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
        >>> unique(["a", "b", "a"])
        ['a', 'b']
    """
    seen = set()
    result = []
    for item in iterable:
        try:
            if item not in seen:
                seen.add(item)
                result.append(item)
        except TypeError:
            # Fallback for unhashable items (e.g. dicts, lists)
            if item not in result:
                result.append(item)
    return result


def inject_builtins():
    """Inject all 5 functions into python's builtins namespace."""
    import builtins
    builtins.is_palindrome = is_palindrome
    builtins.truncate = truncate
    builtins.compact = compact
    builtins.chunk = chunk
    builtins.unique = unique


# Auto-inject for convenient global usage when imported
inject_builtins()
