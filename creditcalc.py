import math
import argparse

parser = argparse.ArgumentParser(usage="This program calculates and prints \
Differentiate or Annuity payments.")

parser.add_argument("--type", type=str, choices=["diff", "annuity"],
                    help="You need to choose only one method from the list.")
parser.add_argument("--payment", type=int, help="You need to define payment in numbers.")
parser.add_argument("--principal", type=int, help="You need to specify principal in numbers.")
parser.add_argument("--periods", type=int, help="You need to mention the number of periods.")
parser.add_argument("--interest", type=float, help="You need to specify the interest in numbers (percentage).")
args = parser.parse_args()


def differentiate(p, n, i):
    i = i / (12 * 100)
    payments = []
    for m in range(n):
        m += 1
        d = (p / n + i * (p - p * (m - 1) / n))
        payments.append(math.ceil(d))
        print(f"Month {m}: payment is {math.ceil(d)}")
    print(f"\nOverpayment = {sum(payments) - p}")


def annuity(i, n=0, p=0, a=0):
    i = i / (12 * 100)

    if not n:
        n = math.log(a / (a - i * p), 1 + i)
        years, months = divmod(n, 12)
        if math.ceil(months) == 12:
            years += 1
            print("It will take {} years to repay this loan!".format(int(years)))
        elif years < 1:
            print("It will take {} months to repay this loan!".format(math.ceil(months)))
        else:
            print("It will take {} years {} months to repay this loan!".format(years, math.ceil(months)))
        n = math.ceil(n)
        print(f"Overpayment = {math.ceil((a * n) - p)}")
    elif p and not a:
        a = p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
        print(f"Your annuity payment = {math.ceil(a)}!")
        print(f"Overpayment = {math.ceil(a) * n - p}!")
    elif a and not p:
        p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        print(f"Your loan principal = {math.floor(p)}!")
        print(f"Overpayment = {math.ceil(a * n - p)}!")


try:
    if args.type == "diff":
        differentiate(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        if args.periods is None:
            annuity(p=args.principal, i=args.interest, a=args.payment)
        elif args.principal:
            annuity(n=args.periods, i=args.interest, p=args.principal)
        elif args.payment:
            annuity(n=args.periods, i=args.interest, a=args.payment)

except:
    print("Incorrect Parameters")
