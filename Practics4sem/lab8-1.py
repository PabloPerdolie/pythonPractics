# def main(input_str):
#     new_str = input_str.replace("[ <%", "").replace("%>,]", "").strip()
#     pairs = new_str.split("%>,")
#     res = {}
#     for pair in pairs:
#         pair = pair.strip()
#         if pair == " " or pair == "":
#             continue
#         key_value = pair.split("=")
#         key = key_value[0]
#         value = key_value[1]
#         key = key.replace("local", "").strip(" <%")
#         value = value.strip(" #-.")
#         res[key] = value
#     return res
# print(main("[ <% local atbi = #-9134. %>, <% local xeatis = #6737. %>,]"))
#
# def main_2(input_str):
#     new_str = input_str.replace(".do", "").replace(".end", "").strip().replace("variable", "")
#     pairs = new_str.split(";")
#     res = []
#     for pair in pairs:
#         pair.strip()
#         if pair == "" or pair == ' ':
#             continue
#         key_value = pair.split("|>")
#         key = key_value[0]
#         value = key_value[1]
#         key = key.strip(" .begin#")
#         value = value.strip(" q()")
#         res.append((value, key))
#     return res
#
#
# str_1 = '.do .begin variable#3466 |> q(telaor_907).end; .begin variable #-9875'
# str_2 = '|> q(riar_101) .end; .begin variable#-8276 |>q(enaror_521).end; .end'
# print(main_2(str_1 + str_2))

def main_3(input_str):
    new_str = input_str.replace(".begin", "")\
        .replace(".end", "")\
        .replace("<%", "")\
        .replace("%>", "")\
        .replace("variable", "")\
        .replace("q(", "")\
        .replace(")", "")\
        .replace(".", "")\
        .replace(' ', "").strip()
    pairs = new_str.split(";")
    print(pairs)
    res = []
    for pair in pairs:
        pair.strip()
        if pair == "" or pair == ' ':
            continue
        key_value = pair.split("<-")
        key = key_value[0]
        value = key_value[1]
        res.append((key, value))
        print(key, value)
    return res


print(main_3(".begin <% variable q(edsoat_66) <- maen_271. %>;<% variable q(xeat) <- usbi. %>; <% variable q(sole) <- teve. %>;<% variable q(enin_212) <- redi_825. %>;.end"))
