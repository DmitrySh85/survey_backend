from dataclasses import dataclass
from typing import Optional


@dataclass
class EmployeesFilters:
    tg_id: Optional[int] = None
    is_blocked: Optional[bool] = False
    role: Optional[str] = None

