from django.conf import settings

import hmac
from hashlib import sha512

BCH = "BCH"
BLK = "BLK"
BTC = "BTC"
DASH = "DASH"
DCR = "DCR"
DGB = "DGB"
DOGE = "DOGE"
ETC = "ETC"
ETH = "ETH"
EXP = "EXP"
GAME = "GAME"
LSK = "LSK"
LTC = "LTC"
MAID = "MAID"
NAV = "NAV"
NEO = "NEO"
POT = "POT"
SBD = "SBD"
STEEM = "STEEM"
STRAT = "STRAT"
VTC = "VTC"
XEM = "XEM"
XMR = "XMR"
XRP = "XRP"
XVG = "XVG"
CURRENCY_CHOICES = (
    (BCH, 'Bitcoin Cash'),
    (BLK, 'BlackCoin'),
    (BTC, 'Bitcoin'),
    (DASH, 'Dash'),
    (DCR, 'Decred'),
    (DGB, 'DigiByte'),
    (DOGE, 'Dogecoin'),
    (ETC, 'Ether Classic'),
    (ETH, 'Ether'),
    (EXP, 'Expanse'),
    (GAME, 'GameCredits'),
    (LSK, 'LISK'),
    (LTC, 'Litecoin'),
    (MAID, 'MaidSafeCoin'),
    (NAV, 'NAV Coin'),
    (NEO, 'NEO'),
    (POT, 'PotCoin'),
    (SBD, 'Steem Dollars'),
    (STEEM, 'STEEM'),
    (STRAT, 'Stratis'),
    (VTC, 'Vertcoin'),
    (XEM, 'NEM'),
    (XMR, 'Monero'),
    (XRP, 'Ripple'),
    (XVG, 'VERGE'),
)


def get_coins_list():
    coins = getattr(settings, 'COINPAYMENTS_ACCEPTED_COINS', None)
    if not coins:
        coins = CURRENCY_CHOICES
    return coins


def create_ipn_hmac(request):
    # secret = 'you sould set your API secret in here and then uncomment this line'

    # for example:
    # secret = 'mysecret'
    secret = 'default'
    encoded = request[2:-1]
    computed_sig = hmac.new(
        bytearray(secret, 'utf-8'),
        msg=bytearray(encoded, 'utf-8'), digestmod=sha512
    ).hexdigest()
    print(computed_sig)
    return computed_sig
