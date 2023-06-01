class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0

        while i < len(chars):
            count = 1
            while i + count < len(chars) and chars[i] == chars[i+count]:
                count += 1
            cnt_str = chars[i]
            if count > 1:
                cnt_str += str(count)
                chars[i:i+count] = list(cnt_str)
            i += len(cnt_str)
        
        return len(chars)

        # T: O(n)
        # S: O(1)
