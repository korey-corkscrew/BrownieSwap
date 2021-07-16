from brownie import *
from scripts.polygon import *

def main():
    router = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
    weth = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2" #i've vetted this to be the true weth, future me
    USDC = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
    DAI = "0x6b175474e89094c44da98b954eedeac495271d0f"
    whale = "0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE"


    whale = accounts.at('0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE', force=True)


    tokenIn = USDC
    tokenOut = DAI
    amountIn = 1000000
    amountOut = amountIn - (amountIn * 0.01)
    to = whale
    frm = {"from": whale}
    Swappy[0].Swap(tokenIn, tokenOut, amountIn, amountOut, to, frm)