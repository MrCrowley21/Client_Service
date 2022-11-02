class RatingSystem:
    def __init__(self):
        self.marks = []

    def get_mark(self, preparing_time, max_wait):
        if preparing_time < max_wait:
            mark = 5
        elif preparing_time < 1.1 * max_wait:
            mark = 4
        elif preparing_time < 1.2 * max_wait:
            mark = 3
        elif preparing_time < 1.3 * max_wait:
            mark = 2
        elif preparing_time < 1.4 * max_wait:
            mark = 1
        else:
            mark = 0
        self.marks.append(mark)
        return mark
