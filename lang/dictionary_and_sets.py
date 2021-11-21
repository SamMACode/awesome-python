import sys
import re
import collections
from types import MappingProxyType
from unicodedata import name


def createDict():
    """Given these ground rules, you can build dictionaries in several ways"""
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print(f"whether a == b == c == d == e, {a == b == c == d == e}")


def reverseDictItems():
    """Here the pairs are reversed: country is the key, and code is the value"""
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


def indexMappingWord():
    """Build an index mapping word -> list of occurrences, [$ python3.8 dictionary_and_sets.py main.py]"""
    WORD_RE = re.compile('\w+')
    # index = {}, using an instance of default dict instead of the setdefault method
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


def mappingProxy():
    """using MappingProxyType builds a read-only mapping-proxy instance from a dict"""
    maps = {1: 'A'}
    d_proxy = MappingProxyType(maps)
    print(f"d_proxy value: {d_proxy}, d_proxy[1]: {d_proxy[1]}")
    '''
        d_proxy[2] = 'X'
    TypeError: 'mappingproxy' object does not support item assignment
    d_proxy[2] = 'X'
    '''
    maps[2] = 'B'
    print(f"after change maps, d_proxy: {d_proxy}, d_proxy[2]: {d_proxy[2]}")
    lists = ['spam', 'spam', 'eggs', 'spam']
    print(f"set(lists) to remove duplicated items: {set(lists)}, list(set(lists)) value: {list(set(lists))}")

    # Build set of characters with codes from 32 to 255 that have the word 'SIGN' in their names
    sign_codes = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
    print(f"get unicode which's range between 32 and 256, sign_codes: {sign_codes}")


def sortDictMapEle():
    """fills three dictionaries with the same data sorted in different ways"""
    DIAL_CODES = [(86, 'China'), (91, 'India'),
                  (1, 'United States'), (62, 'Indonesia'),
                  (55, 'Brazil'), (92, 'Pakistan'),
                  (880, 'Bangladesh'), (234, 'Nigeria'),
                  (7, 'Russia'), (81, 'Japan')]
    d1 = dict(DIAL_CODES)
    # d1: dict_keys([86, 91, 1, 62, 55, 92, 880, 234, 7, 81])
    print('d1:', d1.keys())
    d2 = dict(sorted(DIAL_CODES))
    # d2: dict_keys([1, 7, 55, 62, 81, 86, 91, 92, 234, 880])
    print("d2:", d2.keys())
    d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
    # d3: {880: 'Bangladesh', 55: 'Brazil', 86: 'China', 91: 'India', 62: 'Indonesia', 81: 'Japan',
    # 234: 'Nigeria', 92: 'Pakistan', 7: 'Russia', 1: 'United States'}
    print("d3:", d3)


if __name__ == '__main__':
    map = {'name': 'jason', 'age': 20}
    #     Traceback (most recent call last):
    #   File "dictionary_and_sets.py", line 122, in <module>
    #     print(f"map['name']: {map['name']}, element that doesn't exist: ${map['ages']}")
    # KeyError: 'ages'
    # print(f"map['name']: {map['name']}, element that doesn't exist: ${map['ages']}")

    # delete the key 'name' from dictMap, update map['age'] value to 26
    map.pop('name')
    map['age'] = 26
    # to fix this problem，use map.get(key, null)方法, map['args]: $null
    print(f"map['args]: {map.get('args', 'null')}, map: {map}")

