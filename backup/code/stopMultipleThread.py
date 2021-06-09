def main():
    pill2kill = threading.Event()
    tasks = ["task ONE", "task TWO", "task THREE"]

    def thread_gen(pill2kill, tasks):
        for task in tasks:
            t = threading.Thread(target=doit, args=(pill2kill, task))
            yield t

    threads = list(thread_gen(pill2kill, tasks))
    for thread in threads:
        thread.start()
    time.sleep(5)
    pill2kill.set()
    for thread in threads:
        thread.join()