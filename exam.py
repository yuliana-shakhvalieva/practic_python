class StrategyDeal:

    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        return self.targets

    def get_target_percents(self):
        return [(target / self.entry - 1) * 100 for target in self.targets]

    def get_target_banks(self):
        return [self.bank * target / self.entry for target in self.targets]

    def get_str_target(self, i):
        target = f"{i + 1} target: {self.get_targets()[i]}\n"
        percent = f"Percent: {round(self.get_target_percents()[i], 3)}%\n"
        bank = f"Bank: {round(self.get_target_banks()[i], 3)}"
        return target + percent + bank

    def __str__(self):
        targets = '\n\n'.join([self.get_str_target(i) for i in range(len(self.targets))])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def read_data(file_name):
    with open(file_name) as file:
        return file.read()


def parse_data(content):
    deals_content = content.split("-----")
    deals = []
    for deal_index, deal_raw in enumerate(deals_content):
        if len("".join(deal_raw.split())) == 0:
            continue

        bank_index = deal_raw.find('Bank')
        entry_index = deal_raw.find('Entry')
        target_index = deal_raw.find('Target')
        close_index = deal_raw.find('Close')

        if bank_index == -1 or entry_index == -1 or target_index == -1 or close_index == -1:
            raise Exception('File format does not follow the regular convention at deal #' + str(deal_index + 1))

        bank = float(deal_raw[bank_index + 5:deal_raw.find('\n', bank_index) - 3])
        entry = float(deal_raw[entry_index + 7:deal_raw.find('\n', entry_index) - 3])
        target = [float(tar[:-3]) for tar in deal_raw[target_index + 8:deal_raw.find('\n', target_index)].split(';')]
        close = float(deal_raw[close_index + 6:deal_raw.find('\n', close_index) - 3])

        deals.append(StrategyDeal(bank, entry, target, close))

    return deals


def write_data(file_name, data):
    f = open(file_name, 'w')
    f.write("\n\n-----\n\n".join([str(d) for d in data]))
    f.close()


def main():
    content = read_data('deals.txt')
    result = parse_data(content)
    write_data('out.txt', result)


if __name__ == '__main__':
    main()
