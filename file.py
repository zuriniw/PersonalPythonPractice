"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if line1 == line2:
        return IDENTICAL
    
    min_len = min(len(line1), len(line2))
    for index in range(min_len):
        if line1[index] != line2[index]:
            return index
        
    if len(line1) != len(line2):
        return min_len

    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    minlen = min(len(line1), len(line2))
    
    if ("\n " in (line1 + line2) or "\r" in (line1 + line2)) or ((idx < 0) or (idx > minlen)) :
        return ""
    else:
        prompt = "=" * idx + "^"
        return (line1 + "\n" + prompt + "\n" + line2 + "\n")

    

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    min_len = min(len(lines1), len(lines2))

    for item in range(min_len):
        diff_index = singleline_diff(lines1[item], lines2[item])
        if diff_index != IDENTICAL:
            return (item, diff_index)

    if len(lines1) != len(lines2):
        return (min_len, 0)

    return (IDENTICAL, IDENTICAL)



def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines = []
    
    with open(filename, 'r', encoding = "UTF-8") as file:
        for line in file:
            # remove enters
            stripped_line = line.rstrip('\n\r')
            lines.append(stripped_line)
            
    return lines



def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    # read files into lists
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)

    # find difference
    line_num, diff_index = multiline_diff(lines1, lines2)

    # same file
    if line_num == IDENTICAL:
        return "No differences\n"

    # formatting
    line1 = lines1[line_num] if line_num < len(lines1) else ""
    line2 = lines2[line_num] if line_num < len(lines2) else ""
    diff = singleline_diff_format(line1, line2, diff_index)

    return f"Line {line_num}:\n{diff}"

