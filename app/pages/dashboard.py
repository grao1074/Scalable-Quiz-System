import reflex as rx
from app.states.auth_state import AuthState
from app.components.navbar import navbar


def role_based_content() -> rx.Component:
    return rx.match(
        AuthState.current_user_role,
        (
            "ADMIN",
            rx.el.div(
                rx.el.h2(
                    "Admin Dashboard", class_name="text-2xl font-bold text-gray-800"
                ),
                rx.el.p(
                    "Full access to all platform features.", class_name="text-gray-600"
                ),
                class_name="p-6 bg-blue-100 border border-blue-200 rounded-lg",
            ),
        ),
        (
            "EDITOR",
            rx.el.div(
                rx.el.h2(
                    "Content Editor Dashboard",
                    class_name="text-2xl font-bold text-gray-800",
                ),
                rx.el.p(
                    "Access to CMS for managing quizzes and blog posts.",
                    class_name="text-gray-600",
                ),
                class_name="p-6 bg-green-100 border border-green-200 rounded-lg",
            ),
        ),
        (
            "PARTICIPANT",
            rx.el.div(
                rx.el.h2(
                    "Participant Dashboard",
                    class_name="text-2xl font-bold text-gray-800",
                ),
                rx.el.p(
                    "Join quizzes and view your scores.", class_name="text-gray-600"
                ),
                class_name="p-6 bg-yellow-100 border border-yellow-200 rounded-lg",
            ),
        ),
        rx.el.p("Loading content..."),
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Welcome, ",
                    rx.el.span(
                        AuthState.current_user_name, class_name="text-orange-500"
                    ),
                    "!",
                    class_name="text-4xl font-bold text-gray-800 mb-8",
                ),
                role_based_content(),
                class_name="max-w-4xl mx-auto py-12 px-4",
            )
        ),
        class_name="font-['Poppins'] bg-gray-50 min-h-screen",
    )