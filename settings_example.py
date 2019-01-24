import logging

BASE_URL = 'https://www.bitmex.com/api/v1/'

API_KEY = '[API_KEY]'
API_SECRET = '[API_SECRET]'

SYMBOL = 'XBTUSD|ETHUSD'

TRADE_QUANTITY = 100

HEDGE = True
HEDGE_SIDE = 'Buy|Sell'
HEDGE_MULTIPLIER = .5

STOP_LIMIT_MULTIPLIER = .015
STOP_MULTIPlIER = .0175

LOOP_INTERVAL = 1

API_REST_INTERVAL = 3

TIMEOUT = 10

LOG_LEVEL = logging.INFO

ORDERID_PREFIX = 'mm_'
