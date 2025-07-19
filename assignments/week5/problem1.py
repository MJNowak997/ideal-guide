speech = '''Fellow Senators, friends, colleagues, allies, adversaries. I stand before you this morning with a heavy heart. I’ve spent my life in this chamber. I came here as a child. And as I look around now, I realize I have almost no memories that pre-date my arrival and few bonds of affection that cleave so tightly. Through these many years, I believe I have served my constituents honorably and upheld our code of conduct. This chamber is a cauldron of opinions and we’ve certainly all had our patience and tempers tested in pursuit of our ideals. Disagree as we might, I am hopeful that those of you who know me will vouch for my credibility in the days to come. I stand this morning with a difficult message. I believe we are in crisis. The distance between what is said and what is known to be true has become an abyss. Of all the things at risk, the loss of an objective reality is perhaps the most dangerous. The death of truth is the ultimate victory of evil. When truth leaves us, when we let it slip away, when it is ripped from our hands, we become vulnerable to the appetite of whatever monster screams the loudest. This Chamber’s hold on the truth was finally lost on the Ghorman Plaza. What took place yesterday… what happened yesterday on Ghorman was unprovoked genocide! Yes! Genocide! And that truth has been exiled from this chamber! And the monster screaming the loudest? The monster we’ve helped create? The monster who will come for us all soon enough is Emperor Palpatine!'''

import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def ewordfind(target):
    remove_punctuation(target)
    words = target.split()
    total = len(words)
    ewords = 0
    for word in words:
        if 'e' in word.lower():
            ewords = ewords + 1
        else:
            ewords = ewords
    percent = (ewords / total) * 100
    print(f'Your text contains {total} words, of which {ewords} ({percent}%) contain an "e".')

ewordfind(speech)