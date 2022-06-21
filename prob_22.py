Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].







def find_sentence(dictionary, s):
    sentence, valid = find_sentence_helper(dictionary, s)
    if valid:
        return sentence

def find_sentence_helper(dictionary, s):
    if len(s) == 0:
        return [], True

    result = []
    for i in range(len(s) + 1):
        prefix, suffix = s[:i], s[i:]
        if prefix in dictionary:
            rest, valid = find_sentence_helper(dictionary, suffix)
            if valid:
                return [prefix] + rest, True
    return [], False