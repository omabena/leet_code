"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """     
        if n == 0: return 0
    
        reads = (n-1)//4
        buf_read = list(buf)
        char_reads = 0
        while (reads >= 0):
            reads = reads - 1
            single_read_count = read4(buf_read)
            for i in range(single_read_count):
                if char_reads >= n: break
                buf[char_reads] = buf_read[i]
                char_reads = char_reads + 1
            
        return char_reads