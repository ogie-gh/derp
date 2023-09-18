import click
import os
import random
import string


def generate_jira_issue(prefix):
    # Generate a random 4-digit number combination
    numbers = ''.join(random.choice(string.digits) for _ in range(4))

    # Combine the user-defined prefix and the number combination with a hyphen
    issue_key = f"{prefix}-{numbers}"

    return issue_key

def set_env(key):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'issue={key}', file=fh)

@click.command()
@click.option("--prefix", help='User-defined prefix for the Jira issue', required=True)
@click.option("--summary", help="Summary of the issue to be created", required=True)
@click.option("--description", help="Description field contents", required=True)
def main(prefix, summary, description):
        random_issue = generate_jira_issue(prefix.upper())
        print(random_issue, summary, description)
        set_env(random_issue)

if __name__ == '__main__':
    main()
