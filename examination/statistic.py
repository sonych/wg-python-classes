# coding: utf-8


def statistic(file):

    average_line_length = 0

    for i, line in enumerate(file, 1):

        if line.strip():
            average_line_length += len(line)

            yield i, average_line_length/i, line
