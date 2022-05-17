# Finds-phone-numbers-and-email-addresses-on-clip-board
Say you have the boring task of finding every phone number and email address in a long web page or document. If you manually scroll through the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and email addresses, you could simply press ctrl-A to select all the text, press ctrl-C to copy it to the clipboard, and then run your program. It could replace the text on the clipboard with just the phone numbers and email addresses it finds.

For example, your phone and email address extractor will need to do
the following:

• Get the text off the clipboard.
• Find all phone numbers and email addresses in the text.
• Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The code will need to do the following:

• Use the pyperclip module to copy and paste strings.
• Create two regexes, one for matching phone numbers and the other for matching email addresses.
• Find all matches, not just the first match, of both regexes.
• Neatly format the matched strings into a single string to paste.
• Display some kind of message if no matches were found in the text.
