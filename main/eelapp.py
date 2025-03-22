import eel
import os
import sys  # ✅ Added missing import

# Get absolute path of "web" folder
web_folder = os.path.join(os.path.dirname(__file__), "web")

# Debug print to check if the folder exists
print(f"📂 Checking web folder: {web_folder}")
if not os.path.exists(web_folder):
    print("❌ ERROR: Web folder not found!")
    exit()

# Initialize eel
eel.init(web_folder)

# Debug print to check if the HTML file exists
html_file = "index.html"
html_path = os.path.join(web_folder, html_file)
print(f"📝 Checking HTML file: {html_path}")

if not os.path.exists(html_path):
    print("❌ ERROR: HTML file not found!")
    exit()

# Start Eel app (without fullscreen argument)
print("🚀 Starting Eel app...")

# Different methods based on OS
if sys.platform == "win32":
    options = {
        'mode': 'chrome',  # Use Chrome if available
        'host': 'localhost',
        'port': 8080,
        'cmdline_args': ['--start-fullscreen']  # Makes Chrome fullscreen
    }
else:
    options = {
        'mode': 'default',
        'host': 'localhost',
        'port': 8080
    }

eel.start(html_file, **options)
