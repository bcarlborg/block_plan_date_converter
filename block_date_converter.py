import datetime
import re
import sys
import os

block_pattern1 = r'(first|second|third|fourth|fifth|sixth|seventh|eigth|1st|2st|3rd|4th|5th|6th|7th|8th) block'
block_pattern2 = r'block ([1-8]|one|two|three|four|five|six|seven|eigth)'
week_pattern1 = r'(first|second|third|fourth|1st|2st|3rd|4th) week'
week_pattern2 = r'week ([1-4]|one|two|three|four)'
day_pattern = r'day ([1-7]|one|two|three|four|five|six|seven)'



block_start_dates_map = {
        1: {'start': datetime.date(2017, 8, 28), 'end': datetime.date(2017, 9, 20)},
        2: {'start': datetime.date(2017, 9, 25), 'end': datetime.date(2017, 10, 18)},
        3: {'start': datetime.date(2017, 10, 23), 'end': datetime.date(2017, 11, 15)},
        4: {'start': datetime.date(2017, 11, 27), 'end': datetime.date(2017, 12, 20)},
        5: {'start': datetime.date(2018, 1, 22), 'end': datetime.date(2017, 2, 14)},
        6: {'start': datetime.date(2018, 2, 19), 'end': datetime.date(2017, 3, 14)},
        7: {'start': datetime.date(2018, 3, 26), 'end': datetime.date(2017, 4, 18)},
        8: {'start': datetime.date(2018, 4, 23), 'end': datetime.date(2017, 5, 16)} }




def silly(match):
    if match:
        return int(match[0])
    else:
        return None

def meow(text):
    text = text.lower()

    B = re.search(r'(?<=block )[1-8]', text)

    W = re.search(r'(?<=week )[1-4]', text)

    D = re.search(r'(?<=day )[1-7]', text)

    return block_date_to_real_time_date( silly(B), silly(W), silly(D) )


def get_current_block():
        today = datetime.date.today()
        end_dates = [ block_start_dates_map[b]['end'] for b in range(1,9) ]

        block_counter = 0
        for date in end_dates:
            if today > date:
              block_counter += 1

        return block_counter


def block_date_to_real_time_date(B, W, D):

    if B and W and D:
        return get_date( B, W, D)

    elif B and W:
        return get_range_of_week( B, W )

    elif W and D:
        return get_date( get_current_block(), W, D )

    elif B and D:
        return 'invalid input'

    elif B:
        return get_range_of_block( B )

    elif W:
        return get_range_of_week( get_current_block(), W )

    elif D:
        return 'invalid input'

    else:
        return 'invalid input'


def get_range_of_block(B):
    return ( block_start_dates_map[B]['start'], block_start_dates_map[B]['end'] )

def get_range_of_week(B, W):
    return ( block_start_dates_map[B]['start'] + datetime.timedelta(7 * (W - 1) + 1 ), block_start_dates_map[B]['start'] + datetime.timedelta(7 * (W - 1) + 7 ) )

def get_date(B, W, D):
    return ( block_start_dates_map[B]['start'] + datetime.timedelta(7 * (W - 1) + D) )



if __name__ == '__main__':
    file = open("converted_date.txt", 'w')

    s = sys.argv[1]
    if s == "test":
        file.write("the test works")
        file.close()
    else:
        out = str(meow(s))
        print(out)
        file.write(out)
        file.close()

    os.system("open converted_date.txt")
