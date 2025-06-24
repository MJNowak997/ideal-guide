def to_secs(h, m, s):
    nh = int(h)*3600
    nm = int(m)*60
    ns = int(s)
    total = nh+nm+ns
    return total

import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno   
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_suite()