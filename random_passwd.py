#!/usr/bin/env python3
# Challenge:
# Making a random password generator
# Originally coded for sololearn:
# https://code.sololearn.com/c2RjeH7a5GjI/#py
import random, re, string

def validate(password):
  # check if password contains:
  # a letter..
  letter = re.search(r"[a-zA-Z]",
    password) is None
  # a digit..
  digit = re.search(r"\d", password) is None
  # a symbol..
  symbol = re.search(r"\W", password) is None
  # the blood of a virgin... ok, no.  
  return not(letter or digit or symbol)


def random_password(length):
  charset = (
    string.ascii_letters
    + string.digits
    + string.punctuation
  )
  return ''.join((
    random.choice(charset)
      for ch in range(length)
  ))


def main():
  try:
    # Enter the length of your password
    passwd_len = int(input("Enter the length of your password: "))
  except ValueError:
    print("Please enter a number!")
    return 1
        
  if passwd_len >= 3 and passwd_len <= 100:
    password = ""
    while not validate(password):
      password = random_password(passwd_len)
    print("Your shiny brand new password:")
    print("-"*30)
    print(password)
        
  else:
    print("Please enter a number between 3 and 100.")


if __name__ == "__main__":
    main()

