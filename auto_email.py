# auto_email.py
import yagmail
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Step 1: Enter sender details from .env
sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")

# Step 2: Yagmail SMTP setup
yag = yagmail.SMTP(user=sender_email, password=app_password)

# Step 3: Read CSV file with messages
df = pd.read_csv("personalized_messages.csv")

# Step 4: Loop and send emails
for index, row in df.iterrows():
    receiver = row['email']
    message = row['message']

    try:
        yag.send(
            to=receiver,
            subject="Follow-up: Thanks for attending / Missed you!",
            contents=message
        )
        print(f"✅ Email sent to {receiver}")
    except Exception as e:
        print(f"❌ Error sending to {receiver}: {e}")
