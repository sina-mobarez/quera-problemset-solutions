row_no, sit_no = input(" : ").split()


def find_direction(sit_no):
    if sit_no > 10:
        return "Left"
    else:
        return "Right"


def find_rows(row_no):
    steps = 0
    for i in range(10, 0, -1):
        steps += 1
        if i == row_no:
            return steps


def find_sits(sit_no):
    dir = find_direction(sit_no)
    steps = 0
    if dir == "Right":
        return sit_no
    else:
        for i in range(20, 10, -1):
            steps += 1
            if i == sit_no:
                return steps


def main(row_no, sit_no):
    print(
        find_direction(sit_no=sit_no),
        find_rows(row_no=row_no),
        find_sits(sit_no=sit_no),
    )


if __name__ == "__main__":
    main(int(row_no), int(sit_no))
