from typing import List

from jobcoin.client.jobcoin_client import JobcoinClient
from jobcoin.settings import get_settings

settings = get_settings()


def mix_coins(from_jobcoin_wallet_address: str, to_jobcoin_wallet_address: List[str], amount) -> dict:
    broken_down_amounts = break_down_amount_into_ratios(amount, len(to_jobcoin_wallet_address))
    transfer_the_balance_to_central_bank(from_jobcoin_wallet_address, amount)
    for to_wallet_address, amount in zip(to_jobcoin_wallet_address, broken_down_amounts):
        try:
            transfer_from_bank_to_wallet(to_wallet_address, amount)
        except Exception as error:
            print(error)
    response = {}
    return response


def check_coin_deposit():
    #     check if we got the jobcoins in our temp address.
    return True


def transfer_the_balance_to_central_bank(from_jobcoin_address: str, amount: float):
    JobcoinClient.post_data(from_jobcoin_address, settings.central_wallet_address, amount)


def transfer_from_bank_to_wallet(to_jobcoin_address: str, amount: float):
    JobcoinClient.post_data(settings.central_wallet_address, to_jobcoin_address, amount)


def break_down_amount_into_ratios(amount, parts):
    # this logic will be changed by randomizing the ratios.
    random_ratios = [amount / parts for _ in range(parts)]
    return random_ratios

# if __name__ == '__main__':
#     print(f"{mix_coins()}")
