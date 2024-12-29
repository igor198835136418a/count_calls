calls = 0

def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    len(string)
    string.upper()
    string.lower()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string_lo = string.lower()

    return string_lo in [item.lower() for item in list_to_search]

print(string_info('Abakan'))
print(string_info('Moscow_City'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)