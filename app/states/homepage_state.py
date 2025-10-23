import reflex as rx
from typing import TypedDict


class Feature(TypedDict):
    icon: str
    title: str
    description: str


class Plan(TypedDict):
    title: str
    price: str
    features: list[str]
    cta: str
    is_popular: bool


class Testimonial(TypedDict):
    quote: str
    name: str
    role: str
    avatar: str


class HomepageState(rx.State):
    features: list[Feature] = [
        {
            "icon": "zap",
            "title": "Real-time Quizzes",
            "description": "Engage your audience with live quizzes that are both fun and interactive. Perfect for classrooms and corporate training.",
        },
        {
            "icon": "bar-chart-2",
            "title": "Analytics Dashboard",
            "description": "Track performance, identify knowledge gaps, and get detailed insights with our powerful analytics tools.",
        },
        {
            "icon": "file-text",
            "title": "Content Management",
            "description": "Easily create, edit, and organize your quizzes and other content with our intuitive CMS.",
        },
        {
            "icon": "smartphone",
            "title": "Mobile-First Design",
            "description": "A seamless experience on any device. Participants can join and play from their phones, tablets, or desktops.",
        },
    ]
    plans: list[Plan] = [
        {
            "title": "Free",
            "price": "$0",
            "features": [
                "For Participants",
                "Join unlimited quizzes",
                "Track personal scores",
                "Basic support",
            ],
            "cta": "Get Started",
            "is_popular": False,
        },
        {
            "title": "Pro",
            "price": "$29",
            "features": [
                "For Educators & Teams",
                "Create unlimited quizzes",
                "Advanced analytics",
                "Priority support",
            ],
            "cta": "Choose Pro",
            "is_popular": True,
        },
        {
            "title": "Enterprise",
            "price": "Custom",
            "features": [
                "For Organizations",
                "Custom branding",
                "Dedicated account manager",
                "24/7 support",
            ],
            "cta": "Contact Us",
            "is_popular": False,
        },
    ]
    testimonials: list[Testimonial] = [
        {
            "quote": "QuizWhiz has transformed my classroom! My students are more engaged than ever, and the analytics help me tailor my teaching.",
            "name": "Sarah Johnson",
            "role": "High School Teacher",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Sarah",
        },
        {
            "quote": "We use QuizWhiz for corporate training, and it's been a game-changer. Our employees love the interactive format.",
            "name": "David Chen",
            "role": "HR Manager, TechCorp",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=David",
        },
        {
            "quote": "As a student, I find QuizWhiz much more fun than traditional study methods. The competition aspect is a great motivator!",
            "name": "Maria Rodriguez",
            "role": "University Student",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Maria",
        },
    ]