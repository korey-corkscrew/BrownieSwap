from brownie import *

def main():
    router = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
    weth = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2" #i've vetted this to be the true weth, future me
    Swappy.deploy(router, weth, {'from': accounts[0]})