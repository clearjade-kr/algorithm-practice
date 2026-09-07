class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        # If s1 is longer -> impossible, return False
        if n1 > n2:
            return False

        # list of char counts for s1, s2
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
            return True

        # Slide size fixed window across s2
        for end in range(n1, n2):
            s2_counts[ord(s2[end]) - ord('a')] += 1
            s2_counts[ord(s2[end - n1]) - ord('a')] -= 1

            if s1_counts == s2_counts:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    # s1 = "ab"
    # s2 = "eidbaooo"
    s1 = "adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1=s1, s2=s2))
