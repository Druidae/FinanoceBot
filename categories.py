""" Work with expense categories"""
from typing import List, Dict, NamedTuple

import db


class Category(NamedTuple):
    """ Category structure """
    codename: str
    name: str
    is_base_expense: bool
    aliases: List[str]

class Categories:
    def __init__(self) -> None:
        self._categories = self

    def _load_categories(self) -> List[Category]:
        pass