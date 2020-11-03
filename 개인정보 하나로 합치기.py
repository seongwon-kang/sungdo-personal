import os

directory = "personal_info/" #A라는 폴더 안에 B라는파일 A/B
outfile_name = "merged_personal_info.txt"

out_file = open(outfile_name, 'w', encoding="utf8")

files = os.listdir(directory) #directory라는 위치로 찾아가서 내용을 스캔하여 리턴한다.

for filename in files:
    if ".txt" not in filename:
        continue
    file = open(directory + filename, encoding="utf8")
    for line in file:
        out_file.write(line)
    out_file.write("\n\n")
    file.close()
out_file.close()