file = open("input.txt")
lines = file.readlines()
t = "├──"
l = "└──"
v = "│"

open('output.txt', 'w').close()
open('output_final.txt', 'w').close()
out_file = open('output.txt', 'a')
last_dir_level = 0
sof = 1

for line in reversed(lines):
    dir_level = int(((len(line) - len(line.lstrip()))/2))
    if sof == 0:
        if dir_level == 0:
            out_line = t + line.lstrip()
            out_file.write(out_line)
        else:
            if last_dir_level == dir_level:
                out_line = v + "   "*(dir_level) + t + line.lstrip()
            elif last_dir_level != dir_level:
                out_line = v + "   "*(dir_level) + l + line.lstrip()
            out_file.write(out_line)
        print('line: {}; dir: {}; last_dir: {}'.format(out_line, dir_level, last_dir_level))
        last_dir_level = dir_level
    if sof == 1:
        out_line = " "*(dir_level*3) + l + line.lstrip()
        print('line: {}; dir: {}; last_dir: {}'.format(out_line, dir_level, last_dir_level))
        sof = 0
        last_dir_level = dir_level
        out_file.write(out_line)
        out_file.write("\n")
        
        
out_file.close()

# Reverse lines in output file
ofile = open("output.txt")
output_file = ofile.readlines()
ofile_final = open("output_final.txt", "a")
for line in reversed(output_file):
    ofile_final.write(line)
ofile.close()
ofile_final.close()

