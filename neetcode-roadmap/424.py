class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        start, end = 0, 0
        # approach - s[start:end]
        # (end - start) - (current most frequent char count)
        # if k is bigger - more character can be consumed - end + 1
        # Else - start + 1 while current substring can consume more
                    
        # dict{char: cnt}
        dict_cnt = defaultdict(int)
        max_freq = 0
        ret_val = 0

        while end < len(s):
            dict_cnt[s[end]] += 1
            max_freq = max(max_freq, dict_cnt[s[end]])

            # We only need to check the max_freq change
            # since we need is the longest substring
            if (end - start + 1) - max_freq > k:
                dict_cnt[s[start]] -= 1
                start += 1
            
            ret_val = max(ret_val, end - start + 1)
            end += 1

        return ret_val


if __name__ == "__main__":
    sol = Solution()
    s = "AABBA"
    k = 1
    print(sol.characterReplacement(s=s, k=k))
