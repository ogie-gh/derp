import click
import os
import random
import string
import json

@click.command()
@click.option("--auth-token", help="token for auth", required=True)
@click.option("--auth-user", help="user for auth", required=True)
def main(auth_token, auth_user):
  print(auth_token)
  print(auth_user)

if __name__ == '__main__':
    main()
