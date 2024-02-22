import pandas as pd

# Load the data
data = pd.read_csv('past_email_mbox.csv')

# Identify all reply emails and their original subjects (i.e., remove "Re:")
data['Original_Subject'] = data.loc[data['Subject'].str.startswith(
    'Re:'), 'Subject'].str.replace('Re: ', '')

# Identify all original emails
original_emails_all = data[~data['Subject'].str.startswith('Re:')]

# Pair all reply emails with their corresponding original emails
paired_emails_all = pd.merge(data, original_emails_all, how='inner', left_on=['Original_Subject', 'To'],
                             right_on=['Subject', 'To'], suffixes=('_reply', '_original'))

# Save all reply and original email pairs to a CSV file
paired_emails_all.to_csv('output.csv', index=False)
