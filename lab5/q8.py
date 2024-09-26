# You have a text document that contains dates in various formats such as 12/09/2023, 2023-09-12, and Sep 12, 2023. Write a Python script that uses regular expressions to extract all dates in these formats from the text.

import re

def extract_dates(text):
    date_types = [
        r'\b\d{2}/\d{2}/\d{4}\b',            
        r'\b\d{4}-\d{2}-\d{2}\b',            
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}\b'
    ]
    
    combined_pattern = '|'.join(date_types)
    
    dates = re.findall(combined_pattern, text)
    
    return dates

text = """
Event is on 12/09/2023. The meeting is scheduled for 2023-09-12. 
Don't forget Sep 12, 2023, is the  deadline. Also, 09/10/2023 and 2023-10-09 are meeting dates.
"""

extract = extract_dates(text)

print("Extracted Dates:")
for date in extract:
    print(date)
