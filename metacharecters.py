# -------[]----------
# import re
# text="hello how hello are 1223456789 are you"
# # x=re.findall('[a-h]',text)
# # x=re.findall('[a-zA-Z0-9]',text)
# x=re.findall('[ahn]',text)
# print(x)
# # -------.----------
# import re
# text="hello how how hello are 1223456789 are you"
# # x=re.findall("h.w",text)
# x=re.findall("h......",text)
# print(x)
# # -------^----------
# import re
# text="hello how how hello are 1223456789 are you"
# x=re.findall("^h",text)
# # x=re.findall("^hz",text)
# print(x)
# -----------$-----------
# import re
# text="hello how how hello are 1223456789 are you"
# x=re.findall("u$",text)
# print(x)
# ----------*----------
# import re
# text="hello how how hello are 1223456789 are you"
# x=re.findall("he.*o",text)
# print(x)
# ----------+----------
# import re
# text="hello how how hello are 1223456789 are you"
# x=re.findall("he.+o",text)
# print(x)
# # ----------?----------
# import re
# text="hello heo how how hello are 1223456789 are you"
# x=re.findall("he.?o",text)
# print(x)
# ----------{}----------
# import re
# text="hello heo planet"
# x=re.findall("h.{3}o",text)
# print(x)
# ----------|----------
# import re
# text="hello heo planet"
# # x=re.findall("h|o",text)
# # x=re.findall("h|z",text)
# x=re.findall("k|z",text)
# print(x)
# ----------\----------
# import re
# text="hello how are you"
# # x=re.findall("\Ah",text)
# x=re.findall("\Aa",text)
# print(x)
# ----------\----------
# import re
# text="hello heo you"
# x=re.findall("u\Z",text)
# # x=re.findall("h|z",text)
# # x=re.findall("k|z",text)
# print(x)


































