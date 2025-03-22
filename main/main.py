import os
import json
import time
import random
import sys
import tkinter as tk
from tkinter import messagebox

USER_FILE = "user_data.json"

class PythonOS:
    def __init__(self):
        self.installed = os.path.exists(USER_FILE)
        self.username = None
        self.password = None
        self.command_count = 0
        self.logged_in = False

        if self.installed:
            self.load_user()

    def vinstall_menu(self):
        if self.installed:
            print("System detected. Booting into FireOS...")
        else:
            print("Welcome to LAVinstall - FireOS Installer")
            print("1) Install FireOS with LAV-INSTALLER")
            print("2) Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.install_os()
            else:
                print("Installation aborted.")
                exit()

    def install_os(self):
        print("Installing FireOS...\n")
        for i in range(1, 101):
            time.sleep(0.1)
            print(f"Copying file {i}/100 to /system")

        print("\nThank You For Installing FireOS")
        self.setup_user()
        self.installed = True

    def setup_user(self):
        print("\nUser Setup:")
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.save_user()
        print("User created successfully!\n")

    def save_user(self):
        with open(USER_FILE, "w") as f:
            json.dump({"username": self.username, "password": self.password}, f)

    def load_user(self):
        with open(USER_FILE, "r") as f:
            data = json.load(f)
            self.username = data["username"]
            self.password = data["password"]

    def shell(self):
        while True:
            if not self.logged_in:
                self.login_prompt()

            cmd = input("root@vos: $ ")
            self.command_count += 1

            if cmd == "exit":
                print("Shutting down...")
                exit()
            elif cmd == "help":
                print("Available commands: help, exit, echo, clear, install, reboot, gui start, reset")
            elif cmd.startswith("echo "):
                print(cmd[5:])
            elif cmd == "clear":
                print("\033c", end="")
            elif cmd == "install":
                print("Installing software package...")
            elif cmd == "reboot":
                print("Rebooting system...\n")
                self.vinstall_menu()
            elif cmd == "gui start":
                self.start_gui()
            elif cmd == "reset":
                self.reset_system()
            else:
                print("Command not found.")

            if self.command_count == 23:
                print("\nSystem setup complete. You must now log in.")
                self.command_count += 1
                self.logged_in = False

    def login_prompt(self):
        print("\n=== Login Required ===")
        while True:
            usr = input("Username: ")
            pwd = input("Password: ")
            if usr == self.username and pwd == self.password:
                print("Login successful!\n")
                self.logged_in = True
                break
            else:
                print("Invalid credentials, try again.")

    def start_gui(self):
        eelapp_path = os.path.join(os.path.dirname(__file__), "eelapp.py")

        if os.path.exists(eelapp_path):
            print("✅ Launching GUI...")
            os.system(f'python "{eelapp_path}"')
        else:
            print(f"❌ ERROR: eelapp.py not found at {eelapp_path}")


    def reset_system(self):
        print("\nResetting system...")
        if os.path.exists(USER_FILE):
            os.remove(USER_FILE)
        print("System has been reset. Please restart the OS.\n")
        exit()

if __name__ == "__main__":
    os_sim = PythonOS()
    os_sim.vinstall_menu()
    os_sim.shell()
