#!/bin/env python
## This script was used to select protein gene models having >=50% similarity to the B. mori model.
id_dict = {
}

annotated_prot = open("/Users/lucasb/Documents/Diatraea_project/annotated_proteins.txt", "w")
filtered_prot = open("/Users/lucasb/Documents/Diatraea_project/filtered_proteins.txt", "w")

with open("/Users/lucasb/Documents/Diatraea_project/prot_filtered2.gff", "r") as f:
    lines = f.readline().split()
    while lines:
        info = lines[8]
        info = info.split(";")
        identity = info[4][17:]
        prot_id = info[1][9:-1]
##de onde vem esses NP_ ?
        if prot_id in id_dict.keys():
            if identity not in id_dict.values():
                id_dict[prot_id].append(identity)
        if prot_id not in id_dict.keys():
            if prot_id.startswith("NP_") == False:
                id_dict[prot_id] = [identity]
        lines = f.readline().split()

## write file containing all alignment scores:
annotated_prot.write("Protein_ID"+"\t"+"Identity"+"\n")
for key, value in id_dict.items():
    if len(value) > 1:
        annotated_prot.write(str(key)+"\t"+str(value[0]))
        for n in range(len(value)):
            if n == (len(value)-1):
                annotated_prot.write(", "+str(value[n]+"\n"))
            if 0 < n < (len(value)-1):
                annotated_prot.write(", "+str(value[n]))
    else:
        annotated_prot.write(str(key)+"\t"+str(value[0])+"\n")
annotated_prot.close()

# write file containing only >= 50% aligned identity:
filtered_prot.write("Protein_ID"+"\t"+"Identity"+"\n")
for key, value in id_dict.items():
    newlist = []
    if len(value) > 1:
        for elem in value:
            if float(elem) >= 50:
                newlist.append(elem)
    if newlist:
        filtered_prot.write(str(key)+'\t'+', '.join(newlist)+'\n')
    else:
        if float(value[0]) >= 50:
            filtered_prot.write(str(key)+'\t'+str(value[0])+'\n')
filtered_prot.close()