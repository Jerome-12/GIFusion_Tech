class Solution:

    def reverse(self, x: int) -> int:

      if x.bit_length() > 31:

        return 0

      else:      

        value = -1 if x < 0 else 1 # if x is negative then x is multipled by -1, otherwise it remains same

        x *= value

        rev_num = 0


        while x:

            rev_num = rev_num * 10 + x % 10 

            x //= 10 

               

        return value * rev_num   

