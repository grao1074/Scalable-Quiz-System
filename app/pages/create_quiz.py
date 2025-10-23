import reflex as rx
from app.components.navbar import navbar
from app.states.quiz_state import QuizState, Question
from app.states.auth_state import AuthState


def answer_input(question_id: str, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.input(
            placeholder=f"Answer {index + 1}",
            on_change=lambda text: QuizState.update_answer_text(
                question_id, index, text
            ),
            class_name="w-full pl-4 pr-12 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
        ),
        rx.el.div(
            rx.el.input(
                type="radio",
                name=f"correct_answer_{question_id}",
                on_change=lambda: QuizState.set_correct_answer(question_id, index),
                class_name="h-4 w-4 text-orange-600 focus:ring-orange-500 border-gray-300",
            ),
            class_name="absolute right-4 top-1/2 -translate-y-1/2",
        ),
        class_name="relative",
    )


def question_card(question: Question, index: int) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                f"Question {index + 1}",
                class_name="text-lg font-semibold text-gray-800",
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="h-4 w-4"),
                on_click=lambda: QuizState.remove_question(question["id"]),
                class_name="text-gray-500 hover:text-red-600",
            ),
            class_name="flex justify-between items-center mb-4",
        ),
        rx.el.textarea(
            placeholder="Enter your question here...",
            on_change=lambda text: QuizState.update_question_field(
                question["id"], "text", text
            ),
            class_name="w-full p-2 border border-gray-300 rounded-lg mb-4",
            rows=3,
        ),
        rx.el.div(
            rx.foreach(rx.Var.range(4), lambda i: answer_input(question["id"], i)),
            class_name="grid grid-cols-2 gap-4 mb-4",
        ),
        rx.el.div(
            rx.el.label("Time Limit", class_name="text-sm font-medium text-gray-700"),
            rx.el.select(
                rx.el.option("10 seconds", value="10"),
                rx.el.option("20 seconds", value="20"),
                rx.el.option("30 seconds", value="30"),
                rx.el.option("60 seconds", value="60"),
                default_value="20",
                on_change=lambda value: QuizState.update_question_field(
                    question["id"], "time_limit", value
                ),
                class_name="w-full mt-1 p-2 border border-gray-300 rounded-lg",
            ),
        ),
        class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-200 mb-6",
    )


def create_quiz_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Create a New Quiz",
                    class_name="text-4xl font-bold text-gray-800 mb-2",
                ),
                rx.el.p(
                    "Build an engaging quiz for your audience.",
                    class_name="text-lg text-gray-600 mb-8",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Quiz Details",
                        class_name="text-2xl font-semibold text-gray-800 border-b pb-2 mb-6",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Quiz Title",
                            class_name="text-sm font-semibold text-gray-700",
                        ),
                        rx.el.input(
                            placeholder="e.g., World Capitals Challenge",
                            on_change=lambda value: QuizState.update_quiz_field(
                                "title", value
                            ),
                            class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Quiz Description",
                            class_name="text-sm font-semibold text-gray-700",
                        ),
                        rx.el.textarea(
                            placeholder="A brief description of what this quiz is about.",
                            on_change=lambda value: QuizState.update_quiz_field(
                                "description", value
                            ),
                            class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                            rows=4,
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Category", class_name="text-sm font-semibold text-gray-700"
                        ),
                        rx.el.input(
                            placeholder="e.g., Geography, Science, History",
                            on_change=lambda value: QuizState.update_quiz_field(
                                "category", value
                            ),
                            class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Status", class_name="text-sm font-semibold text-gray-700"
                        ),
                        rx.el.div(
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        QuizState.new_quiz["is_published"],
                                        "eye",
                                        "eye_off",
                                    ),
                                    class_name="mr-2",
                                ),
                                rx.cond(
                                    QuizState.new_quiz["is_published"],
                                    "Published",
                                    "Draft",
                                ),
                                on_click=lambda: QuizState.set_published(
                                    ~QuizState.new_quiz["is_published"]
                                ),
                                class_name=rx.cond(
                                    QuizState.new_quiz["is_published"],
                                    "flex items-center px-4 py-2 rounded-lg bg-green-100 text-green-700 font-semibold",
                                    "flex items-center px-4 py-2 rounded-lg bg-gray-100 text-gray-700 font-semibold",
                                ),
                            ),
                            class_name="mt-2",
                        ),
                    ),
                ),
                rx.el.div(
                    rx.el.h2(
                        "Questions",
                        class_name="text-2xl font-semibold text-gray-800 border-b pb-2 mb-6 mt-12",
                    ),
                    rx.foreach(QuizState.new_quiz["questions"], question_card),
                    rx.el.button(
                        "Add Question",
                        on_click=QuizState.add_question_to_current,
                        class_name="w-full py-3 border-2 border-dashed border-gray-300 rounded-lg text-gray-600 hover:bg-gray-50 hover:border-gray-400 transition-colors",
                    ),
                ),
                rx.el.div(
                    rx.el.button(
                        "Save Quiz",
                        on_click=QuizState.save_quiz,
                        class_name="w-full py-3 mt-8 bg-orange-500 text-white font-bold rounded-lg hover:bg-orange-600 transition-colors shadow-md",
                    )
                ),
                class_name="max-w-4xl mx-auto py-12 px-4",
            )
        ),
        class_name="font-['Poppins'] bg-gray-50 min-h-screen",
    )