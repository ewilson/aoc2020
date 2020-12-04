import re

from aoc.util import multiline_input, regex_parse_input, verify

def parse(raw_input):
    raw_passports = []
    current = []
    for line in raw_input:
        if line.strip() == '':
            raw_passports.append(list(current))
            current.clear()
        else:
            current.append(line)
    if current:
        raw_passports.append(current)
    return raw_passports


def parse2(raw_passports):
    key_vals = []
    for rp in raw_passports:
        key_val_list = []
        for s in rp:
            key_val_list.extend(s.split(' '))
        key_vals.append(key_val_list)
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
        if re.match(r'^\d+(in|cm)$', s):
            num = int(s[:-2])
            units = s[-2:]
            if units == 'in':
                return 59 <= num <= 76
            elif units == 'cm':
                return 150 <= num <= 193

    validations = {
        'byr': lambda s: year_val(s, 1920, 2002),
        'iyr': lambda s: year_val(s, 2010, 2020),
        'eyr': lambda s: year_val(s, 2020, 2030),
        'hgt': hgt_val,
        'hcl': lambda s: True if re.match(r'^#[0-9a-f]{6}$', s) else False,
        'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda s: True if re.match(r'^[0-9]{9}$', s) else False
    }
    for k in validations:
        if not k in doc or not validations[k](doc[k]):
            return False
    return True


def compute1(lines, expected=None):
    raw_passports = parse(lines)
    key_vals = parse2(raw_passports)
    docs = parse3(key_vals)
    valid_docs = [d for d in docs if valid(d)]
    return verify(expected, len(valid_docs))


def compute2(lines, expected=None):
    raw_passports = parse(lines)
    key_vals = parse2(raw_passports)
    docs = parse3(key_vals)
    valid_docs = [d for d in docs if valid2(d)]
    return verify(expected, len(valid_docs))


if __name__ == '__main__':
    test_data = multiline_input(__file__, test=True)
    data = multiline_input(__file__)
    # compute1(test_data, 2)
    result1 = compute1(data, 228)
    print(result1)
    compute2(test_data, 4)
    result2 = compute2(data)
    print(result2)
