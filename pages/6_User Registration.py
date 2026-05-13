import re

import bcrypt
import streamlit as st
import yaml
from yaml import SafeLoader


CONFIG_PATH = "login_config.yml"
USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]{3,30}$")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.load(file, Loader=SafeLoader)


def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        yaml.safe_dump(config, file, sort_keys=False)


def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


st.set_page_config(page_title="User Registration")

if "login_status" not in st.session_state or not st.session_state["login_status"]:
    st.write("You don't have access to this page")
    st.stop()

if st.session_state.get("role", "").lower() != "admin":
    st.info("Only Admins can register new users.")
    st.stop()

st.title("User Registration")

with st.form("user_registration_form", clear_on_submit=True):
    username = st.text_input("Username")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    city = st.text_input("City")
    area = st.text_input("Area")
    role = st.selectbox("Role", ["Officer", "Admin"])
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submitted = st.form_submit_button("Register User")

if submitted:
    username = username.strip()
    email = email.strip()

    if not USERNAME_PATTERN.match(username):
        st.error("Username must be 3-30 characters and use only letters, numbers, or underscores.")
        st.stop()

    if not all([name.strip(), email, city.strip(), area.strip(), password, confirm_password]):
        st.error("Please fill in all fields.")
        st.stop()

    if "@" not in email or "." not in email:
        st.error("Please enter a valid email address.")
        st.stop()

    if len(password) < 6:
        st.error("Password must be at least 6 characters long.")
        st.stop()

    if password != confirm_password:
        st.error("Passwords do not match.")
        st.stop()

    config = load_config()
    usernames = config.setdefault("credentials", {}).setdefault("usernames", {})

    if username in usernames:
        st.error("That username already exists.")
        st.stop()

    usernames[username] = {
        "email": email,
        "name": name.strip(),
        "city": city.strip(),
        "area": area.strip(),
        "role": role,
        "password": hash_password(password),
    }

    preauthorized = config.setdefault("preauthorized", {}).setdefault("emails", [])
    if email not in preauthorized:
        preauthorized.append(email)

    save_config(config)
    st.success(f"User '{username}' registered successfully.")
