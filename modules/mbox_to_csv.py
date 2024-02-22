import pandas as pd
import mailbox
from bs4 import BeautifulSoup as bs
import quopri


def mbox_to_csv(mbox_file_path, csv_file_path):
    # Open the mbox file
    mbox = mailbox.mbox(mbox_file_path)
    msg_list = list(mbox)

    headers = ['subject', 'from', 'to', 'date', 'body']
    df = pd.DataFrame(columns=headers)

    for message in msg_list:
        if message.is_multipart():
            for submessage in message.get_payload():
                for key in headers:
                    submessage[key] = message[key]
                msg_list.append(submessage)
        else:
            payload = message.get_payload()
            if len(payload) > 2000:
                continue
            text = bs(payload, "html.parser").get_text()
            ascii_text = text.encode('ascii', 'replace').decode()
            try:
                body = quopri.decodestring(
                    ascii_text).decode()

                new_row = {}
                for key in headers:
                    new_row[key] = message[key]
                new_row['body'] = body
                df.loc[len(df)] = new_row
            except:
                pass

    df.to_csv(csv_file_path, index=False)


def get_user_emails(csv_file_path, user_name):
    # Load the CSV data
    data = pd.read_csv(csv_file_path)

    user_emails = data[data['from'].str.contains(user_name)]
    user_emails['subject'] = user_emails['subject'].fillna('')
    reply_emails = user_emails[user_emails['subject'].str.startswith('Re:')]
    reply_emails['original_subject'] = reply_emails['subject'].str[4:]

    # Now pair these reply emails with the original email they replied to, by matching subjects.
    original_emails = user_emails[~user_emails['subject'].str.startswith(
        'Re:')]

    # Merge original and reply emails based on the subject (or original subject in the case of replies)
    paired_emails = pd.merge(reply_emails, original_emails, left_on='original_subject', right_on='subject',
                             suffixes=('_reply', '_original'))

    # Save the paired_emails DataFrame to a CSV file
    paired_emails.to_csv(f'data/emails.csv', index=False)


mbox_file_path = 'data/Sent.mbox'
csv_file_path = 'data/mbox.csv'
user_name = 'Zhengyi'


# mbox_to_csv(mbox_file_path, csv_file_path)
get_user_emails(csv_file_path, user_name)
