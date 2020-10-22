#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: word_search.py
#    Created:       <2020/10/22 13:58:58>
#    Last Modified: <2020/10/22 17:05:48>

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]

class GridLocation(NamedTuple):
    row: int
    column: int

def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid: Grid):
    for row in grid:
            print("".join(row))

def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        columns: range = range(col, col + length + 1)
        rows: range = range(row, row + length + 1)
        if col + length <= width:
           domain.append([GridLocation(row, c) for c in columns])
           if row + length <= height:
               domain.append([GridLocation(r, col + (r - row)) for r in rows])
        if row + length <= height:
            domain.append([GridLocation(r, col) for r in rows])
            if col - length >= 0:
                domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain
