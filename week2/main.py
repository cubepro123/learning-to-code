"""
week2
Python practice project.
Run: python main.py
"""

# ── Example 1: Basic functions ────────────────────────
def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}! Welcome to USIU."

# ── Example 2: List comprehension ────────────────────
def squares(n: int) -> list:
    """Return a list of squares from 1 to n."""
    return [i * i for i in range(1, n + 1)]

# ── Example 3: Dictionary operations ─────────────────
def word_count(text: str) -> dict:
    """Count occurrences of each word in text."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:")
        counts[word] = counts.get(word, 0) + 1
    return counts

# ── Example 4: Simple class ───────────────────────────
class Student:
    def __init__(self, name: str, student_id: str):
        self.name       = name
        self.student_id = student_id
        self.grades     = []

    def add_grade(self, subject: str, score: float):
        self.grades.append({"subject": subject, "score": score})

    def gpa(self) -> float:
        if not self.grades:
            return 0.0
        return round(sum(g["score"] for g in self.grades) / len(self.grades), 2)

    def __repr__(self):
        return f"Student({self.name!r}, GPA={self.gpa()})"


if __name__ == "__main__":
    print(greet("John"))
    print("Squares 1-10:", squares(10))
    print("Word count:", word_count("to be or not to be that is the question"))

    s = Student("John Mwangi", "USI-2024-001")
    s.add_grade("IST1025", 88.5)
    s.add_grade("MAT1010", 75.0)
    s.add_grade("ENG1001", 91.0)
    print(s)
    print("Grades:", s.grades)
