import numpy as np
    
# Find no. of leading spaces in each line
with open("sample_input.txt","r") as fp: 
    lspaces=[]
    for line in fp:
        lspaces.append(len(line)-len(line.lstrip()))
    
# Associate spaces with an index no. for indentation
space_map={}
lspaces_unique=(list(np.unique(np.array(lspaces))))
for count,element in enumerate(lspaces_unique):
    space_map[element]=count
    
# Find the symbols corresponding to each line by reverse parsing through the lines
row_entry=["   "]*len(lspaces_unique)
symbol_entries=[]
for element in reversed(lspaces):
    if(row_entry[space_map[element]]=="   "):
        row_entry[space_map[element]]="└──"
    else:
        row_entry[space_map[element]]="├──"
    count_2=0
    for element_2 in row_entry[:space_map[element]]:
        if(row_entry[count_2]=="└──" or row_entry[count_2]=="├──"):
            row_entry[count_2]="│  "
        count_2=count_2+1
    row_entry[space_map[element]+1:] = ['   ']*len(row_entry[space_map[element]+1:])
    symbol_entries.append(list(row_entry))
symbol_entries.reverse()    

# Display the output    
with open("sample_input.txt","r") as fp: 
    for count, line in enumerate(fp):
        out_string=""
        for element in symbol_entries[count][:space_map[lspaces[count]]+1]:
            out_string+=(element)
        out_string+=(line.strip())
        print(out_string)
