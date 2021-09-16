# baekjoon 알고리즘 단계별 문제
# 문자열
# 단어 공부 (1157번)

word = input().upper()
n_word = list(set(word))

count_w = []
for i  in n_word:
    c = word.count(i)     # n_word에 단어가 word에 몇번 나오는지 count하여 c에 저장
    count_w.append(c)

if count_w.count(max(count_w)) > 1:   # count_w에 append 한 c 중 제일 큰 숫자가 2개 이상일 시 print: ?
    print('?')
else:
    print(n_word[count_w.index(max(count_w))]) # count_w에서 제일 큰 숫자의 index를 n_word 인덱스로 하면 그의 해당하는 단어 출력






    