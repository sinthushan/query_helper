from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Field:
    field_name: str
    field_type: str
    db_column: str
    choices: Optional[List[str]] = None

@dataclass
class Screen:
    screen_name: str
    fields: List[Field]
    db_table: str
    def __post_init__(self):
        self.fields = [Field(**field) for field in self.fields]
        self.href = f'/{self.db_table}'
@dataclass
class Mvest:
    screens: List[Screen]
    current_screen: Optional[Screen] = None
    def __post_init__(self):
        self.screens = [Screen(**screen) for screen in self.screens]
    def set_current_screen(self, screen_name):
        self.current_screen = list(filter(lambda screen: screen.db_table == screen_name, self.screens))[0]



