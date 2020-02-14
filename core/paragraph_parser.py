import pandas as pd


class Book:
    def __init__(self, filepath, separator='\n', min_paragraph_length=50):
        self.min_paragraph_length = min_paragraph_length
        # Ensure that we get a line-reading sequence in the best way possible:
        try:
            # Check if the file-like object has an xreadlines method
            self.seq = open(filepath, encoding='utf8').readlines()
        except AttributeError:
            # No, so fall back to the xreadlines module's implementation
            raise IOError("File reading error occurred")

        self.line_num = 0  # current index into self.seq (line number)
        self.para_num = 0  # current index into self (paragraph number)

        # Ensure that separator string includes a line-end character at the end
        if separator[-1:] != '\n':
            separator += '\n'
        self.separator = separator

    def __getitem__(self, index):
        if index != self.para_num:
            raise TypeError("Only sequential access supported")
        self.para_num += 1
        # Start where we left off and skip 0+ separator lines
        while 1:
            # Propagate IndexError, if any, since we're finished if it occurs
            line = self.seq[self.line_num]
            self.line_num += 1
            if line != self.separator: break
        # Accumulate 1+ nonempty lines into result
        result = [line.replace('\n', ' ')]
        while 1:
            # Intercept IndexError, since we have one last paragraph to return
            try:
                # Let's check if there's at least one more line in self.seq
                line = self.seq[self.line_num]
            except IndexError:
                # self.seq is finished, so we exit the loop
                break
            # Increment index into self.seq for next time
            self.line_num += 1
            if line == self.separator:
                break
            result.append(line.replace('\n', ' '))
        return ''.join(result).replace('  ', ' ')

    def get_dataframe(self):
        paras = []
        for p in self:
            # filter small paragraphs
            if len(p) < self.min_paragraph_length:
                continue
            paras.append(p)
        return pd.DataFrame({'body': paras})
