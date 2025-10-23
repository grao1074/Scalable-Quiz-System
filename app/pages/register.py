import reflex as rx
from app.states.auth_state import AuthState
from app.components.auth_layout import auth_layout, form_field


def register_page() -> rx.Component:
    return auth_layout(
        "Create Your Account",
        rx.el.form(
            form_field("Full Name", "full_name", "text", "John Doe", "user"),
            form_field("Email Address", "email", "email", "you@example.com", "mail"),
            form_field("Password", "password", "password", "••••••••", "lock"),
            rx.el.div(
                rx.el.label(
                    "Role",
                    html_for="role",
                    class_name="text-sm font-semibold text-gray-700",
                ),
                rx.el.select(
                    rx.el.option("Participant", value="PARTICIPANT"),
                    rx.el.option("Content Editor", value="EDITOR"),
                    rx.el.option("Admin", value="ADMIN"),
                    name="role",
                    default_value="PARTICIPANT",
                    class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400 focus:border-transparent transition-colors",
                ),
                class_name="mb-5",
            ),
            rx.cond(
                AuthState.register_error != "",
                rx.el.div(
                    rx.icon("badge_alert", class_name="mr-2"),
                    AuthState.register_error,
                    class_name="flex items-center p-3 mb-4 text-sm text-red-700 bg-red-100 rounded-lg",
                ),
                None,
            ),
            rx.el.button(
                "Create Account",
                type="submit",
                class_name="w-full py-3 bg-orange-500 text-white font-bold rounded-lg hover:bg-orange-600 transition-all duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-0.5",
            ),
            rx.el.p(
                "Already have an account? ",
                rx.el.a(
                    "Login",
                    href="/login",
                    class_name="font-semibold text-orange-500 hover:underline",
                ),
                class_name="text-center mt-6 text-sm text-gray-600",
            ),
            on_submit=AuthState.handle_registration,
        ),
    )