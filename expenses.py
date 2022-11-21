import datetime
import re

from typing import List, NamedTuple, Optional

import exceptions


class Message(NamedTuple): # The structur of the parsed message about a new expens
    amount: int
    category_text: str

class Expense(NamedTuple): # The structur of the new expense added to the db
    id: Optional[int]
    amount: int
    category_name: str

def _parse_message(raw_message: str) -> Message: # Parses a text of an incoming message about a new expense
    regexp_result = re.match(r"([\d ]+) (.*)", raw_message)
    if not regexp_result or not regexp_result.group(0) or not regexp_result.group(1) or not regexp_result.group(2):
        raise exceptions.NotCorrectMessage("Не могу понять сообщение. Напишите сообщение в формате, например: \n1500 метро")

    amount = regexp_result.group(1).replace(" ", "")
    category_text = regexp_result.group(2).strip().lower()
    return Message(amount=amount, category_text=category_text)