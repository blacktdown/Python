"""
날짜 : 2020/12/22
이름 : 박준우
내용 : 파이썬 파일 입출력 함수 실습하기
"""

# 파일읽기
from builtins import print

file1 = open('C:/Users/bigdata/Desktop/test.txt', 'r')
line = file1.readline()
print('line : ', line)

file1.close()

# 여러줄 파일 읽기
file2 = open('C:/Users/bigdata/Desktop/test.txt', 'r')

while True:
    line = file2.read()
    if not line:
        break

    print(line)
file2.close()

# 파일쓰기
file3 = open('C:/Users/bigdata/Desktop/test3.txt', 'w')
file3.write('안녕하세요.\n')
file3.write('반가워요.\n')
file3.write('잘있어요.\n')
file3.close()

# 구구단 파일 출력
file4 = open('C:/Users/bigdata/Desktop/test4.txt', 'w')

for a in range(2, 10):
    file4.write('%d단\n' % a)
    for b in range(1, 10):
        file4.write('%d x %d = %d\n'% (a, b, a*b))
file4.close()

# with문(파일생성과 close를 한번에 실행하는 구문)
with open('C:/Users/bigdata/Desktop/test5.txt', 'w') as file5:
    for i in range(11):
        file5.write('☆'*i+'\n')
