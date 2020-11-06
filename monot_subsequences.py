#task 
def max_non_incr_sub_seq(sequence):
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
    
    if subseq_end_ind > 0:
        print("sub_seq_int",subseq_end_ind)
        print(sequence[subseq_end_ind - max_subseq_len + 1  :  subseq_end_ind + 1])
    
    return max_subseq_len


#classic explanation of longest non incr subseq - n^2
def len_longest_non_incr_subseq_n2(sequence):
    #length of the longest non increasing subsequence ending in the element with index i.
    sub_len = [1] * len(sequence)
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] >= sequence[j]) and (sub_len[j] <= sub_len[i]):
                sub_len[j] = sub_len[i] + 1
    print(sub_len)
    return max(sub_len)


#classic explanation of longest incr subseq - n^2
def len_longest_incr_subseq_n2(sequence):
    #length of the longest increasing subsequence ending in the element with index i.
    sub_len = [1] * len(sequence)
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] <= sequence[j]) and (sub_len[j] <= sub_len[i]):
                sub_len[j] = sub_len[i] + 1
    print(sub_len)
    return max(sub_len)


def longest_non_incr_subseq_n2(sequence):
    #length of the longest non increasing subsequence ending in the element with index i.
    sequence_len = len(sequence)
    sub_len = [1] * sequence_len
    #sub_seq = [-1] * sequence_len
    max_subseq_len = 0
    for i in range(sequence_len - 1):
        for j in range(i + 1, sequence_len):
            if (sequence[i] >= sequence[j]) and (sub_len[j] <= sub_len[i] + 1):
                sub_len[j] = sub_len[i] + 1
                #sub_seq[i] = j
            if sub_len[j] > max_subseq_len:
                max_subseq_len = sub_len[j]
                pos = j
    
    path = []
    print(f"pos = {pos}")
    flag = True
    el = -1
    for i in range(pos):
        if (sequence[i] >= sequence[i + 1]) and el == -1:
            path.append(sequence[i])
            el = sequence[i + 1]
            flag = False
        elif el >= sequence[i + 1]:
            path.append(el)
            el = sequence[i + 1]
    path.append(sequence[pos]) 


    print(f"sub_seq = {path}")
    print("sub_len =", sub_len)
    return max(sub_len),path


def longest_incr_subseq_n2(sequence):
    pass


def len_longest_non_incr_subseq_log(sequence):
    pass


def main():
    A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11]
    B = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    C = [7, 11, 9, 7, 11, 15, 5, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11, 0]
    D = [0, 0, 0, 0, 0, 0]
    E = [11, 17, 15, 9, 7, 19, 14, 10, 19, 20, 21, 0]
    #print("len_of_max_non_incr_sub_seq", max_non_incr_sub_seq(A))
    print(f"longest_non_incr_subseq_n2 = {longest_non_incr_subseq_n2(E)}")
    #print("longest_incr_subseq_n2",len_longest_incr_subseq_n2(B))


if __name__ == "__main__":
    main()
