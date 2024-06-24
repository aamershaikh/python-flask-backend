import json
import openai
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read the JSON file
with open('/Users/aamershaikh/Documents/python-flask-backend/app/prompt/prompts.json') as f:
    data = json.load(f)

# Extract the type and prompt details
prompt_type = data[0]['Type']
prompt_details = data[0]['PromptDetails']

# OpenAI API key
openai.api_key = 'my-openai-key'

# Database setup using SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/asdb'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the Account model
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    summarizatioavailable = Column(Text)
    accountsummary = Column(Text)
    summarytext = Column(Text)

# Function to call OpenAI API
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Mapping from PromptSequence to database columns
sequence_to_column = {
    "001": "summarizatioavailable",
    "002": "accountsummary",
    "003": "summarytext"
}

# Dictionary to hold the responses
responses = {}

# Loop through the prompts and get responses
for detail in prompt_details:
    sequence = detail['PromptsSequence']
    prompt_text = detail['PromptText']
    response = get_openai_response(prompt_text)
    responses[sequence] = response

# Create a new account instance with the responses
new_account = Account(
    summarizatioavailable=responses.get("001"),
    accountsummary=responses.get("002"),
    summarytext=responses.get("003")
)

# Insert the new account into the database
session.add(new_account)
session.commit()

print("Data inserted successfully.")
