#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: missionaries.py
#    Created:       <2020/01/06 15:27:01>
#    Last Modified: <2020/01/06 16:58:58>

from __future__ import annotations
from typing import List, Optional
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries # west bank missionaries
        self.wc: int = cannibals # west bank cannibals
        self.em: int = MAX_NUM - self.wm # east bank missonaries
        self.ec: int = MAX_NUM - self.wc # east bank cannibals
        self.boat: bool = boat

    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {} cannibals.\n"
                "On the east bank there are {} missionaries and {} cannibals.\n"
                "The boat is on the {} bank.")\
                .format(self.wm, self.wc, self.em, self.ec,
                        ("west" if self.boat else "east"))

    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat: # boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wm > 0 ) and (self.wc > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else: # boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.em > 0) and (self.ec > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]
