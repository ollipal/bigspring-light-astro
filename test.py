import re

pattern = r'^(\/(blog|pricing|contact|faq)?\/?)$'
strings = ['/', '/blog', '/pricing/', '/contact', '/faq', '/about', '/faqa']

for string in strings:
    if re.match(pattern, string):
        print(f"Matched: {string}")
    else:
        print(f"Not matched: {string}")