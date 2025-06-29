# Crafted-Gmail

Crafted Gmail Generator is a Python-based tool designed for security researchers and bug bounty hunters. It helps generate a Gmail-like string of exactly 255 characters, ending with M at the 255th position. This is useful for testing input truncation, buffer limits, or crafted payloads in email fields during vulnerability assessments.

🖥️ Features
🧱 Builds a Gmail-like address with precise 255-character length.

🎨 Uses ASCII art for a cool interface with pyfiglet.

✅ Ensures the crafted email ends with 'M' (for payload testing).

🐍 User-friendly prompts with emoji guidance.

💡 Bug bounty focused — send this through Burp Suite for testing.

📦 Requirements
Python 3.x

pyfiglet (for ASCII art)

Install with:

bash
Copy
Edit
pip install pyfiglet
🚀 How It Works
You enter the domain extension (.exploit-0a0d002b04c0dcac80d4989101a200a2.exploit-server.net).

You enter the email username (@dontwannacry.com).

The tool calculates how many characters to fill to reach 254.

You choose your lucky alphabet (like x) to repeat.

Tool appends 'M' to make the total 255 characters.

Use the crafted string for input testing (e.g., in Burp Suite).

🧪 Example Output
yaml
Copy
Edit
Enter your lucky alphabet: Z

Generated:
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz@dontwannacry.com.exploit-0a3e003e04c850cc8021cfe401f100e0.exploit-server.net

Length: 255

paste the Generated mail check vulnerable exist or not.😁😁
