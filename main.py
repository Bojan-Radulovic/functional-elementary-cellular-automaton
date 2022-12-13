def length(li):

    def length_iter(inner_li, n):
        if not inner_li:
            return n
        return length_iter(inner_li[1:], n + 1)

    return length_iter(li, 0)


def reversed_str(string):

    def reversed_str_iter(inner_str, rev_str):
        if inner_str == '':
            return rev_str
        return reversed_str_iter(inner_str[:-1], rev_str + inner_str[-1])

    return reversed_str_iter(string, '')


def list_to_string(li):

    def list_to_string_iter(inner_li, new_string):
        if not inner_li:
            return new_string
        return list_to_string_iter(inner_li[1:], new_string + str(inner_li[0]))

    return list_to_string_iter(li, "")


def bits_to_int(li):
    return int(list_to_string(li), 2)


def int_to_bits(n):
    return '{0:08b}'.format(n)


def ceiling(n):
    return int(-1 * n // 1 * -1)


def elementary_cellular_automaton(rule, width=33, height=16, first_row=None):

    def rule_check(bit_li, inner_rule):
        return list(reversed_str(inner_rule))[bits_to_int(bit_li)]

    def generate_first_row(w):
        return [0] * int(w / 2) + [1] + [0] * int(w / 2 - 1 + ceiling(w % 2))

    def generate_row(old_row, inner_rule):

        def generate_row_iter(inner_old_row, new_row, iter_rule):
            if length(inner_old_row) <= 2:
                return new_row
            return generate_row_iter(
                inner_old_row[1:],
                new_row + [rule_check([inner_old_row[0], inner_old_row[1], inner_old_row[2]], iter_rule)],
                iter_rule
            )

        return [old_row[0]] + generate_row_iter(old_row, [], inner_rule) + [old_row[-1]]

    def elementary_cellular_automaton_iter(h, inner_rule, matrix):
        if h <= 0:
            return matrix
        return elementary_cellular_automaton_iter(
            h - 1,
            inner_rule,
            matrix + [generate_row(matrix[-1], inner_rule)]
        )

    if not 0 <= rule <= 255:
        return "Rule number must be between 0 and 255"

    if width < 3:
        return "Minimum width is 3"

    if height < 1:
        return "Minimum height is 1"

    if first_row:
        return elementary_cellular_automaton_iter(
            height - 1,
            int_to_bits(rule),
            [first_row]
        )
    return elementary_cellular_automaton_iter(
        height - 1,
        int_to_bits(rule),
        [generate_first_row(width)]
    )


def matrix_to_string(matrix):

    def matrix_to_string_iter(inner_matrix, new_string):
        if not inner_matrix:
            return new_string[:-1]
        return matrix_to_string_iter(inner_matrix[1:], new_string + list_to_string(inner_matrix[0]) + '\n')

    return matrix_to_string_iter(matrix, "")


def pretty_string(old_string):
    return old_string.replace("0", " ").replace("1", "■")


print(pretty_string(matrix_to_string(elementary_cellular_automaton(150))))
