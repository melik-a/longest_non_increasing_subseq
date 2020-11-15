"""to do: 
        1) provide finding all longest subsequences, not only first
        2) cover with tests
        3) add n * logarithmic algorithms for all subtasks
"""

#task 
def longest_continuous_non_incr_subseq(sequence):
    max_subseq_len = 1
    curr_subseq_len = 1
    subseq_end_ind = -1
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            curr_subseq_len += 1
            if curr_subseq_len > max_subseq_len:
                max_subseq_len = curr_subseq_len
                #if next el in seq more than current then save next el index as last
                subseq_end_ind = i + 1
        else:
            curr_subseq_len = 1
    
    """ if subseq_end_ind > 0:
        print("sub_seq_int",subseq_end_ind)
        print(sequence[subseq_end_ind - max_subseq_len + 1  :  subseq_end_ind + 1]) """
    
    return sequence[subseq_end_ind - max_subseq_len + 1  :  subseq_end_ind + 1]


def longest_continuous_incr_subseq(sequence):
    max_subseq_len = 1
    curr_subseq_len = 1
    subseq_end_ind = -1
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            curr_subseq_len += 1
            if curr_subseq_len > max_subseq_len:
                max_subseq_len = curr_subseq_len
                #if next el in seq more than current then save next el index as last
                subseq_end_ind = i + 1
        else:
            curr_subseq_len = 1
    
    """ if subseq_end_ind > 0:
        print("sub_seq_int",subseq_end_ind)
        print(sequence[subseq_end_ind - max_subseq_len + 1  :  subseq_end_ind + 1]) """
    
    return sequence[subseq_end_ind - max_subseq_len + 1  :  subseq_end_ind + 1]

#classic explanation of longest non incr subseq - n^2
def len_longest_non_incr_subseq_n2(sequence):
    #length of the longest non increasing subsequence ending in the element with index i.
    sub_len = [1] * len(sequence)
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] >= sequence[j]) and (sub_len[j] <= sub_len[i]):
                sub_len[j] = sub_len[i] + 1
    return max(sub_len)


#classic explanation of longest incr subseq - n^2
def len_longest_incr_subseq_n2(sequence):
    #length of the longest increasing subsequence ending in the element with index i.
    sub_len = [1] * len(sequence)
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] < sequence[j]) and (sub_len[j] <= sub_len[i]):
                sub_len[j] = sub_len[i] + 1
    return max(sub_len)


def longest_non_incr_subseq_n2(sequence):
    """
        comment this solution
    """
    sequence_len = len(sequence)
    max_subseq_len = 0
    pos  = 0 
    #length of the longest non increasing subsequence ending in the element with index i.
    sub_len = [1] * sequence_len
    traces = [-1] * sequence_len

    for i in range(sequence_len):
        for j in range(i):
            if (sequence[i] <= sequence[j]) and (sub_len[j] + 1 > sub_len[i]):
                sub_len[i] = sub_len[j] + 1
                traces[i] = j
        if sub_len[i] > max_subseq_len:
            max_subseq_len = sub_len[i]
            pos = i
    
    path = []
    while pos != -1:
        path.append(sequence[pos])
        pos = traces[pos]

    path.reverse()

    return path


def longest_incr_subseq_n2(sequence):
    """
        comment this solution
    """
    sequence_len = len(sequence)
    max_subseq_len = 0
    pos = 0 
    #length of the longest non increasing subsequence ending in the element with index i.
    sub_len = [1] * sequence_len
    trace = [-1] * sequence_len
    
    for i in range(sequence_len):
        for j in range(i):
            if (sequence[i] > sequence[j]) and (sub_len[j] + 1 > sub_len[i]):
                sub_len[i] = sub_len[j] + 1
                trace[i] = j
        if sub_len[i] > max_subseq_len:
            max_subseq_len = sub_len[i]
            pos = i
    
    path = []
    while pos != -1:
        path.append(sequence[pos])
        pos = trace[pos]
    path.reverse()

    return path


def binary_search(path_arr, searched_x):
    left = 0
    right = len(path_arr)
    while left < right:
        mid = (left + right) // 2
        if path_arr[mid] <= searched_x:
            left = mid + 1
        else:
            right = mid
            
    return left


def longest_non_incr_subseq_nlogn(sequence):
    """
        comment this solution
    """
    #sequence.reverse()
    sequence_len = len(sequence)
    #smollest last element of subsequence with lenght i.
    traces = [-1]
    end_of_subseq = []
    for i in range(sequence_len - 1, -1, -1):
        if len(end_of_subseq) != 0:
            j = binary_search([sequence[k] for k in end_of_subseq], sequence[i])
            if j < len(end_of_subseq):
                end_of_subseq[j] = i
            else:
                end_of_subseq.append(i)
            
            traces.append(end_of_subseq[j-1] if j > 0 else -1)
        else:
            end_of_subseq.append(i)
    
    
    traces.reverse()
    subseq = []
    el = end_of_subseq[-1]
    while el != -1:
        subseq.append(sequence[el])
        el = traces[el]

    return subseq


def longest_non_decr_subseq_nlogn(sequence):
    """ 
        comment this solution 
    """
    sequence_len = len(sequence)
    #smollest last element of subsequence with lenght i.
    end_of_subseq = []
    traces = [-1]
    for i in range(sequence_len):
        if len(end_of_subseq) != 0:
            j = binary_search([sequence[k] for k in end_of_subseq], sequence[i])
            if j < len(end_of_subseq):
                end_of_subseq[j] = i
            else:
                end_of_subseq.append(i)
            
            traces.append(end_of_subseq[j-1] if j > 0 else -1)
        else:
            end_of_subseq.append(i)
    
    #traces.reverse()
    subseq = []
    el = end_of_subseq[-1]
    while el != -1:
        subseq.append(sequence[el])
        el = traces[el]

    return subseq[::-1]


def test_longest_continuous_non_incr_subseq(test_l):
    A = [11, 9, 0]
    B = [8, 4]
    C = [11, 9, 7]
    D = [0, 0, 0, 0, 0, 0]
    E = [17, 15, 9, 7]
    answers = [A, B, C, D, E]
    test_answ = zip(test_l, answers)
    for test, answ in test_answ :
        current_answ = longest_continuous_non_incr_subseq(test)
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
    



def main():
    A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11]
    B = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    C = [7, 11, 9, 7, 11, 15, 5, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11, 0]
    D = [0, 0, 0, 0, 0, 0]
    E = [11, 17, 15, 9, 7, 19, 14, 10, 19, 20, 21, 0]
    test_set = [A, B, C, D, E]
    for i in test_set:
        print (f"test_seq = {i}\n")
        print(f"-------------------------------------------------------------------")
        
        print(f"len_longest_non_incr_subseq_n2 = {len_longest_non_incr_subseq_n2(i)}\n")
        
        print(f"longest_continuous_non_incr_subseq = {longest_continuous_non_incr_subseq(i)}\n")
        print(f"longest_non_incr_subseq_n2 = {longest_non_incr_subseq_n2(i)}\n")
        print(f"longest_non_incr_subseq_nlogn = {longest_non_incr_subseq_nlogn(i)}\n")
        
        print(f"-------------------------------------------------------------------\n")
        
        print(f"len_longest_incr_subseq_n2 = {len_longest_incr_subseq_n2(i)}\n")

        print(f"longest_continuous_incr_subseq = {longest_continuous_incr_subseq(i)}\n")
        print(f"longest_incr_subseq_n2 = {longest_incr_subseq_n2(i)}\n")
        print(f"longest_non_decr_subseq_nlogn = {longest_non_decr_subseq_nlogn(i)}\n")

        print(f"###################################################################")
        print(f"###################################################################")
        print(f"###################################################################\n")
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"D = {D}")
    print(f"E = {E}\n")
    tests()


if __name__ == "__main__":
    main()

