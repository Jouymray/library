from PyPDF2 import PdfReader
import random

# Function to extract topics from the PDF
def extract_topics(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Extract numbers and topics
        topics = []
        lines = text.splitlines()
        for line in lines:
            if line.strip() and line[0].isdigit():  # Check if the line starts with a number
                parts = line.split(".", 1)  # Split on the first period
                if len(parts) > 1:
                    number = parts[0].strip()
                    topic = parts[1].strip()
                    topics.append(f"{number}. {topic}")

        return topics
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to assign topics to teams
def assign_topics_to_teams(teams_count, topics):
    if len(topics) < teams_count:
        print("Not enough topics for all teams.")
        return {}

    random.shuffle(topics)  # Shuffle the topics for randomness
    assignments = {}
    for team in range(1, teams_count + 1):
        assignments[f"Team {team}"] = topics.pop()  # Assign a topic and remove it from the list
    return assignments

# Specify the PDF file path
pdf_path = "Expert System Development Assignment.pdf"

# Number of teams
teams_count = 10

# Extract topics and assign them to teams
topics = extract_topics(pdf_path)
if topics:
    print("Extracted Topics:")
    for topic in topics:
        print(topic)

    print("\nTeam Assignments:")
    team_assignments = assign_topics_to_teams(teams_count, topics)
    for team, topic in team_assignments.items():
        print(f"{team}: {topic}")
else:
    print("No topics found in the PDF.")
