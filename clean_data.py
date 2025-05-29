import pandas as pd

# Step 1: Dataset Load
df = pd.read_csv('registrations.csv')

# Step 2: Remove duplicate emails
df = df.drop_duplicates(subset='email')

# Step 3: Clean 'has_joined_event' column
df['has_joined_event'] = df['has_joined_event'].astype(str).str.strip().str.lower()
df['has_joined_event'] = df['has_joined_event'].map({'yes': True, 'no': False})

# Step 4: Check LinkedIn profile column
def check_linkedin(url):
    if pd.isna(url) or url.strip() == '' or not url.startswith('http'):
        return True  # Missing or invalid
    return False

df['linkedin_missing'] = df['What is your LinkedIn profile?'].apply(check_linkedin)

# Step 5: Check Job Title column
df['job_title_missing'] = df['Job Title'].isna() | (df['Job Title'].astype(str).str.strip() == '')

# Step 6: Save cleaned data
df.to_csv('cleaned_output.csv', index=False)

print("✅ Cleaned data saved as 'cleaned_output.csv'")
