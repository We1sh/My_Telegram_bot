import imp
from logging import _Level

from config import db_name
import shelve
from dataclasses import dataclass
from turtle import st
from typing import Tuple

@dataclass
class User:
    number: str = ''
    mode: str = ''
    level: int = 4
    history: Tuple = ()


def get_or_create_user(id):
    with shelve.open(db_name) as storage:
        return storage.get(str(id),User())
def save_user(id,user):
    with shelve.open(db_name) as storage:
        storage[str(id)]=user

def del_user(id):
    with shelve.open(db_name) as storage:
        if str(id) in storage:
            del storage[str(id)]
