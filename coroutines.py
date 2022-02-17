# we use coroutine to save time by not running same time_consuming operations again and again
def searcher() :
    a = " suraj djna csicna jacnka print ajncka cdswjnfkj jkwnfjas jkcfwbskcs ekfbcskm cswhvkldj scwecbn blcavyaeldhdc" \
        "cjnshbdcjscbsjcbskbcc good ok "
    import time
    time.sleep(3)
    while True :
        text = (yield)
        if text in a :
            print(f"{text} is in the file.")
        else :
            print(f"{text} is not in the file.")

search = searcher()
next(search)
search.send("print")
search.send("suraj")
search.send("dsshbkhvs")
search.close()
search1 = searcher()
next(search1)
search1.send("sc")