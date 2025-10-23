import reflex as rx
from app.states.auth_state import AuthState
from app.components.navbar import navbar


def profile_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Manage Your Profile",
                    class_name="text-4xl font-bold text-gray-800 mb-8",
                ),
                rx.el.div(
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Full Name",
                                class_name="text-sm font-semibold text-gray-700",
                            ),
                            rx.el.input(
                                name="full_name",
                                default_value=AuthState.current_user_name,
                                key=AuthState.current_user_name,
                                class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Email Address",
                                class_name="text-sm font-semibold text-gray-700",
                            ),
                            rx.el.input(
                                name="email",
                                disabled=True,
                                class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg bg-gray-100 cursor-not-allowed",
                                default_value=AuthState.logged_in_user["email"],
                                key=AuthState.logged_in_user["email"],
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "New Password (optional)",
                                class_name="text-sm font-semibold text-gray-700",
                            ),
                            rx.el.input(
                                name="password",
                                type="password",
                                placeholder="Leave blank to keep current password",
                                class_name="w-full mt-2 p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Role", class_name="text-sm font-semibold text-gray-700"
                            ),
                            rx.el.div(
                                rx.icon("shield", class_name="mr-2"),
                                rx.el.span(AuthState.current_user_role),
                                class_name="flex items-center mt-2 px-4 py-2.5 bg-gray-100 text-gray-600 rounded-lg font-medium",
                            ),
                            class_name="mb-8",
                        ),
                        rx.el.button(
                            "Update Profile",
                            type="submit",
                            class_name="w-full py-3 bg-orange-500 text-white font-bold rounded-lg hover:bg-orange-600 transition-all shadow-md",
                        ),
                        on_submit=AuthState.update_profile,
                    ),
                    class_name="p-8 bg-white rounded-2xl shadow-lg border border-gray-100",
                ),
                class_name="max-w-2xl mx-auto py-12 px-4",
            )
        ),
        class_name="font-['Poppins'] bg-gray-50 min-h-screen",
    )