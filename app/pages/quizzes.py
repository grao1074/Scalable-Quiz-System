import reflex as rx
from app.components.navbar import navbar
from app.states.quiz_state import QuizState, Quiz
from app.states.auth_state import AuthState


def quiz_card(quiz: Quiz) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    quiz["category"],
                    class_name="text-xs font-semibold bg-orange-100 text-orange-600 px-2 py-1 rounded-full",
                ),
                class_name="mb-4",
            ),
            rx.el.h3(
                quiz["title"],
                class_name="text-xl font-bold text-gray-800 mb-2 truncate",
            ),
            rx.el.p(
                quiz["description"],
                class_name="text-gray-600 text-sm mb-4 h-10 overflow-hidden",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("circle_plus", class_name="h-4 w-4 mr-1 text-gray-500"),
                    rx.el.span(
                        f"{quiz['questions'].length()} Questions",
                        class_name="text-sm text-gray-600",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.div(
                    rx.icon("clock", class_name="h-4 w-4 mr-1 text-gray-500"),
                    rx.el.span(
                        f"{quiz['questions'].length() * 1} min",
                        class_name="text-sm text-gray-600",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex justify-between items-center text-xs text-gray-500 border-t border-gray-100 pt-3 mt-3",
            ),
            class_name="p-5",
        ),
        rx.el.div(
            rx.el.a(
                rx.el.button(
                    "Start Quiz",
                    rx.icon("play", class_name="ml-2 size-4"),
                    class_name="w-full flex items-center justify-center py-2.5 bg-orange-500 text-white font-bold rounded-b-lg hover:bg-orange-600 transition-colors",
                ),
                href=f"/quizzes/{quiz['id']}/play",
            )
        ),
        class_name="bg-white rounded-xl shadow-md border border-gray-100 hover:shadow-lg transition-all duration-300 flex flex-col justify-between overflow-hidden",
    )


def quizzes_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Quiz Library", class_name="text-4xl font-bold text-gray-800"
                    ),
                    rx.el.p(
                        "Browse, search, and start quizzes.",
                        class_name="text-lg text-gray-600 mt-2",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "search",
                            class_name="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400",
                        ),
                        rx.el.input(
                            placeholder="Search quizzes...",
                            on_change=QuizState.set_search_query,
                            class_name="w-full md:w-80 pl-10 pr-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                        ),
                        class_name="relative",
                    ),
                    rx.cond(
                        (AuthState.current_user_role == "ADMIN")
                        | (AuthState.current_user_role == "EDITOR"),
                        rx.el.a(
                            rx.el.button(
                                "Create Quiz",
                                rx.icon("plus", class_name="mr-2"),
                                class_name="flex items-center px-4 py-2.5 bg-green-500 text-white font-bold rounded-lg hover:bg-green-600 transition-colors",
                            ),
                            href="/quizzes/create",
                        ),
                        None,
                    ),
                    rx.el.select(
                        rx.el.option("All Categories", value=""),
                        rx.foreach(
                            QuizState.all_categories,
                            lambda cat: rx.el.option(cat, value=cat),
                        ),
                        on_change=QuizState.set_selected_category,
                        class_name="w-full md:w-56 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                    ),
                    class_name="flex flex-col md:flex-row gap-4 mt-8 items-center",
                ),
                rx.el.div(
                    rx.foreach(QuizState.filtered_quizzes, quiz_card),
                    class_name="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 mt-8",
                ),
                rx.cond(
                    QuizState.filtered_quizzes.length() == 0,
                    rx.el.div(
                        rx.icon("search-x", class_name="h-16 w-16 text-gray-400 mb-4"),
                        rx.el.h3(
                            "No Quizzes Found",
                            class_name="text-xl font-semibold text-gray-700",
                        ),
                        rx.el.p(
                            "Try adjusting your search or filter.",
                            class_name="text-gray-500",
                        ),
                        class_name="text-center py-20 bg-gray-50 rounded-lg mt-8",
                    ),
                    None,
                ),
                class_name="max-w-7xl mx-auto py-12 px-4",
            )
        ),
        class_name="font-['Poppins'] bg-gray-50 min-h-screen",
    )