from typing import List, Dict


def saddle_points(matrix: list[int]):

    saddle_pts_rtn: list[dict[str, int]] = []

    if len(matrix) > 0:
        if len(set([len(row) for row in matrix])) > 1:
            raise ValueError('The input Matrix has rows of differing lengths.')

        columns = list(zip(*matrix))

        for row_num, row in enumerate(matrix):
            for col_num, value in enumerate(row):
                if value == max(row) and value == min(columns[col_num]):
                    saddle_pts_rtn.append({"row": int(row_num + 1), "column": int(col_num + 1)})

    return saddle_pts_rtn
