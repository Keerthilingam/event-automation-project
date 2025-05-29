import pandas as pd

# Load cleaned data
df = pd.read_csv('cleaned_output.csv')

# Prepare message list
messages = []

for _, row in df.iterrows():
    name = row['first_name']
    job = str(row['Job Title']).strip()
    joined = row['has_joined_event']
    linkedin_missing = row['linkedin_missing']

    # Handle missing job title
    job_title = job if job else "professional"

    if joined:
        message = f"Hey {name}, thanks for joining our session! As a {job_title}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        message = f"Hi {name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job_title}."

    # Optionally: Add a note if LinkedIn profile is missing
    if linkedin_missing:
        message += " (P.S. We noticed you haven’t added a LinkedIn profile – feel free to update!)"

    messages.append({
        'email': row['email'],
        'message': message
    })

# Save to CSV
output_df = pd.DataFrame(messages)
output_df.to_csv('personalized_messages.csv', index=False)

print("✅ Messages generated and saved to 'personalized_messages.csv'")
