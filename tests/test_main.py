from src.main import add
import pytest

def test_add():
  assert add(2, 3) == 5
  assert add(5, 4) == 9
  assert add(3, 1) == 4
  assert add(3, 8) == 11
  assert add(5, 1) == 6
  assert add(5, 4) == 9
  assert add(5, 4, 4) == 13
  assert add(1, 2, 4) == 7
  assert add(8, 3, 4) == 15
  assert add(5, 4, 4) == 13
  assert add(5, 4, 11) == -1
  assert add(5, 10, -1) == -1
