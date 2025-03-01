# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_string):
        """Initialize with a string containing email addresses."""
        if not isinstance(email_string, str):
            raise TypeError("Email string must be a string.")
        self.email_string = email_string

    def parse(self):
        """Parse the email string into a sorted list of unique email addresses."""
        # Replace commas with spaces to normalize separators, then split on whitespace
        normalized_string = self.email_string.replace(',', ' ')
        potential_emails = normalized_string.split()

        # Regular expression for basic email validation
        # Matches: username@domain.tld (allows dots, letters, numbers, etc.)
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        # Filter valid emails, remove duplicates, and sort
        valid_emails = [item for item in potential_emails if email_pattern.match(item)]
        unique_emails = sorted(list(set(valid_emails)))

        return unique_emails