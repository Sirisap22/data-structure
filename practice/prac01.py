s = input('Enter Roman/Arabic Number: ')
class Translator:
    def __init__(self):
        self.numToRo =  { 
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I",
            0 : ""        
        }

        self.roToNum = { value: key for key, value in self.numToRo.items() }


    def romanToArabic(self, s):
        ans = 0
        if len(s) == 1:
            ans += self.roToNum[s]
        else:
            for  i in range(0, len(s)-1):
                ans += self.roToNum[s[i]] if self.roToNum[s[i]] >= self.roToNum[s[i+1]] else -self.roToNum[s[i]]
            ans += self.roToNum[s[-1]]
        return ans

    def arabicToRoman(self, s):
        ans = ''
        s = int(s)
        while s != 0:
            maxi = 0
            for num in self.numToRo.keys():
                if s - num >= 0 and num > maxi:
                    maxi = num
            s -= maxi
            ans += self.numToRo[maxi]
        return ans

t = Translator()
if s.isnumeric():
    ans = t.arabicToRoman(s)
else:
    ans = t.romanToArabic(s)

print(ans)
