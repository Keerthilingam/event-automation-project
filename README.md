# event-automation-project
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
🖥️ 1. Clone the Repo

git clone https://github.com/Keerthilingam/event-automation-project.git
cd event-automation-project
 2. Install Requirements

3. Run Scripts
bash
Copy code

🌐 Web App (Coming Soon)
We're building a simple Flask-based UI to:

Upload CSV registrations

View & clean data

Trigger email sending

Stay tuned for updates!
!

🙌 Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change

# Step 1: Clean data
python clean_data.py

# Step 2: Generate messages
python generate_messages.py

# Step 3: Send emails
python auto_email.py

📌 Future Improvements
Add GUI interface for non-technical users

Use templates for email messages

Add logging and error handling

Schedule email sending with cron or task scheduler

🙋‍♂️ Author
Made with ❤️ by Keerthi Lingam
GitHub: @Keerthilingam



