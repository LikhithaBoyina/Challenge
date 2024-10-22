class Solution():
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2) # convert from binary to decimal
        b = int(b,2)
        # Add to decimal numbers
        c = a+b
        return bin(c)[2:]           # convert added number to binnary format   

# creating objject to the class Solution
Sol = Solution()
# Collect binary number input from the user
a = input("Enter any binary number : ")
b = input("Enter any binary number : ")
print(Sol.addBinary(a,b))
