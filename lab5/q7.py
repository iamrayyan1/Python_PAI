# You have a block of text that contains several email addresses scattered throughout. Write a Python script that uses regular expressions to extract all valid email addresses from the text.
 
import re

def extract(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(email_pattern, text)
    
    return emails

text = """
Hello, you can reach out to me at rrija.fast@example.com or ali.rija123@domain.co.uk.
For further inquiries, contact fast@company.com or nuces@business.org. 
Invalid email formats like user@com, someone@.com will not be extracted.
"""

emails = extract(text)

print("Extracted Emails:")
for email in emails:
    print(email)
