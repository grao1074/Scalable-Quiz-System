import reflex as rx


def auth_layout(title: str, *children) -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("swords", class_name="h-12 w-12 text-orange-500"),
                    class_name="mx-auto mb-6 bg-orange-100 p-3 rounded-full",
                ),
                rx.el.h1(
                    title,
                    class_name="text-3xl font-bold text-center text-gray-800 mb-2",
                ),
                rx.el.p(
                    "Welcome to QuizWhiz! Let the games begin.",
                    class_name="text-center text-gray-500 mb-8",
                ),
                *children,
                class_name="w-full max-w-md p-8 bg-white rounded-2xl shadow-lg border border-gray-100",
            ),
            class_name="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-4",
        ),
        class_name="font-['Poppins']",
    )


def form_field(
    label: str, name: str, input_type: str, placeholder: str, icon_tag: str
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label, html_for=name, class_name="text-sm font-semibold text-gray-700"
        ),
        rx.el.div(
            rx.icon(
                icon_tag,
                class_name="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400",
            ),
            rx.el.input(
                id=name,
                name=name,
                type=input_type,
                placeholder=placeholder,
                class_name="w-full pl-10 pr-4 py-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-400 focus:border-transparent transition-colors",
            ),
            class_name="relative mt-2",
        ),
        class_name="mb-5",
    )