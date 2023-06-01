class Solution:
    def intToRoman(self, num: int) -> str:
        
        lookup = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        res = ''
        for count, rom in lookup.items():
            if num == 0:
                break
            q, num = num//count, num%count
            res += rom*q
        
        return res
        