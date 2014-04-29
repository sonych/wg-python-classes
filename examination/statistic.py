# coding: utf-8


def statistic(file):

    average_line_length = 0

    for i, line in enumerate(file, 1):

        if line.strip():
            if i == 1:
                average_line_length = len(line)
            else:
                average_line_length = (average_line_length + len(line)) / 2.

            yield i, int(average_line_length), line
