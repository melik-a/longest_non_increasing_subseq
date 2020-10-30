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

def longest_non_incr_subseq():
    pass

def longest_incr_subseq():
    pass

if __name__ == "__main__":
    A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1 , 5, 12, 14, 0, 10, 11] 
    print("len of max non-increasing sub sequence", len_of_max_non_incr_sub_seq(A))

