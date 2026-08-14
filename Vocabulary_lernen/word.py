from dataclasses import dataclass


@dataclass
class Word:
    question: str
    answer: str

    image: str | None = None
    audio: str | None = None
    example: str | None = None

    correct: int = 0
    wrong: int = 0
    weight: float = 1.0

    chapter: str = ""