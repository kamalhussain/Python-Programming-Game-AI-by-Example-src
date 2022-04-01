from miner import Miner

def main() -> None:
    m = Miner(1)
    mf = Miner(2)

    for _ in range(25):
        m.update()
        mf.update()

if __name__ == "__main__":
    main()