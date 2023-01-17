def miane_miyangin (t):
    import numpy as f
    miane = f.median(t)
    miyangin = f.mean(t)
    res = (miyangin, miane)
    print (res)


miane_miyangin ((3, 3, 0, 1, 12, 13, 15, 16))    