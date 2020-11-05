#task 
def len_of_max_non_incr_sub_seq(sequence):
    max_sub_seq = 1
    curr_sub_seq = 1
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            curr_sub_seq += 1
            if curr_sub_seq > max_sub_seq:
                max_sub_seq = curr_sub_seq
        else:
            curr_sub_seq = 1
    return max_sub_seq


#classic explanation of longest non incr subseq
def longest_non_incr_subseq_n2(sequence):
    sub_len = [1] * len(sequence)
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] >= sequence[j]) and (sub_len[j] <= sub_len[i]):
                sub_len[j] = sub_len[i] + 1
    print(sub_len)
    return max(sub_len)


def longest_incr_subseq_n2(sequence):
    sub_len = [1] * len(sequence)
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] <= sequence[j]) and (sub_len[j] <= sub_len[i]):
                sub_len[j] = sub_len[i] + 1
    print(sub_len)
    return max(sub_len)


def main():
    A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11]
    B = [2, 5, 3, 7, 11, 8, 10, 13, 6]
    print("len_of_max_non_incr_sub_seq", len_of_max_non_incr_sub_seq(A))
    print("longest_non_incr_subseq_n2", longest_non_incr_subseq_n2(A))
    print("longest_incr_subseq_n2",longest_incr_subseq_n2(B))


if __name__ == "__main__":
    main()
