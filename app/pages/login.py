import reflex as rx
from app.states.auth_state import AuthState
from app.components.auth_layout import auth_layout, form_field


def login_page() -> rx.Component:
    return auth_layout(
        "Sign In to Your Account",
        rx.el.form(
            form_field("Email Address", "email", "email", "you@example.com", "mail"),
            form_field("Password", "password", "password", "••••••••", "lock"),
            rx.cond(
                AuthState.login_error != "",
                rx.el.div(
                    rx.icon("badge_alert", class_name="mr-2"),
                    AuthState.login_error,
                    class_name="flex items-center p-3 mb-4 text-sm text-red-700 bg-red-100 rounded-lg",
                ),
                None,
            ),
            rx.el.button(
                rx.cond(
                    AuthState.is_processing,
                    rx.el.div(
                        rx.spinner(class_name="mr-2"),
                        "Logging in...",
                        class_name="flex items-center justify-center",
                    ),
                    "Login",
                ),
                type="submit",
                disabled=AuthState.is_processing,
                class_name="w-full py-3 bg-orange-500 text-white font-bold rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-0.5 disabled:bg-orange-300 disabled:cursor-not-allowed",
            ),
            rx.el.p(
                "Don't have an account? ",
                rx.el.a(
                    "Sign up",
                    href="/register",
                    class_name="font-semibold text-orange-500 hover:underline",
                ),
                class_name="text-center mt-6 text-sm text-gray-600",
            ),
            on_submit=[
                AuthState.handle_login,
                rx.console_log("Submitting login form..."),
            ],
        ),
    )