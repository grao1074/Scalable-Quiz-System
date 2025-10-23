import reflex as rx
from typing import Literal, TypedDict
import asyncio

UserRole = Literal["ADMIN", "EDITOR", "PARTICIPANT"]


class User(TypedDict):
    email: str
    full_name: str
    password_hash: str
    role: UserRole


class AuthState(rx.State):
    users: dict[str, User] = {
        "admin@example.com": {
            "email": "admin@example.com",
            "full_name": "Admin User",
            "password_hash": "admin123",
            "role": "ADMIN",
        }
    }
    logged_in_user: User | None = None
    login_error: str = ""
    register_error: str = ""
    is_processing: bool = False
    redirect_to: str = ""

    @rx.var
    def is_authenticated(self) -> bool:
        return self.logged_in_user is not None

    @rx.var
    def current_user_role(self) -> str:
        if self.logged_in_user:
            return self.logged_in_user["role"]
        return ""

    @rx.var
    def current_user_name(self) -> str:
        if self.logged_in_user:
            return self.logged_in_user["full_name"]
        return ""

    @rx.event
    def set_processing(self, processing: bool):
        self.is_processing = processing

    @rx.event
    def handle_registration(self, form_data: dict):
        self.register_error = ""
        email = form_data.get("email", "").lower()
        password = form_data.get("password", "")
        full_name = form_data.get("full_name", "")
        role = form_data.get("role", "PARTICIPANT")
        if not all([email, password, full_name, role]):
            self.register_error = "All fields are required."
            return
        if email in self.users:
            self.register_error = "An account with this email already exists."
            return
        new_user: User = {
            "email": email,
            "full_name": full_name,
            "password_hash": password,
            "role": role,
        }
        self.users[email] = new_user
        self.logged_in_user = new_user
        return rx.redirect("/dashboard")

    @rx.event
    async def handle_login(self, form_data: dict):
        self.login_error = ""
        self.is_processing = True
        yield
        try:
            await asyncio.sleep(0.5)
            email = form_data.get("email", "").lower()
            password = form_data.get("password", "")
            if not email or not password:
                self.login_error = "Email and password are required."
                self.is_processing = False
                return
            user = self.users.get(email)
            if user and user["password_hash"] == password:
                self.logged_in_user = user
                self.is_processing = False
                yield rx.redirect("/dashboard")
                return
            self.login_error = "Invalid email or password."
        finally:
            self.is_processing = False

    @rx.event
    def handle_logout(self):
        self.logged_in_user = None
        return rx.redirect("/")

    @rx.event
    def update_profile(self, form_data: dict):
        if self.logged_in_user:
            email = self.logged_in_user["email"]
            self.users[email]["full_name"] = form_data.get(
                "full_name", self.users[email]["full_name"]
            )
            if form_data.get("password"):
                self.users[email]["password_hash"] = form_data["password"]
            self.logged_in_user = self.users[email]
            return rx.toast.success("Profile updated successfully!")

    @rx.event
    async def check_auth_and_redirect(self):
        if not self.is_authenticated:
            self.redirect_to = self.router.page.path
            yield rx.redirect("/")

    @rx.event
    def require_role(self, role: UserRole):
        @rx.event
        async def check_role_and_redirect():
            if not self.is_authenticated:
                self.redirect_to = self.router.page.path
                yield rx.redirect("/")
            elif self.logged_in_user["role"] != role:
                yield rx.redirect("/dashboard")

        return check_role_and_redirect