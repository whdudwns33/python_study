# s의 i번째 열 글자가 포함되어 있으면 알파벳 순서의 j번째에 i가 들어가야함
# ad
# a => 0,
# 0, -1, -1, +1
# alp = []
# ch = [] * 26
# rst = [-1]*26
# s = list(input())
#
# # ord() 문자열을 아스키 코드로 변환
# for i in range(97, 123):
#     alp.append(chr(i))
# # print(ord(s[0]))
#
# for i in range(len(s)):
#     if s[i] in alp:
#         a = (ord(alp[ord(s[i]) - 97]) - 97)
#         rst[ord(s[i])-97] = a
# print(rst)

s = input()
a = "abcdefghijklmnopqrstuvwxyz"
for e in a:
    print(s.find(e), end= " ")  # a가 s를 순회하면서 없으면 -1, 해당 알파벳이 있으면 s의 해당 알파벳의 배열 번호를 출력







