# 🎉 Event Automation Project

This is an automation system built with Python to handle event registrations, clean registration data, generate custom messages, and send emails — ideal for efficiently managing event logistics.

---

## 📌 Features

- ✅ Registration data handling from CSV
- 🧹 Data cleaning using `pandas`
- 📬 Auto-generation of personalized messages
- ✉️ Email sending using SMTP
- 🖥️ Web interface (in progress)

---

## 🛠️ Technologies Used

- Python
- Pandas
- CSV Handling
- SMTP for Email
- Flask (for Web App interface)

---

## 📂 Project Structure

```bash
event-automation-project/
│
├── registrations.csv           # Raw registrations
├── cleaned_output.csv          # Cleaned and validated data
├── clean_data.py               # Script to clean CSV
├── generate_messages.py        # Create custom messages
├── auto_email.py               # Send emails automatically
├── app.py                      # Flask WebApp (optional step)
├── .gitignore
└── README.md                   # You are here ✅
1. Clone the Repo
bash
Copy code
git clone https://github.com/Keerthilingam/event-automation-project.git
cd event-automation-project
2. Install Requirements
bash
Copy code
3. Run Scripts
bash
Copy code
python clean_data.py
python generate_messages.py
python auto_email.py


🌐 Web App (Coming Soon)
We're building a simple Flask-based UI to:

Upload CSV registrations

View & clean data

Trigger email sending

Stay tuned for updates!

🙌 Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📫 Contact
Created by @Keerthilingam

yaml
Copy code
# Step 1: Clean data
python clean_data.py

# Step 2: Generate messages
python generate_messages.py

# Step 3: Send emails
python auto_email.py
 Features

- Read and clean raw event data
- Generate personalized messages for each registrant
- Send automated emails using Python
- Handle CSV file input/output
- Easy-to-edit templates and code
 Features

- Read and clean raw event data
- Generate personalized messages for each registrant
- Send automated emails using Python
- Handle CSV file input/output
- Easy-to-edit templates and code



