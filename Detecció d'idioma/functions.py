def Tr_txt(text):
    # chr from ascii to character
    # ord from character to ascii
    str = ""
    j = 0
    i = 0
    ln = len(text)
    while i < ln:
        carac = ord(text[i])
        if (carac >= 9 and carac <= 12):
            carac = ord(" ")
        if carac >= ord("0") and carac <= ord("9"):
            pass
        elif carac >= ord("A") and carac <= ord("Z"):
            str += chr(carac + 32)
            j += 1
        elif carac == ord(" "):
            if (j != 0 and str[j - 1] == " ") or j == 0:
                pass
            else:
                str += chr(carac)
                j += 1
        else:
            str += chr(carac)
            j += 1
        i += 1
    return str

def separation(sentences):
    str = ""
    str += Tr_txt(sentences.pop(0))
    str += "  "
    for sentence in sentences:
        str += "  "
        str += Tr_txt(sentence)
    return str