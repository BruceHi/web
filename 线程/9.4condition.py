from threading import Thread, Condition


def condition():
    ret = False
    r = input('>>>')
    if r == 'yes':
        ret = True
    return ret


def func(conn, i):
    conn.acquire()
    conn.wait_for(condition)
    print(i + 100)
    conn.release()


c = Condition()
for i in range(5):
    t = Thread(target=func, args=(c, i))
    t.start()
