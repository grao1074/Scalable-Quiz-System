import reflex as rx
from app.components.navbar import navbar
from app.states.homepage_state import HomepageState, Feature, Plan, Testimonial


def hero_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "The Ultimate ",
                rx.el.span("Quiz ", class_name="text-orange-500"),
                "Experience",
                class_name="text-5xl md:text-7xl font-extrabold text-gray-800 leading-tight",
            ),
            rx.el.p(
                "Engage, learn, and compete with friends and colleagues. Your next adventure in knowledge starts here!",
                class_name="mt-6 text-lg md:text-xl text-gray-600 max-w-2xl mx-auto",
            ),
            rx.el.a(
                rx.el.button(
                    "Get Started for Free",
                    rx.icon("arrow-right", class_name="ml-2"),
                    class_name="mt-10 px-8 py-4 bg-orange-500 text-white text-lg font-bold rounded-xl hover:bg-orange-600 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1",
                ),
                href="/register",
            ),
            class_name="text-center",
        ),
        class_name="max-w-7xl mx-auto flex items-center justify-center min-h-[80vh] px-4 py-20",
    )


def how_it_works_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "How It Works",
            class_name="text-4xl font-bold text-center text-gray-800 mb-4",
        ),
        rx.el.p(
            "Get started in three simple steps.",
            class_name="text-center text-gray-600 mb-12 text-lg",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("pencil", class_name="h-12 w-12 text-orange-500 mb-4"),
                rx.el.h3("1. Create", class_name="text-2xl font-bold mb-2"),
                rx.el.p(
                    "Build engaging quizzes with our easy-to-use quiz creator.",
                    class_name="text-gray-600",
                ),
                class_name="text-center p-6",
            ),
            rx.el.div(
                rx.icon("send", class_name="h-12 w-12 text-orange-500 mb-4"),
                rx.el.h3("2. Launch", class_name="text-2xl font-bold mb-2"),
                rx.el.p(
                    "Host live quiz sessions and invite participants to join.",
                    class_name="text-gray-600",
                ),
                class_name="text-center p-6",
            ),
            rx.el.div(
                rx.icon("bar-chart-big", class_name="h-12 w-12 text-orange-500 mb-4"),
                rx.el.h3("3. Analyze", class_name="text-2xl font-bold mb-2"),
                rx.el.p(
                    "Review results and gain insights with our detailed analytics.",
                    class_name="text-gray-600",
                ),
                class_name="text-center p-6",
            ),
            class_name="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto",
        ),
        class_name="py-20 bg-white",
    )


def feature_card(feature: Feature) -> rx.Component:
    return rx.el.div(
        rx.icon(feature["icon"], class_name="h-10 w-10 text-orange-500 mb-4"),
        rx.el.h3(feature["title"], class_name="text-xl font-bold text-gray-800 mb-2"),
        rx.el.p(feature["description"], class_name="text-gray-600"),
        class_name="bg-white p-6 rounded-xl shadow-md border border-gray-100 hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def features_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Platform Features",
            class_name="text-4xl font-bold text-center text-gray-800 mb-12",
        ),
        rx.el.div(
            rx.foreach(HomepageState.features, feature_card),
            class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-7xl mx-auto",
        ),
        class_name="py-20 px-4",
    )


def pricing_card(plan: Plan) -> rx.Component:
    return rx.el.div(
        rx.cond(
            plan["is_popular"],
            rx.el.div(
                "Most Popular",
                class_name="absolute top-0 -translate-y-1/2 left-1/2 -translate-x-1/2 bg-orange-500 text-white px-3 py-1 text-sm font-bold rounded-full",
            ),
            None,
        ),
        rx.el.h3(plan["title"], class_name="text-2xl font-bold text-gray-800 mb-4"),
        rx.el.div(
            rx.el.span(plan["price"], class_name="text-5xl font-extrabold"),
            rx.el.span("/month", class_name="text-gray-500"),
            class_name="mb-6 flex items-baseline",
        ),
        rx.el.ul(
            rx.foreach(
                plan["features"],
                lambda feature: rx.el.li(
                    rx.icon("square_check", class_name="h-5 w-5 text-green-500 mr-2"),
                    feature,
                    class_name="flex items-center text-gray-600 mb-2",
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.button(
            plan["cta"],
            class_name=rx.cond(
                plan["is_popular"],
                "w-full py-3 bg-orange-500 text-white font-bold rounded-lg hover:bg-orange-600",
                "w-full py-3 bg-gray-200 text-gray-800 font-bold rounded-lg hover:bg-gray-300",
            ),
        ),
        class_name=rx.cond(
            plan["is_popular"],
            "relative bg-white p-8 rounded-xl shadow-2xl border-2 border-orange-500",
            "bg-white p-8 rounded-xl shadow-lg border border-gray-100",
        ),
    )


def pricing_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Pricing & Plans",
            class_name="text-4xl font-bold text-center text-gray-800 mb-12",
        ),
        rx.el.div(
            rx.foreach(HomepageState.plans, pricing_card),
            class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto items-center",
        ),
        class_name="py-20 bg-white px-4",
    )


def testimonial_card(testimonial: Testimonial) -> rx.Component:
    return rx.el.div(
        rx.el.p(f'''"{testimonial["quote"]}"''', class_name="text-gray-600 mb-6"),
        rx.el.div(
            rx.image(src=testimonial["avatar"], class_name="h-12 w-12 rounded-full"),
            rx.el.div(
                rx.el.h4(testimonial["name"], class_name="font-bold text-gray-800"),
                rx.el.p(testimonial["role"], class_name="text-gray-500 text-sm"),
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="bg-white p-8 rounded-xl shadow-md border border-gray-100",
    )


def testimonials_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "What Our Users Say",
            class_name="text-4xl font-bold text-center text-gray-800 mb-12",
        ),
        rx.el.div(
            rx.foreach(HomepageState.testimonials, testimonial_card),
            class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto",
        ),
        class_name="py-20 px-4",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.h3("Product", class_name="text-lg font-bold text-gray-800 mb-4"),
                rx.el.a(
                    "Features",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                rx.el.a(
                    "Pricing",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                rx.el.a(
                    "How It Works",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                class_name="flex flex-col gap-2",
            ),
            rx.el.div(
                rx.el.h3(
                    "Resources", class_name="text-lg font-bold text-gray-800 mb-4"
                ),
                rx.el.a(
                    "Blog", href="#", class_name="text-gray-600 hover:text-orange-500"
                ),
                rx.el.a(
                    "Help Center",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                rx.el.a(
                    "API Docs",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                class_name="flex flex-col gap-2",
            ),
            rx.el.div(
                rx.el.h3("Company", class_name="text-lg font-bold text-gray-800 mb-4"),
                rx.el.a(
                    "About Us",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                rx.el.a(
                    "Careers",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                rx.el.a(
                    "Contact",
                    href="#",
                    class_name="text-gray-600 hover:text-orange-500",
                ),
                class_name="flex flex-col gap-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("swords", class_name="size-8 text-orange-500"),
                    rx.el.span(
                        "QuizWhiz", class_name="text-2xl font-bold text-gray-800"
                    ),
                    class_name="flex items-center gap-2 mb-4",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("twitter", class_name="h-6 w-6"),
                        href="#",
                        class_name="text-gray-500 hover:text-orange-500",
                    ),
                    rx.el.a(
                        rx.icon("facebook", class_name="h-6 w-6"),
                        href="#",
                        class_name="text-gray-500 hover:text-orange-500",
                    ),
                    rx.el.a(
                        rx.icon("linkedin", class_name="h-6 w-6"),
                        href="#",
                        class_name="text-gray-500 hover:text-orange-500",
                    ),
                    rx.el.a(
                        rx.icon("instagram", class_name="h-6 w-6"),
                        href="#",
                        class_name="text-gray-500 hover:text-orange-500",
                    ),
                    class_name="flex gap-4",
                ),
            ),
            class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-12 max-w-7xl mx-auto",
        ),
        rx.el.div(
            rx.el.p(
                "© 2024 QuizWhiz. All rights reserved.",
                class_name="text-center text-gray-500 text-sm",
            ),
            class_name="border-t border-gray-200 mt-12 pt-8",
        ),
        class_name="bg-gray-100 py-12 px-4",
    )


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero_section(),
            how_it_works_section(),
            features_section(),
            pricing_section(),
            testimonials_section(),
            footer(),
        ),
        class_name="font-['Poppins'] bg-gray-50",
    )