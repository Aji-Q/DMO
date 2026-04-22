#!/usr/bin/env python3
"""moomoo US 手续费计算器

费率结构（在 config/holdings.yaml 中确认）：
- 平台费: $0.005/股，最低 $0.99/单
- SEC 费: 0.00278% 成交额（仅卖出）
- FINRA TAF: $0.000166/股（双向）

用法：
    from calculate_fees import calculate_moomoo_fees
    fees = calculate_moomoo_fees(shares=0.3, price=434.44, is_sell=False)
    # -> {'platform': 0.99, 'sec': 0.0, 'taf': 0.0, 'total': 0.99}
"""

PLATFORM_FEE_PER_SHARE = 0.005
PLATFORM_FEE_MIN = 0.99
SEC_FEE_RATE = 0.0000278  # 0.00278%
TAF_FEE_PER_SHARE = 0.000166


def calculate_moomoo_fees(shares: float, price: float, is_sell: bool) -> dict:
    """返回单笔交易的手续费分解."""
    platform_fee = max(PLATFORM_FEE_MIN, shares * PLATFORM_FEE_PER_SHARE)
    gross = shares * price
    sec_fee = (gross * SEC_FEE_RATE) if is_sell else 0.0
    taf_fee = shares * TAF_FEE_PER_SHARE
    total = platform_fee + sec_fee + taf_fee
    return {
        "platform": round(platform_fee, 4),
        "sec": round(sec_fee, 4),
        "taf": round(taf_fee, 4),
        "total": round(total, 4),
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("用法: python3 calculate_fees.py <shares> <price> <buy|sell>")
        sys.exit(1)
    shares = float(sys.argv[1])
    price = float(sys.argv[2])
    is_sell = sys.argv[3].lower() == "sell"
    fees = calculate_moomoo_fees(shares, price, is_sell)
    gross = shares * price
    action = "SELL" if is_sell else "BUY"
    print(f"{action} {shares} 股 @ ${price} = ${gross:.2f}")
    print(f"  平台费:   ${fees['platform']:.4f}")
    print(f"  SEC 费:   ${fees['sec']:.4f}")
    print(f"  FINRA TAF: ${fees['taf']:.4f}")
    print(f"  合计:     ${fees['total']:.4f}  ({fees['total']/gross*100:.3f}% of gross)")
