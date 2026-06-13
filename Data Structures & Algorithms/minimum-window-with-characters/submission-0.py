class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t) > len(s):
            return ""
        window, t_dict = {}, {}
        

        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1
        
        have, need = 0, len(t_dict)

        l = 0
        res, res_len = [-1,-1], float('infinity')

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in t_dict and window[s[r]] == t_dict[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = r-l+1
                window[s[l]] -= 1
                if s[l] in t_dict and t_dict[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if res_len != float('infinity') else ""


        




        