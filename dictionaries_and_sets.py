import sys
import re
import collections

# Given these ground rules, you can build dictionaries in several ways
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(f"whether a == b == c == d == e, {a == b == c == d == e}")

DITL_CODES = [(86, 'China'),
              (91, 'India'),
              (1, 'United States'),
              (62, 'Indonesia'), (55, 'Brazil'),
              (92, 'Pakistan'),
              (880, 'Bangladesh'), (234, 'Nigeria'),
              (7, 'Russia'),
              (81, 'Japan')]
# Here the pairs are reversed: country is the key, and code is the value
country_code = {country: code for code, country in DITL_CODES}
# {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55,
#  'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
print(f"country_code - country is the key, code is the value: {country_code}")

# {1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}
reverse_dict = {code: country.upper() for country, code in country_code.items()
                if code < 66}
print(f"reverse dict: {reverse_dict}")

# Build an index mapping word -> list of occurrences, $ python3.8 dictionaries_and_sets.py main.py
WORD_RE = re.compile('\w+')
# index = {}, using an instance of defaultdict insted of the setdefault method
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            '''
            # this is ugly, coded like this to make a point
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            '''
            # index.setdefault(word, []).append(location)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


# StrKeyDict0 converts nonstring keys to str on lookup
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
