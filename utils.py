class utils:
    def printh(self,msg = ""):
        print("".center(120, "="))
        print(f" {msg} ".center(120, "="))
        print("".center(120, "="))
        
    def printc(self,msg = ""):
        print(f" {msg} ".center(120, "#"))
        
    def isHeading(self, str):
        if str[0] == '#':
            return True
    def findPos(self, str, char):
        # print(str, char)
        start = str.index("*")
        beg = str.index("*")
        while str[start] == char:
            start+=1
        
        str = str[start:]
        end = str.index("*")
        val = str.index("*")
        while str[val] == char:
            val+=1
        return start, start+end,beg,val