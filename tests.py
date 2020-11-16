from monot_subsequences import *

def test_longest_continuous_non_incr_subseq(test_l):
    A = [11, 9, 0]
    B = [8, 4]
    C = [11, 9, 7]
    D = [0, 0, 0, 0, 0, 0]
    E = [17, 15, 9, 7]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = longest_continuous_non_incr_subseq(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_longest_continuous_incr_subseq(test_l):
    A = [1, 5, 12, 14]
    B = [0, 8]
    C = [1, 5, 12, 14]
    D = []
    E = [10, 19, 20, 21]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = longest_continuous_incr_subseq(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_len_longest_non_incr_subseq_n2(test_l):
    A = 5
    B = 5
    C = 8
    D = 6
    E = 5
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = len_longest_non_incr_subseq_n2(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_len_longest_incr_subseq_n2(test_l):
    A = 5
    B = 6
    C = 5
    D = 1
    E = 5
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = len_longest_incr_subseq_n2(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_longest_decr_subseq_n2(test_l):
    A = [11, 9, 2, 1, 0]
    B = [12, 10, 6, 5, 3]
    C = [11, 9, 7, 5, 2, 1, 0]
    D = [0]
    E = [17, 15, 9, 7, 0]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = longest_decr_subseq_n2(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_longest_incr_subseq_n2(test_l):
    A = [7, 9, 11, 15, 18]
    B = [0, 4, 6, 9, 13, 15]
    C = [7, 9, 11, 15, 18]
    D = [0]
    E = [11, 17, 19, 20, 21]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = longest_incr_subseq_n2(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_longest_non_incr_subseq_nlogn(test_l):
    A = [11, 9, 0, 0, 0]
    B = [12, 10, 6, 5, 3]
    C = [11, 9, 7, 5, 2, 1, 0, 0]
    D = [0, 0, 0, 0, 0, 0]
    E = [17, 15, 9, 7, 0]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = longest_non_incr_subseq_nlogn(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def test_longest_non_decr_subseq_nlogn(test_l):
    A = [0, 0, 1, 5, 10, 11]
    B = [0, 2, 6, 9, 11, 15]
    C = [7, 7, 11, 12, 14]
    D = [0, 0, 0, 0, 0, 0]
    E = [11, 15, 19, 19, 20, 21]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ:
        current_answ = longest_non_decr_subseq_nlogn(test)
        assert  current_answ == answ, f"incorrect answer on {test}\nexpected:{answ}, but given {current_answ}"


def tests():
    """ testing all task functions:
            1) max_non_incr_sub_seq()
            2) len_longest_non_incr_subseq_n2()
            3) len_longest_incrt_subseq_n2()
            4) longest_non_incr_subseq_n2()
            5) longest_incr_subseq_n2()
            6) longest_non_incr_subseq_nlogn()
            7) longest_incr_subseq_nlogn()
            8) ...
    """

    A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11]
    B = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    C = [7, 11, 9, 7, 11, 15, 5, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11, 0]
    D = [0, 0, 0, 0, 0, 0]
    E = [11, 17, 15, 9, 7, 19, 14, 10, 19, 20, 21, 0]
    
    print("testing sets:")
    print(f"\t\tA = {A}")
    print(f"\t\tB = {B}")
    print(f"\t\tC = {C}")
    print(f"\t\tD = {D}")
    print(f"\t\tE = {E}\n")

    test_list = [A, B, C, D, E]

    test_longest_continuous_non_incr_subseq(test_list)
    test_longest_continuous_incr_subseq(test_list)
    
    test_len_longest_non_incr_subseq_n2(test_list)
    test_len_longest_incr_subseq_n2(test_list)
    
    test_longest_decr_subseq_n2(test_list)
    test_longest_incr_subseq_n2(test_list)

    test_longest_non_incr_subseq_nlogn(test_list)
    test_longest_non_decr_subseq_nlogn(test_list)


if __name__ == "__main__":
    tests()

