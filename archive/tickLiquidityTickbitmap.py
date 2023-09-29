from collections import namedtuple
from web3 import Web3

web3 = Web3(
    Web3.HTTPProvider(
        "https://eth-mainnet.g.alchemy.com/v2/0egnJaRphy3CFa9xRy7itveY8kKH2Ceg"
    )
)
pool = Web3.to_checksum_address("0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640")
contract = web3.eth.contract(
    address="0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
    abi=[
        {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "int24",
                    "name": "tickLower",
                    "type": "int24",
                },
                {
                    "indexed": True,
                    "internalType": "int24",
                    "name": "tickUpper",
                    "type": "int24",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "amount",
                    "type": "uint128",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
            ],
            "name": "Burn",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "int24",
                    "name": "tickLower",
                    "type": "int24",
                },
                {
                    "indexed": True,
                    "internalType": "int24",
                    "name": "tickUpper",
                    "type": "int24",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "amount0",
                    "type": "uint128",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "amount1",
                    "type": "uint128",
                },
            ],
            "name": "Collect",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "amount0",
                    "type": "uint128",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "amount1",
                    "type": "uint128",
                },
            ],
            "name": "CollectProtocol",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "paid0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "paid1",
                    "type": "uint256",
                },
            ],
            "name": "Flash",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint16",
                    "name": "observationCardinalityNextOld",
                    "type": "uint16",
                },
                {
                    "indexed": False,
                    "internalType": "uint16",
                    "name": "observationCardinalityNextNew",
                    "type": "uint16",
                },
            ],
            "name": "IncreaseObservationCardinalityNext",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint160",
                    "name": "sqrtPriceX96",
                    "type": "uint160",
                },
                {
                    "indexed": False,
                    "internalType": "int24",
                    "name": "tick",
                    "type": "int24",
                },
            ],
            "name": "Initialize",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "int24",
                    "name": "tickLower",
                    "type": "int24",
                },
                {
                    "indexed": True,
                    "internalType": "int24",
                    "name": "tickUpper",
                    "type": "int24",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "amount",
                    "type": "uint128",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
            ],
            "name": "Mint",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "feeProtocol0Old",
                    "type": "uint8",
                },
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "feeProtocol1Old",
                    "type": "uint8",
                },
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "feeProtocol0New",
                    "type": "uint8",
                },
                {
                    "indexed": False,
                    "internalType": "uint8",
                    "name": "feeProtocol1New",
                    "type": "uint8",
                },
            ],
            "name": "SetFeeProtocol",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "amount0",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "amount1",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "uint160",
                    "name": "sqrtPriceX96",
                    "type": "uint160",
                },
                {
                    "indexed": False,
                    "internalType": "uint128",
                    "name": "liquidity",
                    "type": "uint128",
                },
                {
                    "indexed": False,
                    "internalType": "int24",
                    "name": "tick",
                    "type": "int24",
                },
            ],
            "name": "Swap",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "int24", "name": "tickLower", "type": "int24"},
                {"internalType": "int24", "name": "tickUpper", "type": "int24"},
                {"internalType": "uint128", "name": "amount", "type": "uint128"},
            ],
            "name": "burn",
            "outputs": [
                {"internalType": "uint256", "name": "amount0", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "int24", "name": "tickLower", "type": "int24"},
                {"internalType": "int24", "name": "tickUpper", "type": "int24"},
                {
                    "internalType": "uint128",
                    "name": "amount0Requested",
                    "type": "uint128",
                },
                {
                    "internalType": "uint128",
                    "name": "amount1Requested",
                    "type": "uint128",
                },
            ],
            "name": "collect",
            "outputs": [
                {"internalType": "uint128", "name": "amount0", "type": "uint128"},
                {"internalType": "uint128", "name": "amount1", "type": "uint128"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {
                    "internalType": "uint128",
                    "name": "amount0Requested",
                    "type": "uint128",
                },
                {
                    "internalType": "uint128",
                    "name": "amount1Requested",
                    "type": "uint128",
                },
            ],
            "name": "collectProtocol",
            "outputs": [
                {"internalType": "uint128", "name": "amount0", "type": "uint128"},
                {"internalType": "uint128", "name": "amount1", "type": "uint128"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "factory",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "fee",
            "outputs": [{"internalType": "uint24", "name": "", "type": "uint24"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "feeGrowthGlobal0X128",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "feeGrowthGlobal1X128",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "uint256", "name": "amount0", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1", "type": "uint256"},
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "flash",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "uint16",
                    "name": "observationCardinalityNext",
                    "type": "uint16",
                }
            ],
            "name": "increaseObservationCardinalityNext",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint160", "name": "sqrtPriceX96", "type": "uint160"}
            ],
            "name": "initialize",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "liquidity",
            "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "maxLiquidityPerTick",
            "outputs": [{"internalType": "uint128", "name": "", "type": "uint128"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "int24", "name": "tickLower", "type": "int24"},
                {"internalType": "int24", "name": "tickUpper", "type": "int24"},
                {"internalType": "uint128", "name": "amount", "type": "uint128"},
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "mint",
            "outputs": [
                {"internalType": "uint256", "name": "amount0", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "observations",
            "outputs": [
                {"internalType": "uint32", "name": "blockTimestamp", "type": "uint32"},
                {"internalType": "int56", "name": "tickCumulative", "type": "int56"},
                {
                    "internalType": "uint160",
                    "name": "secondsPerLiquidityCumulativeX128",
                    "type": "uint160",
                },
                {"internalType": "bool", "name": "initialized", "type": "bool"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint32[]", "name": "secondsAgos", "type": "uint32[]"}
            ],
            "name": "observe",
            "outputs": [
                {
                    "internalType": "int56[]",
                    "name": "tickCumulatives",
                    "type": "int56[]",
                },
                {
                    "internalType": "uint160[]",
                    "name": "secondsPerLiquidityCumulativeX128s",
                    "type": "uint160[]",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "name": "positions",
            "outputs": [
                {"internalType": "uint128", "name": "liquidity", "type": "uint128"},
                {
                    "internalType": "uint256",
                    "name": "feeGrowthInside0LastX128",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "feeGrowthInside1LastX128",
                    "type": "uint256",
                },
                {"internalType": "uint128", "name": "tokensOwed0", "type": "uint128"},
                {"internalType": "uint128", "name": "tokensOwed1", "type": "uint128"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "protocolFees",
            "outputs": [
                {"internalType": "uint128", "name": "token0", "type": "uint128"},
                {"internalType": "uint128", "name": "token1", "type": "uint128"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "feeProtocol0", "type": "uint8"},
                {"internalType": "uint8", "name": "feeProtocol1", "type": "uint8"},
            ],
            "name": "setFeeProtocol",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "slot0",
            "outputs": [
                {"internalType": "uint160", "name": "sqrtPriceX96", "type": "uint160"},
                {"internalType": "int24", "name": "tick", "type": "int24"},
                {
                    "internalType": "uint16",
                    "name": "observationIndex",
                    "type": "uint16",
                },
                {
                    "internalType": "uint16",
                    "name": "observationCardinality",
                    "type": "uint16",
                },
                {
                    "internalType": "uint16",
                    "name": "observationCardinalityNext",
                    "type": "uint16",
                },
                {"internalType": "uint8", "name": "feeProtocol", "type": "uint8"},
                {"internalType": "bool", "name": "unlocked", "type": "bool"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "int24", "name": "tickLower", "type": "int24"},
                {"internalType": "int24", "name": "tickUpper", "type": "int24"},
            ],
            "name": "snapshotCumulativesInside",
            "outputs": [
                {
                    "internalType": "int56",
                    "name": "tickCumulativeInside",
                    "type": "int56",
                },
                {
                    "internalType": "uint160",
                    "name": "secondsPerLiquidityInsideX128",
                    "type": "uint160",
                },
                {"internalType": "uint32", "name": "secondsInside", "type": "uint32"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "bool", "name": "zeroForOne", "type": "bool"},
                {"internalType": "int256", "name": "amountSpecified", "type": "int256"},
                {
                    "internalType": "uint160",
                    "name": "sqrtPriceLimitX96",
                    "type": "uint160",
                },
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "swap",
            "outputs": [
                {"internalType": "int256", "name": "amount0", "type": "int256"},
                {"internalType": "int256", "name": "amount1", "type": "int256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "int16", "name": "", "type": "int16"}],
            "name": "tickBitmap",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "tickSpacing",
            "outputs": [{"internalType": "int24", "name": "", "type": "int24"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "int24", "name": "", "type": "int24"}],
            "name": "ticks",
            "outputs": [
                {
                    "internalType": "uint128",
                    "name": "liquidityGross",
                    "type": "uint128",
                },
                {"internalType": "int128", "name": "liquidityNet", "type": "int128"},
                {
                    "internalType": "uint256",
                    "name": "feeGrowthOutside0X128",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "feeGrowthOutside1X128",
                    "type": "uint256",
                },
                {
                    "internalType": "int56",
                    "name": "tickCumulativeOutside",
                    "type": "int56",
                },
                {
                    "internalType": "uint160",
                    "name": "secondsPerLiquidityOutsideX128",
                    "type": "uint160",
                },
                {"internalType": "uint32", "name": "secondsOutside", "type": "uint32"},
                {"internalType": "bool", "name": "initialized", "type": "bool"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "token0",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "token1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
    ],
)


Tick = namedtuple(
    "Tick",
    "liquidityGross liquidityNet feeGrowthOutside0X128 feeGrowthOutside1X128 tickCumulativeOutside secondsPerLiquidityOutsideX128 secondsOutside initialized",
)

liquidity = 0
slot0 = contract.functions.slot0().call()

MIN_TICK = -887272
MAX_TICK = 887272
TICK_SPACING = 10


# calc word and bit positions within the Tick Bitmap
def position(tick):
    wordPos = tick >> 8  # tick / 2^8
    bitPos = tick % 256

    return wordPos, bitPos


def ticksInWord(wordPos):
    map = contract.functions.tickBitmap(wordPos).call()
    print(map)
    map_256 = (bin(map)[2:]).zfill(256)

    one_indexes = [i for i, bit in enumerate(map_256) if bit == "1"]

    print(one_indexes)

    ticks = [wordPos * (2**8) + index for index in one_indexes]

    print(ticks)


ticksInWord(0)
