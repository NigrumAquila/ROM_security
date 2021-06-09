def doit(stop_event, arg):
    while not stop_event.wait(1):
        print ("working on %s" % arg)
    print("Stopping as you wish.")


def main():
    pill2kill = threading.Event()
    t = threading.Thread(target=doit, args=(pill2kill, "task"))
    t.start()
    time.sleep(5)
    pill2kill.set()
    t.join()