#task 
def len_of_max_non_incr_sub_seq(sequence):
    max_sub_seq = 1
    curr_sub_seq = 1
    sub_seq = -1
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            curr_sub_seq += 1
            if curr_sub_seq > max_sub_seq:
                max_sub_seq = curr_sub_seq
                #if next el in seq more than current then save next el index as last
                sub_seq = i + 1
        else:
            curr_sub_seq = 1
    print(sub_seq, "sub_seq_int")
    print(sequence[sub_seq - max_sub_seq + 1  :  sub_seq + 1])
    return max_sub_seq


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


def len_longest_non_incr_subseq_log(sequence):
    pass


def longest_non_incr_subseq_n2(sequence):
    pass


def longest_incr_subseq_n2(sequence):
    pass




def main():
    A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11]
    B = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print("len_of_max_non_incr_sub_seq", len_of_max_non_incr_sub_seq(A))
    print("longest_non_incr_subseq_n2", len_longest_non_incr_subseq_n2(A))
    print("longest_incr_subseq_n2",len_longest_incr_subseq_n2(B))


if __name__ == "__main__":
    main()
