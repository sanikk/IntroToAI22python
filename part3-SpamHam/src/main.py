from spamham import SpamHam

HAM_FILE = 'hamcount.txt'
SPAM_FILE = 'spamcount.txt'


def main():
    antispambot = SpamHam(SPAM_FILE, HAM_FILE)
    print(antispambot.evaluate_from_file('spamesim.txt'))
    print(antispambot.evaluate_from_file('hamesim.txt'))
    # print(antispambot.evaluate('I am not a bot I swear'.split()))
    # print(antispambot.evaluate_from_input())
    # print(antispambot.evaluate('million'.split(" "))) # hups tää tuli eri lukemilla matskussa, ihmekään ettei natsannu :D
    # print(antispambot.evaluate('free'.split(" ")))


if __name__ == '__main__':
    main()
