import re

# re.sub, re.match, re.compile

def double(s: str) -> int:
    matched = re.match(r'(?P<int>\d+)', i, re.M|re.S)
    return int(matched.group('int')) * 2

i = '123abbv'
it = double(i)
print(it)