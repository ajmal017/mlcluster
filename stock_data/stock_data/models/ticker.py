# Copyright (C) 2020 Mike Healey
# All rights reserved
#
from dataclasses import dataclass

from stock_data.models.model import Model


@dataclass
class Ticker(Model):
    ticker: str
    name: str
    market: str
    locale: str
    currency: str
    active: bool
