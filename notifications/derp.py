import random
import string

def generate_jira_issue():
    # Generate a random 2-3 letter combination
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(2, 3)))

    # Generate a random 4-5 number combination
    numbers = ''.join(random.choice(string.digits) for _ in range(random.randint(4, 5)))

    # Combine the letter and number combinations with a hyphen
    issue_key = f"{letters}-{numbers}"

    return issue_key

# Generate and print a random Jira issue key
random_issue = generate_jira_issue()
print(random_issue)
