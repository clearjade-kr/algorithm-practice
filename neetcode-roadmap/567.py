class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        dict_cnt_s1 = defaultdict(int)
        for ch in s1:
            dict_cnt_s1[ch] += 1

        cur_cnt = 0
        start, end = 0, 0
        dict_cnt_s2 = defaultdict(int)
        while end < len(s2):
            # current char not in s1
            if s2[end] not in dict_cnt_s1:
                end += 1
                start = end
                dict_cnt_s2.clear()
                continue

            # increase current s2 count
            dict_cnt_s2[s2[end]] += 1

            # if current char count is more than s1
            # slide start while previous char (same as curr) shows
            while dict_cnt_s1[s2[end]] < dict_cnt_s2[s2[end]]:
                dict_cnt_s2[s2[start]] -= 1
                start += 1

            if end - start + 1 == len(s1):
                return True
        
            end += 1

        return False


if __name__ == "__main__":
    sol = Solution()
    # s1 = "ab"
    # s2 = "eidbaooo"
    s1 = "adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1=s1, s2=s2))
