def longestConsecutive(list, k):
    if len(list) == 0 | k > len(list) | k < 0:
        return ""
    else:
        longestString = ""
        # string = ""
        for i in range(len(list)):
            string = ""
            if i + (k-1) < len(list):
                for j in range(k):
                    string += list[j + i]
                if len(string) > len(longestString):
                    longestString = string
        return longestString


a = longestConsecutive(["vengo", "ozzy", "absolutely", "little", "shark", "boo"], 2);
print(a)

s = longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3);
print(s)
