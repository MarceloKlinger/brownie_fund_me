from brownie import FundMe, accounts

from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrace_fee = fund_me.getEntranceFee()
    print(f"Entrace fee: {entrace_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrace_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
