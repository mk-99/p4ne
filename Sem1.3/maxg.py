import random

def max_asc_r(a):
    """
    Returns maximal ascending subsequence of sequence (recursive)
    :param a: sequence of ints as list
    :return: maximal ascending subsequence of a as list
    """
    if len(a) <= 1:
        return a
    b_left = max_asc_r(a[0:-1])
    b_right = max_asc_r(a[1:])



def max_asc(a):
    """
    Returns maximal ascending subsequence of sequence (non-recursive)
    :param a: sequence of ints as list
    :return: maximal ascending subsequence of a as list
    """
    sub_seq = []
    for i in range(0, len(a)):
        sub_seq.append([])

    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if len(sub_seq[i]) == 0 or a[j] > sub_seq[i][-1]:
                sub_seq[i].append(a[j])

    max_len = len(sub_seq[0])
    max_i = 0

    for i in range(0, len(a)):
        if len(sub_seq[i]) > max_len:
            max_len = len(sub_seq[i])
            max_i = i

    return sub_seq[max_i]


if __name__ == '__main__':
    source_sequence = []

    for i in range(0, 20):
        source_sequence.append(random.randint(0, 100))


    print(source_sequence)
    print(max_asc_r(source_sequence))
    print(max_asc(source_sequence))


