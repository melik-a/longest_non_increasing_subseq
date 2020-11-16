""" to do: 
         1) add functionality to generate random sequences to find LNIS, LIS, LDS, LNDS
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


def longest_decr_subseq_n2(sequence):
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
            if (sequence[i] < sequence[j]) and (sub_len[j] + 1 > sub_len[i]):
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


def find(sequence = None):
    if sequence == None:
        A = [7, 11, 9, 0, 11, 15, 0, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11]
        B = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        C = [7, 11, 9, 7, 11, 15, 5, 18, 2, 14, 16, 1, 5, 12, 14, 0, 10, 11, 0]
        D = [0, 0, 0, 0, 0, 0]
        E = [11, 17, 15, 9, 7, 19, 14, 10, 19, 20, 21, 0]
        demo_set = [A, B, C, D, E]

        print(f"demo_sequences:")
        print(f"\t\tA = {A}")
        print(f"\t\tB = {B}")
        print(f"\t\tC = {C}")
        print(f"\t\tD = {D}")
        print(f"\t\tE = {E}")
    else:
        demo_set = []
        demo_set.append(sequence)

    for i in demo_set:
        print(f"\nseq = {i}\n")
        print(f"-------------------------------------------------------------------\n")
        
        print(f"len_longest_non_incr_subseq_n2 = {len_longest_non_incr_subseq_n2(i)}\n")
        
        print(f"longest_continuous_non_incr_subseq = {longest_continuous_non_incr_subseq(i)}\n")
        print(f"longest_decr_subseq_n2 = {longest_decr_subseq_n2(i)}\n")
        print(f"longest_non_incr_subseq_nlogn = {longest_non_incr_subseq_nlogn(i)}\n")
        
        print(f"-------------------------------------------------------------------\n")
        
        print(f"len_longest_incr_subseq_n2 = {len_longest_incr_subseq_n2(i)}\n")

        print(f"longest_continuous_incr_subseq = {longest_continuous_incr_subseq(i)}\n")
        print(f"longest_incr_subseq_n2 = {longest_incr_subseq_n2(i)}\n")
        print(f"longest_non_decr_subseq_nlogn = {longest_non_decr_subseq_nlogn(i)}\n")

        print(f"###################################################################")
        print(f"###################################################################")
        print(f"###################################################################\n")


def main():
    """ 
        comment
    """
    import random
    print("/////////////////////////////////////////////////////////////////")
    print("programm to find all subsequences (LNIS, LIS, LDS, LNDS) in a sequence(integer)")
    print("/////////////////////////////////////////////////////////////////")
    while True:
        print(f'''select the task:
                        1) enter a sequence.
                        2) generate a random sequence.
                        3) demonstration.
                        0) exit.''')
        
        try:
            choice = int(input("enter the task number: "))
        except:
            print("task number must be one of the available values. please try again.\n")
            continue
        
        if choice == 0:
            break
        elif choice == 3:
            find()
        elif choice == 1:
            while True:
                try:
                    size = int(input("enter the size of the sequence: "))
                    if size <= 0:
                        raise Exception
                except:
                    print("please enter the correct size number.\n")
                    continue
                break
            print("\nenter the sequence: ")
            seq = []
            for i in range(size):
                while True:
                    try: el = int(input(f"enter the {i} element = "))
                    except: print("element must be integer. please enter the correct element value\n")
                    seq.append(el)
                    print(f"current sequence = {seq}\n")
                    break
            print(f"your sequence = {seq}")
            find(seq)

        elif choice == 2:
            size = random.randrange(3, 50)
            seq = [random.randrange(0, 200) for i in range(size)]
            find(seq)

    print(f"bye, bye")


if __name__ == "__main__":
    main()

