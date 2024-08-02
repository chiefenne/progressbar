# progressbar.py
import sys
import time

class ProgressBar:
    """
    GUI-less ProgressBar
    """
    def __init__(self, final_count, block_char='.'):
        self.final_count = final_count
        self.block_count = 0
        self.block_char = block_char
        self.output = sys.stdout

        if not self.final_count:
            return
        
        self.output.write('\n                   % Progress                     \n')
        self.output.write('   10   20   30   40   50   60   70   80   90  100\n')

    def progress(self, count):
        count = min(count, self.final_count)
        if self.final_count:
            percent_complete = int(round(100.0 * count / self.final_count))
            percent_complete = max(percent_complete, 1)
        else:
            percent_complete = 100
        
        block_count = percent_complete // 2
        if block_count <= self.block_count:
            return
        
        for _ in range(self.block_count, block_count):
            self.output.write(self.block_char)
        
        self.output.flush()
        self.block_count = block_count

        if percent_complete == 100:
            self.output.write("\n")

if __name__ == "__main__":
    total = 100
    pb = ProgressBar(total)
    for i in range(total + 1):
        pb.progress(i)
        time.sleep(0.1)
