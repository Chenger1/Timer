from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class SummaryReport(BaseModel):
    date: date
    total_earned: Decimal
