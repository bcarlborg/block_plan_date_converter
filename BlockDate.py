

class BlockDate(object):

    block_start_dates_map = {
            1:Date(2017, 8, 27),
            2:Date(2017, 9, 25),
            3:Date(2017, 10, 23),
            4:Date(2017, 11, 27),
            5:Date(2018, 1, 22),
            6:Date(2018, 2, 19),
            7:Date(2018, 3, 26),
            8:Date(2018, 4, 23)
    }

    # B W D
    # B W
    # B
    # W D
    # W
    def __init__(self, B = None, W = None, D = None):

        if B and W and D:
            self.get_date(block=B, week=W, day=D)
        elif B and W:
            self.get_range(block=B, week=W)
        elif W and D:
            self.get_date(block=get_current_block(), week=W, day=D)
        elif B and D:
            pass
        elif B:
            self.get_range(block=B)
        elif W:
            self.get_range(block=get_current_block(), week=W)
        elif D:
            pass
        else:
            pass


        self.block = block
        self.week = week
        self.day = day

    def get_range(block, week):
        if block and week:
            return( block_start_dates_map[block] + datetime.timedelta(7 * (week - 1)), block_start_dates_map[block] + datetime.timedelta(7 * (week - 1) + 6 ) )

        elif block:
            return( block_start_dates_map[block], block_start_dates_map[block] + datetime.timedelta(22) )

        elif week:


        block_date = block_date.lower()
        block_number = re.search(r'.*(?=block)', block_date)
        week_number = re.search(r'.*(?=block)', block_date)
        day_number = re.search(r'.*(?=block)', block_date)
        block = BlockDate(block_number)
        return block_date


    def get_date(block, week, day):
