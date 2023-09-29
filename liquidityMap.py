from web3 import Web3
from eth_abi import decode
import requests
import json
import matplotlib.pyplot as plt

ALCHEMY_API_URL = (
    "https://eth-mainnet.g.alchemy.com/v2/0egnJaRphy3CFa9xRy7itveY8kKH2Ceg"
)

web3 = Web3(Web3.HTTPProvider(ALCHEMY_API_URL))
poolAddress = Web3.to_checksum_address("0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640")
pool = web3.eth.contract(
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

lensAddress = Web3.to_checksum_address("0xbfd8137f7d1516D3ea5cA83523914859ec47F573")
lensAbi = [
    {
        "inputs": [
            {"internalType": "address", "name": "pool", "type": "address"},
            {"internalType": "int16", "name": "tickBitmapIndex", "type": "int16"},
        ],
        "name": "getPopulatedTicksInWord",
        "outputs": [
            {
                "components": [
                    {"internalType": "int24", "name": "tick", "type": "int24"},
                    {
                        "internalType": "int128",
                        "name": "liquidityNet",
                        "type": "int128",
                    },
                    {
                        "internalType": "uint128",
                        "name": "liquidityGross",
                        "type": "uint128",
                    },
                ],
                "internalType": "struct ITickLens.PopulatedTick[]",
                "name": "populatedTicks",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    }
]
lens = web3.eth.contract(address=lensAddress, abi=lensAbi)


def tickToWord(tick):
    return tick >> 8  # tick / 2^8


liquidity = 0
MIN_TICK = -887272
MAX_TICK = 887272
TICK_SPACING = 10

MIN_WORD = -3466  # tickToWord(MIN_TICK)
MAX_WORD = 3465  # tickToWord(MAX_TICK)

print(MIN_WORD, MAX_WORD)


def getActiveTicks(minWord, maxWord):
    ticks = []

    batchSize = 1000

    for startWord in range(minWord, maxWord + 1, batchSize):
        endWord = min(startWord + batchSize, maxWord + 1)
        words = list(range(startWord, endWord))

        input_datas = [
            lens.encodeABI(
                fn_name="getPopulatedTicksInWord",
                args=["0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640", w],
            )
            for w in words
        ]

        payload = [
            {
                "jsonrpc": "2.0",
                "id": i + 1,
                "method": "eth_call",
                "params": [
                    {
                        "to": "0xbfd8137f7d1516D3ea5cA83523914859ec47F573",
                        "data": input_datas[i],
                    },
                    "latest",
                ],
            }
            for i in range(len(input_datas))
        ]
        response = requests.post(
            ALCHEMY_API_URL,
            headers={"content-type": "application/json"},
            data=json.dumps(payload),
        )

        if response.status_code == 200:
            results = response.json()
            tuple_types = ["(int24,int128,uint128)[]"]

            for result in results:
                data = result["result"]

                decoded_data = decode(tuple_types, bytes.fromhex(data[2:]))

                for inner_tuple in decoded_data:
                    for coordinates in inner_tuple:
                        ticks.append(coordinates)

        else:
            print("Error:", response.status_code)

    return ticks


def calcLiquidityMap(dataset):
    sorted_dataset = sorted(dataset, key=lambda x: x[0])
    ticks = []
    liquidity = 0
    for data in sorted_dataset:
        tick = data[0]
        liquidity += data[1]

        ticks.append((tick, liquidity))

    filled_ticks = []

    for i in range(len(ticks) - 1):
        filled_ticks.append(ticks[i])
        diff = ticks[i + 1][0] - ticks[i][0]
        if diff > 1:
            for j in range(1, diff):
                filled_ticks.append((ticks[i][0] + j, ticks[i][1]))

    filled_ticks.append(ticks[-1])

    return sorted_dataset


dataset = getActiveTicks(MIN_WORD, MAX_WORD)  # [(tick, liquidityNet, liquidityGross),]
ticks = calcLiquidityMap(dataset)


print(len(ticks))


x, y = zip(*ticks)

# プロット
plt.plot(x, y, marker="o")

# グラフのタイトルと軸ラベルを設定
plt.title("Ticks Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# グリッドを表示
plt.grid(True)

# グラフを表示
plt.show()
