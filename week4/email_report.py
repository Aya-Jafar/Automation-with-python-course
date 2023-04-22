#!/usr/bin/env python3
import requests
import reports 
import emails

# Send a GET request to the endpoint
response = requests.get('http://34.133.124.157/fruits/')


desc_path = 'supplier-data/descriptions/'

text_data = []
for text_file in os.listdir(desc_path):
    with open(desc_path + text_file, 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])
        f.close()


if __name__ == "__main__":
  now = datetime.now()
  now = now.strftime("%B %d, %Y")
  reports.generate_report("processed.pdf",  f"Processed Update on {now}", lst)
  sender = "automation@example.com"
  receiver = "student-00-f61095d9e837@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate(sender, receiver, subject,
                            body, "processed.pdf")  # From emails.py
  emails.send(message)
