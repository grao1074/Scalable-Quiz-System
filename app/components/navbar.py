import reflex as rx
from app.states.auth_state import AuthState


def navbar() -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.div(
                rx.icon("swords", class_name="size-8 text-orange-500"),
                rx.el.span("QuizWhiz", class_name="text-2xl font-bold text-gray-800"),
                class_name="flex items-center gap-2",
            ),
            href="/",
        ),
        rx.cond(
            AuthState.is_authenticated,
            rx.el.div(
                rx.el.a(
                    "Dashboard",
                    href="/dashboard",
                    class_name="font-medium text-gray-600 hover:text-orange-500 transition-colors",
                ),
                rx.el.a(
                    "Quizzes",
                    href="/quizzes",
                    class_name="font-medium text-gray-600 hover:text-orange-500 transition-colors",
                ),
                rx.el.a(
                    "Profile",
                    href="/profile",
                    class_name="font-medium text-gray-600 hover:text-orange-500 transition-colors",
                ),
                rx.el.button(
                    "Logout",
                    on_click=AuthState.handle_logout,
                    class_name="px-4 py-2 bg-orange-500 text-white rounded-lg font-semibold hover:bg-orange-600 transition-colors shadow-sm",
                ),
                class_name="flex items-center gap-6",
            ),
            rx.el.div(
                rx.el.a(
                    "Login",
                    href="/login",
                    class_name="font-medium text-gray-600 hover:text-orange-500 transition-colors",
                ),
                rx.el.a(
                    "Sign Up",
                    href="/register",
                    class_name="px-5 py-2.5 bg-orange-500 text-white rounded-lg font-semibold hover:bg-orange-600 transition-colors shadow-sm",
                ),
                class_name="flex items-center gap-4",
            ),
        ),
        class_name="flex justify-between items-center w-full max-w-7xl mx-auto p-4",
    )