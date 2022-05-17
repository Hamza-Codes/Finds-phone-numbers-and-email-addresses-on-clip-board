# Finds phone numbers and email addresses on clip board
import pyperclip
import re


# Step - 01: Create a Regex for Phone Numbers

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code - The phone number begins with an optional area code, so the area code group is followed with a                                 question mark. the area code can be just three digits (that is, \d{3}) or three digits within parentheses                       (that is, \(\d{3}\)).

    (\s|-|\.)?                      # seperator - The phone number separator character can be a space (\s), hyphen (-), or period (.), so           these                             parts should also be joined by pipes

    (\d{3})                         # first 3 digits

    (\s|-|\.)                       # seperator

    (\d{4})                         # last 4 digits

    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension

    )''', re.VERBOSE)


# Step - 02: Create a Regex for email addresses. The username part of the email address u is one or more characters that can be any of the following: lowercase and uppercase letters, numbers, a dot, an underscore, a percent sign, a plus sign, or a hyphen. You can put all of these into a character class: [a-zA-Z0-9._ % +-].

emailRegex = re.compile(r'''(
    [a-zA-Zo-9._%+-]+         # username
    @                         # @ symbol
    [a-zA-Zo-9.-]             # domain name
    (\.[a-zA-Z]{2,4})         # dot-somthing
)''', re.VERBOSE)

# step - 03: Find All Matches in the Clipboard Text

# Find matches in clipboard text.

text = str(pyperclip.paste())

# It starts off as an empty list, and a couple for loops. For the email addresses, you append group 0 of each match w. For the matched phone numbers, you don’t want to just append group 0. While the program detects phone numbers in several formats, you want the phone number appended to be in a single, standard format. The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text v. (These groups are the area code, first three digits, last four digits, and extension.)


matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups1], groups[3], groups[5])
    if groups[8] != '':
        phoneNum += 'x'+groups[8]
    machtes.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# There is one tuple for each match, and each tuple contains strings for each group in the regular expression. Remember that group 0 matches the # # # entire regular expression, so the group at index 0 of the tuple is the one you are interested in


# Step 4: Join the Matches into a String for the Clipboard

# Now that you have the email addresses and phone numbers as a list of strings in matches, you want to put them on the clipboard. The pyperclip.copy() function takes only a single string value, not a list of strings, so you call the join() method on matches.

# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found.')
