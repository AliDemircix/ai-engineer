# day03_exercises.py
# Exercise 1 (Day 3 — Dataclasses)

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True


@dataclass
class Cart:
    items: list[Product] = field(default_factory=list)
