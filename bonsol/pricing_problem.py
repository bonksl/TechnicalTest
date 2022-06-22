def pricing_problem(item, price, prov):
    discount = [1000, 5000, 7000, 10000]
    province = ["AB", "ON", "QC", "MI", "DE"]
    total = 0
    total = item * price
    for discounts in discount:
        # 3% discount rate
        if 1000 <= total and total < 5000:
            total = total - total * 0.03
            break
        # 5% discount rate
        elif 5000 <= total and total < 7000:
            total = total - total * 0.05
            break
        # 7% discount rate
        elif 7000 <= total and total < 10000:
            total = total - total * 0.07
            break
        # 10% discount rate
        elif 10000 <= total:
            total = total - total * 0.1
            break
        # no discount rate
        else:
            break

    for provinces in province:
        # 5% tax
        if prov == "AB":
            total = total * 1.05
            break
        # 13% tax
        elif prov == "ON":
            total = total * 1.13
            break
        # 14.975% tax
        elif prov == "QC":
            total = total * 1.14975
            break
        # 6% tax
        elif prov == "MI":
            total = total * 1.06
            break
        # no tax
        elif prov == "DE":
            break
        else:
            break
    return "$" + str(round(total, 2))
