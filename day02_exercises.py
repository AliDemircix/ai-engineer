# day02_exercises.py
# Exercise 1 (Day 2 — Type Hints)


def filter_names_by_age(users: list[dict[str, str | int]], min_age: int) -> list[str]:
    return [user["name"] for user in users if user["age"] > min_age]
