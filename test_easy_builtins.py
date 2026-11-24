#!/usr/bin/env python3
"""
Comprehensive verification test for the 5 Easy Utility Functions:
1. is_palindrome
2. truncate
3. compact
4. chunk
5. unique
"""

import sys
import os

# Ensure current directory is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import is_palindrome, truncate, compact, chunk, unique

print("=" * 65)
print("TESTING 5 EASY UTILITY FUNCTIONS")
print("=" * 65)

# --- 1. IS_PALINDROME ---
print("\n[1] Testing is_palindrome...")
assert is_palindrome("racecar") is True
assert is_palindrome("radar") is True
assert is_palindrome("hello") is False
assert is_palindrome("a") is True
assert is_palindrome("") is True
assert is_palindrome([1, 2, 3, 2, 1]) is True
assert is_palindrome([1, 2, 3, 4]) is False
print("  is_palindrome('racecar') ->", is_palindrome("racecar"))
print("  is_palindrome('hello')   ->", is_palindrome("hello"))
print("  is_palindrome([1,2,2,1]) ->", is_palindrome([1, 2, 2, 1]))
print("  PASS is_palindrome!")

# --- 2. TRUNCATE ---
print("\n[2] Testing truncate...")
assert truncate("Hello World", 8) == "Hello..."
assert truncate("Short", 10) == "Short"
assert truncate("Python Programming", 10, suffix="..") == "Python P.."
assert truncate("Test", 4) == "Test"
assert truncate("ExactBoundary", 13) == "ExactBoundary"
print("  truncate('Hello World', 8)            ->", truncate("Hello World", 8))
print("  truncate('Short', 10)                 ->", truncate("Short", 10))
print("  truncate('Python Programming', 10, '..')->", truncate("Python Programming", 10, suffix=".."))
print("  PASS truncate!")

# --- 3. COMPACT ---
print("\n[3] Testing compact...")
assert compact([1, None, 2, None, 3]) == [1, 2, 3]
assert compact([None, None]) == []
assert compact([]) == []
assert compact(["apple", None, "banana", 0, False]) == ["apple", "banana", 0, False]
print("  compact([1, None, 2, None, 3])        ->", compact([1, None, 2, None, 3]))
print("  compact(['apple', None, 0, False])     ->", compact(["apple", None, 0, False]))
print("  PASS compact!")

# --- 4. CHUNK ---
print("\n[4] Testing chunk...")
assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert chunk([10, 20], 5) == [[10, 20]]
assert chunk([], 3) == []
assert chunk(range(6), 3) == [[0, 1, 2], [3, 4, 5]]
try:
    chunk([1, 2], 0)
    assert False, "Should raise ValueError on size <= 0"
except ValueError:
    pass
print("  chunk([1, 2, 3, 4, 5], 2)             ->", chunk([1, 2, 3, 4, 5], 2))
print("  chunk(range(6), 3)                    ->", chunk(range(6), 3))
print("  PASS chunk!")

# --- 5. UNIQUE ---
print("\n[5] Testing unique...")
assert unique([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
assert unique(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
assert unique([]) == []
assert unique([42]) == [42]
# Test unhashable items (dicts/lists)
assert unique([[1], [2], [1], [3]]) == [[1], [2], [3]]
print("  unique([1, 2, 2, 3, 1, 4])            ->", unique([1, 2, 2, 3, 1, 4]))
print("  unique(['a', 'b', 'a', 'c'])          ->", unique(["a", "b", "a", "c"]))
print("  unique([[1], [2], [1]])               ->", unique([[1], [2], [1]]))
print("  PASS unique!")

print("\n" + "=" * 65)
print("ALL 5 EASY UTILITY FUNCTIONS PASSED WITH 100% SUCCESS!")
print("=" * 65)
