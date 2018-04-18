import time

from tasks import add, step2


def main():
    while True:
        time.sleep(5)
        print("Adding work to queue")
        chain = add.s(1, 2) | step2.s()
        res = chain()
        for result, value in res.collect(intermediate=True):
            print(value)




if __name__ == '__main__':
    main()
