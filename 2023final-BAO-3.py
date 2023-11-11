"""
QUESTION THREE
Shift Cipher
This is a question about cryptography and ciphers.
The decipher shift increments with each new sentence.

i) Write a programov  markyy (?)
Your program should input a line of text.
It should concatenate the ascii values of the lowercase vowels in the string.
It must also add a nine and a three for spaces.
The program needs to print out this string.

ii) Translate the following string.
Show your working.
ABOLYMPIADO
iii)
"""

text = input()

out = ""

for char in text:
    if char == " ":
        out += "93"
    elif char in "aeiou":
        out += str(ord(char))

print(out)

# Works for testcase

# Encrypted Problem - Decrypting

# R|?VUJ?UTFV|?R?JPO:U|FSI?SF?|F
# Q  U   TSE     ION T   H RE  E

# 18 |? 22 21 10 ? 21 20 6 22 | ? 18 ? 10 16 15 : 21 | 6 19 9 ? 19 6 ? | 6

# : -> space
# Caesar Shift 1 - does it change?

# Between Q marks = delete
#
# def caesarShift(s:str, shift:int):
#     ignore_as_qmark = False
#     reverse_current = False
#     result = ""
#
#     reversed_slice = ""
#
#     for char in s:
#         # Ignore between question marks
#         if ignore_as_qmark:
#             if char == "?":
#                 ignore_as_qmark = False
#         elif char == "?":
#             ignore_as_qmark = True
#         else:
#             # Reverse between pipes
#             if reverse_current:
#                 if char == "|":
#                     reverse_current = False
#                     result += reversed_slice[::-1]
#                 else:
#                     reversed_slice += decodeChar(char, shift)
#             elif char == "|":
#                 reverse_current = True
#                 reversed_slice = ""
#             else:
#                 result += decodeChar(char, shift)
#     return result
#
# def decodeChar(char:str, shift:int):
#     if char == ":":
#         return " "
#     elif char == ".": return "."
#     else:
#         # Decode Caesar Shift
#         ascii_num = ord(char)
#         if ascii_num >= 97:
#             # Lowercase
#             ascii_num -= 97
#             ascii_num -= shift # Decode Caesar Shift
#             ascii_num %= 26 # Wrap Around
#             ascii_num += 97
#         else:
#             # Uppercase
#             ascii_num -= 65
#             ascii_num -= shift  # Decode Caesar Shift
#             ascii_num %= 26  # Wrap Around
#             ascii_num += 65
#
#         return chr(ascii_num)
#
# lines = """R|?VUJ?UTFV|?R?JPO:U|FSI?SF?|F
# Ujkh?ks:dpj?v:Ekrjg|t|
# Wk?:a:f?lv:lv:d:|wvhxt|lr?xrc:g:puklp|gc|?q:derx|w|:fubswrj?:?udskb:dqg:flskhu?|evv|?v.
# X|i?gv|imr|???l|:h?x|gxlw|?ig|viltm|:wl|qivgrm:xjm|irxw:am?:xmx?xl:iegl:ria:wir|x??|irgi.
# B?k?||?rugqgj?wn?gga?yj:f|rfwltwu:?fy:wzsx?||?j:f:uwtl?ddp??wfr::at?ty:|:xt|aq|j:f:x|n|ru|jq|:uwt?|?|qg|jr.
# Euax?:grcgey:vxotz:|znk|:ygsk:tashkx?:vx?um?um|sgx|:ynua??rj:ot?vxum|xgs|:?vaz:g:r|o||kt|:ul:zkd?src?z.
# Pa:|ksb?rla|h|?voz|:jv?vad?ujh|lah?m?ula|:aol:|h|z?pucdav?j|p?klcs?p|:ch|s|blz:vm:a|?rh?|ol:svd?egrwty?lyjhzl:c?|emq|q?vdlsz:p||u:aol:zay?|ya|z?pu?|tz|?n.
# Qb:uc?addvsx:sdt|fuyl:|:||dth|mmk|az?ab:|ti|aw:i?e?ll:i:vqvm:ivl:i:b?bp?p|mmz|:?for?nwz:axik?efer|ak|||?ma.
# Cqn:ya?jqr?xpajv:w?dem?nnm?tb|qo|g|nw|d?b:cx:yar?lmm?wc:xdc:cqrb:bca?nn|hqs|?rwp.
# D?sahzkd?bkxc|dkv|o:dro:py|?dfev?|vvygsxq:cdbs?xi?xq.
# D?szh?|hzs|:jzf?i?c:hzc|t?dqv?v|yr.
# |PMUBYKXA?|?NM|A|""".split("\n")
#
# print(lines)
#
# for i in range(len(lines)):
#     # Shift increments for each line
#     print(caesarShift(lines[i], i+1))