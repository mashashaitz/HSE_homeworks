#��������� ������ ���������� � ������������ ����� �� ��� ���, ���� �� �� ����� ������ �����. ����� ����� ��������� ������ ������� �� ����� �� �� �������� ����, ����� ������� ������ 5 �������� (������ ����� �� ��������� �������).
words = []
while 4 < 5:
    smth = input('put a word here, to stop putting words press enter ')
    
    if smth == "":
        break
    elif len(smth) > 5:
        words.append(smth)

for digit in range(len(words)):
    print(words[digit])
        