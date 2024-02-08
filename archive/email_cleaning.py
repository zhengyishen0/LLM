import os
from dotenv import find_dotenv, load_dotenv
import openai
import json
import csv

load_dotenv(find_dotenv())
openai.api_key = os.environ.get("OPENAI_API_KEY")
username = "zhengyishen1@gmail.com"


def parse_email(email_thread):

    system_prompt = f"""
    You are an expert of convert raw email thread into original message / reply pairs. 
    You are given a raw email thread that {username} reply to others, your goal is to convert it into original message / reply pairs. 
    - orignal_message: the last message sent to {username}, if it is a long email thread, only take the last message
    - user_reply: {username}'s reply to the original message

    if there is only one message in the thread, that should be user_reply

    The exported format should look something like 
    {{
        "original_message": "xxxx",
        "user_reply": "xxxx"
    }}
    """

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": email_thread}
        ]
    )
    # print(json.dumps(json.loads(response.model_dump_json()), indent=4))
    return response.choices[0].message.content


def process_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        processed_data = []

        for row in csv_reader:
            try:
                text = row['Body']  # Get the text from the 'body' column
                json_string = parse_email(text)
                print(json_string)
                # Convert JSON string to dictionary
                json_data = json.loads(json_string)
                original_message = json_data.get('original_message', '')
                user_reply = json_data.get('user_reply', '')
                # Append original row data and new columns to processed_data
                processed_data.append([original_message, user_reply])
            except Exception as e:
                print(f"Error processing row: {row}")
                print(e)

    # Write processed data to a new CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['original_message', 'user_reply'])
        # Write data rows
        csv_writer.writerows(processed_data)


# Paths to your input and output CSV files
input_csv_path = 'past_email_mbox.csv'
output_csv_path = 'email_pairs.csv'

# Call the function to process the CSV file
process_csv(input_csv_path, output_csv_path)
