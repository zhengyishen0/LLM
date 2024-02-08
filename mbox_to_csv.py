import pandas as pd
import mailbox
import csv


def mbox_to_csv(mbox_file_path, csv_file_path):
    # Open the mbox file
    mbox = mailbox.mbox(mbox_file_path)

    # Open or create the csv file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header to the csv file
        writer.writerow(['Subject', 'From', 'To', 'Date', 'Body'])

        # Loop through the messages in the mbox file
        for message in mbox:
            # Write the message data to the csv file
            writer.writerow([message['subject'], message['from'],
                            message['to'], message['date'], message.get_payload()])


def get_user_emails(file_name, user_email_address):
    # Load the CSV data
    data = pd.read_csv(file_name)

    # Filter emails sent by User
    user_emails = data[data['From'] == user_email_address]

    # Identify emails that are replies
    reply_emails = user_emails[user_emails['Subject'].str.startswith('Re:')]

    # Remove the 'Re: ' part from the start of these subjects
    reply_emails['Original_Subject'] = reply_emails['Subject'].str[4:]

    # Now pair these reply emails with the original email they replied to, by matching subjects.
    original_emails = user_emails[~user_emails['Subject'].str.startswith(
        'Re:')]

    # Merge original and reply emails based on the subject (or original subject in the case of replies)
    paired_emails = pd.merge(reply_emails, original_emails, left_on='Original_Subject', right_on='Subject',
                             suffixes=('_reply', '_original'))

    # Save the paired_emails DataFrame to a CSV file
    user_name = user_email_address.split(
        '<')[0].strip().lower().replace(' ', '_')
    paired_emails.to_csv(f'data/{user_name}_emails.csv', index=False)


file_name = 'data/mbox.csv'
user_email_address = 'Zhengyi Shen <zhengyishen1@gmail.com>'

# Call the function with the path to your mbox file and the desired csv file
mbox_to_csv('data/Sent.mbox', file_name)
get_user_emails(file_name, user_email_address)
