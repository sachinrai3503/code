# https://leetcode.com/problems/encode-and-decode-tinyurl
"""
TinyURL is a URL shortening service where you enter a URL such as 
 https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
 http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need
 to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to
 the original URL.

Implement the Solution class:
Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.
 
Constraints:
1 <= url.length <= 104
url is guranteed to be a valid URL.
"""

class RangeService:
    
    def __init__(self):
        self.length = 5
        self.s = ['a','a','a','a','a']
        self.e = ['a','a','a','a','z']
        self.exhausted = False
    
    def get_next_range(self):
        if self.exhausted: return None
        next_range = [list(self.s), list(self.e)]
        self.increment_range()
        return next_range
        
    def increment_range(self):
        i = self.length-1
        while i>=0 and self.e[i]=='z':
            self.s[i] = 'a'
            self.e[i] = 'a'
            i-=1
        if i==-1:
            self.exhausted = True
        else:
            self.s[i] = self.e[i] = chr(ord(self.e[i]) + 1)
            self.e[-1] = 'z'

class Codec:

    def __init__(self):
        self.range_svc = RangeService()
        self.cur_range = self.range_svc.get_next_range()
        self.cur_code = self.cur_range[0]
        self.map = dict() # code->URL

    def set_next_code(self):
        if self.cur_code==self.cur_range[1]:
            self.cur_range = self.range_svc.get_next_range()
            self.cur_code = self.cur_range[0]
        else:
            self.cur_code[-1] = chr(ord(self.cur_code[-1]) + 1)
        
    def get_code(self):
        code = ''.join(self.cur_code)
        self.set_next_code()
        return code
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = self.get_code()
        self.map[code] = longUrl
        # print(self.map)
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map.get(shortUrl, None)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))