chcp 65001
del /s /q personal_info
del /s /q merged_personal_info*

python "개인정보 무작위생성.py"
python "개인정보 하나로 합치기.py"
python "셀개인정보 엑셀파일로 만들기.py"
