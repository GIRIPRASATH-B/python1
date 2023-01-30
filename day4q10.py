 if len(s1) != len(s2):
        return False
    
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        count[ch] = count.get(ch, 0) - 1
    total = sum(count.values())
    
    if (total != 0):
        return False
    
    return self.go(s1, s2)

@lru_cache(maxsize=None)
def go(self, s1, s2):
    n = len(s1)
    
    if (s1 == s2):
        return True
    
    for i in range(1, n):
        a = self.go(s1[i:], s2[i:]) and self.go(s1[:i], s2[:i])
        b = self.go(s1[i:], s2[:n-i]) and self.go(s1[:i], s2[n-i:])
        
        if (a or b):
            return True
    return False
