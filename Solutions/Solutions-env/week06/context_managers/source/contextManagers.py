from Performance import Performance
import time

def main():
    with Performance("test.txt") as perf:
        time.sleep(1)


if __name__ == '__main__':
    main()
    