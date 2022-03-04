import requests

from jobcoin.settings import get_settings

SETTINGS = get_settings()


class JobcoinClient:

    @staticmethod
    def get_data() -> dict:
        uri = SETTINGS.jobcoin_base_url
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def post_data(from_wallet_address_payload: str, to_wallet_address: str, amount: float) -> dict:
        payload = {from_wallet_address_payload, to_wallet_address, amount}
        uri = SETTINGS.jobcoin_transaction_post_url
        response = requests.post(uri, json=payload)
        response.raise_for_status()
        return response.json()
