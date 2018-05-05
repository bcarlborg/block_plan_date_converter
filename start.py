import re


p1 = r'(first|second|third|fourth|fifth|sixth|seventh|eighth) block'
p2 = r'block ([1-8]|one|two|three|four|five|six|seven|eight)'
# wp = r'week ([1-4]|one|two|three|four)'
# dp = r'day ([1-7]|one|two|three|four|five|six|seven)'




def parse_date(text):
    # new date d

    #CHECK IF block is present

    if re.match(p1, text, re.I):
        return block_date_to_real_date( re.match(p1, text, re.I).group() )

    if re.match(p2, text, re.I):
        return block_date_to_real_date( re.match(p2, text, re.I).group() )

    return False

'''Takes a string such as 'Block 1 and returns a date range'''




def real_date_to_block_date(real_date):

    return "block_date"
