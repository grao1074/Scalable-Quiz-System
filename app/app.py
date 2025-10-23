import reflex as rx
from app.states.auth_state import AuthState
from app.states.quiz_state import QuizState
from app.pages.index import index
from app.pages.login import login_page
from app.pages.register import register_page
from app.pages.dashboard import dashboard_page
from app.pages.profile import profile_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
from app.pages.quizzes import quizzes_page
from app.pages.create_quiz import create_quiz_page

app.add_page(
    dashboard_page, route="/dashboard", on_load=AuthState.check_auth_and_redirect
)
app.add_page(profile_page, route="/profile", on_load=AuthState.check_auth_and_redirect)
app.add_page(quizzes_page, route="/quizzes", on_load=AuthState.check_auth_and_redirect)
app.add_page(
    create_quiz_page,
    route="/quizzes/create",
    on_load=[AuthState.check_auth_and_redirect, QuizState.reset_new_quiz],
)