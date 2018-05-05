

class BlockDate(object):


# block_start_dates_map["block_1"]["end_date"]
    block_start_dates_map = {
            "block_1": {"start_date": Date(2017, 8, 27), "end_date": Date(2017, 9, 20}
            "block_2": {"start_date": Date(2017, 9, 25), "end_date": Date(2017, 10, 18}
            "block_3": {"start_date": Date(2017, 10, 23), "end_date": Date(2017, 11, 15}
            "block_4": {"start_date": Date(2017, 11, 27), "end_date": Date(2017, 12, 20}
            "block_5": {"start_date": Date(2018, 1, 22), "end_date": Date(2017, 2, 14}
            "block_6": {"start_date": Date(2018, 2, 19), "end_date": Date(2017, 3, 14}
            "block_7": {"start_date": Date(2018, 3, 26), "end_date": Date(2017, 4, 18}
            "block_8": {"start_date": Date(2018, 4, 23), "end_date": Date(2017, 5, 16}
    }


    def __init__(self, block=None, week=None, day=None):
        if day:
            self.get_date()
        else:
            self.get_range()


        self.block = block
        self.week = week
        self.day = day

    def get_current_block(self):
        today = date.now

    def get_range(self):
        if self.block and self.week:
            return( block_start_dates_map[block] + datetime.timedelta(7 * (week - 1)), block_start_dates_map[block] + datetime.timedelta(7 * (week - 1) + 6 ) )

        elif self.block:
            return( block_start_dates_map[block], block_start_dates_map[block] + datetime.timedelta(22) )

        elif self.week:
            return( )


        block_date = block_date.lower()
        block_number = re.search(r'.*(?=block)', block_date)
        week_number = re.search(r'.*(?=block)', block_date)
        day_number = re.search(r'.*(?=block)', block_date)
        block = BlockDate(block_number)
        return block_date


    def get_date(self):
