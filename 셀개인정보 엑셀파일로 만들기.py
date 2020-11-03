import os

directory = "personal_info/"
outfile_name = "merged_personal_info.csv"

out_file = open(outfile_name,'w', encoding="utf8")

files = os.listdir(directory)

headers = []
outfile_has_header = False

for filename in files:
    if ".txt" not in filename:
        continue
    file = open (directory + filename, encoding="utf8")
    contents = []
    for line in file:
        if ":" in line:
            splits = line.split(":")
            contents.append(splits[-1].strip())
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    if not outfile_has_header:
        header = ", ".join(headers)
        out_file.write(header)
        outfile_has_header = True

    new_line = ", ".join(contents)
    out_file.write("\n" + new_line)

    file.close()
out_file.close()