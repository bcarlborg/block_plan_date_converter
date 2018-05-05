

class BlockDate(object):

    dict = {
            1:Date(2017, 8, 27),
            2:Date(2017, 9, 25),
            3:Date(2017, 10, 23),
            4:Date(2017, 11, 27),
            5:Date(2018, 1, 22),
            6:Date(2018, 2, 19),
            7:Date(2018, 3, 26),
            8:Date(2018, 4, 23)
    }


    def __init__(self, block=None, week=None, day=None):
        if day:
            self.get_date()
        else:
            self.get_range()


        self.block = block
        self.week = week
        self.day = day

    def get_range(self):
        if block and week:

        elif block:

        elif week:


        block_date = block_date.lower()
        block_number = re.search(r'.*(?=block)', block_date)
        week_number = re.search(r'.*(?=block)', block_date)
        day_number = re.search(r'.*(?=block)', block_date)
        block = BlockDate(block_number)
        return block_date


    def get_date(self):
