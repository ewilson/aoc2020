import re

from aoc.util import multiple_line_records, verify


def parse2(raw_passports):
    key_vals = [rp.split(' ') for rp in raw_passports]
    return key_vals


def parse3(data):
    pps = []
    for li in data:
        pd = {}
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        for s in li:
            for f in fields:
                if s[0:3] == f:
                    pd[f] = s[4:]
        pps.append(pd)
    return pps


def valid(doc):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for rf in required_fields:
        if rf not in doc:
            return False
    return True


def valid2(doc):
    def year_val(s, start, end):
        if re.match(r'^\d{4}$', s):
            return start <= int(s) <= end

    def hgt_val(s):
        match = re.match(r'^(\d+)(in|cm)$', s)
        if match:
            num, units = match.groups()
            return 59 <= int(num) <= 76 if units == 'in' else 150 <= int(num) <= 193

    validations = {
        'byr': lambda s: year_val(s, 1920, 2002),
        'iyr': lambda s: year_val(s, 2010, 2020),
        'eyr': lambda s: year_val(s, 2020, 2030),
        'hgt': hgt_val,
        'hcl': lambda s: re.match(r'^#[0-9a-f]{6}$', s),
        'ecl': lambda s: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', s),
        'pid': lambda s: re.match(r'^[0-9]{9}$', s)
    }
    for k in validations:
        if k not in doc or not validations[k](doc[k]):
            return False
    return True


def compute1(records, expected=None):
    key_vals = parse2(records)
    docs = parse3(key_vals)
    valid_docs = [d for d in docs if valid(d)]
    return verify(expected, len(valid_docs))


def compute2(records, expected=None):
    key_vals = parse2(records)
    docs = parse3(key_vals)
    valid_docs = [d for d in docs if valid2(d)]
    return verify(expected, len(valid_docs))


if __name__ == '__main__':
    test_data = multiple_line_records(__file__, test=True)
    data = multiple_line_records(__file__)
    # compute1(test_data, 2)
    result1 = compute1(data, 228)
    print(result1)
    compute2(test_data, 4)
    result2 = compute2(data, 175)
    print(result2)
