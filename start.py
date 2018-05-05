import re


p1 = r'(first|second|third|fourth|fifth|sixth|seventh|eighth) block'
p2 = r'block ([1-8]|one|two|three|four|five|six|seven|eight)'


def parse_date(text):

    if re.match(p1, text, re.I):
        return block_date_to_real_date( re.match(p1, text, re.I).group() )

    if re.match(p2, text, re.I):
        return block_date_to_real_date( re.match(p2, text, re.I).group() )

    return False

def block_date_to_real_date(block_date):

    return block_date



def real_date_to_block_date(real_date):

    return "block_date"
