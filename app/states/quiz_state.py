import reflex as rx
from typing import TypedDict
import uuid


class Answer(TypedDict):
    text: str
    is_correct: bool


class Question(TypedDict):
    id: str
    text: str
    answers: list[Answer]
    time_limit: int
    correct_answer_index: int | None


class Quiz(TypedDict):
    id: str
    title: str
    description: str
    category: str
    questions: list[Question]
    is_published: bool


class QuizState(rx.State):
    new_quiz: Quiz = {
        "id": "",
        "title": "",
        "description": "",
        "category": "",
        "questions": [],
        "is_published": False,
    }
    quizzes: list[Quiz] = [
        {
            "id": "1",
            "title": "General Knowledge Challenge",
            "description": "Test your knowledge on a variety of topics from history to science.",
            "category": "Trivia",
            "questions": [
                {
                    "id": "q1",
                    "text": "What is the capital of France?",
                    "answers": [
                        {"text": "Berlin", "is_correct": False},
                        {"text": "Madrid", "is_correct": False},
                        {"text": "Paris", "is_correct": True},
                        {"text": "Saturn", "is_correct": False},
                    ],
                    "time_limit": 20,
                    "correct_answer_index": 2,
                },
                {
                    "id": "q2",
                    "text": "Which planet is known as the Red Planet?",
                    "answers": [
                        {"text": "Mars", "is_correct": True},
                        {"text": "Venus", "is_correct": False},
                        {"text": "Jupiter", "is_correct": False},
                        {"text": "Saturn", "is_correct": False},
                    ],
                    "time_limit": 20,
                    "correct_answer_index": 0,
                },
            ],
            "is_published": True,
        },
        {
            "id": "2",
            "title": "Math Whiz",
            "description": "A fun quiz to test your mathematical skills.",
            "category": "Math",
            "questions": [],
            "is_published": True,
        },
        {
            "id": "3",
            "title": "History Buffs",
            "description": "Dive deep into historical events and figures.",
            "category": "History",
            "questions": [],
            "is_published": False,
        },
    ]
    search_query: str = ""
    selected_category: str = ""

    @rx.var
    def all_categories(self) -> list[str]:
        categories = {quiz["category"] for quiz in self.quizzes}
        return sorted(list(categories))

    @rx.var
    def filtered_quizzes(self) -> list[Quiz]:
        quizzes_list = [q for q in self.quizzes if q["is_published"]]
        if self.search_query:
            quizzes_list = [
                q
                for q in quizzes_list
                if self.search_query.lower() in q["title"].lower()
            ]
        if self.selected_category:
            quizzes_list = [
                q for q in quizzes_list if q["category"] == self.selected_category
            ]
        return quizzes_list

    @rx.event
    def reset_new_quiz(self):
        self.new_quiz = {
            "id": "",
            "title": "",
            "description": "",
            "category": "",
            "questions": [],
            "is_published": False,
        }
        self.add_question_to_current()

    @rx.event
    def update_quiz_field(self, field: str, value: str):
        self.new_quiz[field] = value

    @rx.event
    def add_question_to_current(self):
        new_question: Question = {
            "id": str(uuid.uuid4()),
            "text": "",
            "answers": [
                {"text": "", "is_correct": False},
                {"text": "", "is_correct": False},
                {"text": "", "is_correct": False},
                {"text": "", "is_correct": False},
            ],
            "time_limit": 20,
            "correct_answer_index": None,
        }
        self.new_quiz["questions"].append(new_question)

    @rx.event
    def remove_question(self, question_id: str):
        self.new_quiz["questions"] = [
            q for q in self.new_quiz["questions"] if q["id"] != question_id
        ]

    @rx.event
    def update_question_field(self, question_id: str, field: str, value: str):
        for q in self.new_quiz["questions"]:
            if q["id"] == question_id:
                q[field] = value
                break

    @rx.event
    def update_answer_text(self, question_id: str, answer_index: int, text: str):
        for q in self.new_quiz["questions"]:
            if q["id"] == question_id:
                q["answers"][answer_index]["text"] = text
                break

    @rx.event
    def set_correct_answer(self, question_id: str, answer_index: int):
        for q in self.new_quiz["questions"]:
            if q["id"] == question_id:
                q["correct_answer_index"] = answer_index
                for i, answer in enumerate(q["answers"]):
                    answer["is_correct"] = i == answer_index
                break

    @rx.event
    def set_published(self, is_published: bool):
        self.new_quiz["is_published"] = is_published

    @rx.event
    def save_quiz(self):
        if (
            not self.new_quiz["title"]
            or not self.new_quiz["description"]
            or (not self.new_quiz["category"])
        ):
            return rx.toast.error("Please fill in all quiz details.")
        if not self.new_quiz["questions"]:
            return rx.toast.error("A quiz must have at least one question.")
        for q in self.new_quiz["questions"]:
            if not q["text"]:
                return rx.toast.error("All questions must have text.")
            if all((not a["text"] for a in q["answers"])):
                return rx.toast.error(
                    f'''Question "{q["text"][:20]}..." must have at least one answer.'''
                )
            if q["correct_answer_index"] is None:
                return rx.toast.error(
                    f'''Question "{q["text"][:20]}..." must have a correct answer selected.'''
                )
        new_quiz_to_add = self.new_quiz.copy()
        new_quiz_to_add["id"] = str(uuid.uuid4())
        self.quizzes.append(new_quiz_to_add)
        self.reset_new_quiz()
        yield rx.toast.success("Quiz created successfully!")
        yield rx.redirect("/quizzes")