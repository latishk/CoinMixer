from dataclasses import dataclass

from jobcoin.config import API_TRANSACTIONS_URL, API_ADDRESS_URL, API_BASE_URL, CENTRAL_WALLET_ADDRESS


@dataclass
class Settings:
    jobcoin_base_url: str
    jobcoin_get_balance_by_ids_url: str
    jobcoin_transaction_post_url: str
    central_wallet_address: str
    header_accept: str


def get_settings() -> Settings:
    return Settings(jobcoin_base_url=API_BASE_URL,
                    jobcoin_get_balance_by_ids_url=API_ADDRESS_URL,
                    jobcoin_transaction_post_url=API_TRANSACTIONS_URL,
                    central_wallet_address=CENTRAL_WALLET_ADDRESS,
                    header_accept="application/jobcoin"
                    )
