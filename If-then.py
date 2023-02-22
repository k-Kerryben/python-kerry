code = input("Enter code")
if code == "*544#":
    print("1.Data deals "
          "2.Daily bundles "
          "3.Weekly bundles "
          "4.Monthly bundles "
          "5.Go monthly "
          "6.Check balance "
          "7.With no expiry "
          "98.More"
          )
else:
    print("Invalid USSD")

x = int(input("Enter Choice"))
if x == 1:
    print("1. 1GB 1Hour @sh.10  "
          "2. 5GB 3Days @sh.250")
elif x == 2:
    print("1. 200Mb @sh.20  "
          "2. 500Mb @sh.99")
elif x == 3:
    print("1. 10GB @sh.500  "
          "2. 2GB @sh.149")
elif x == 4:
    print("1. 15GB @sh.1000  "
          "2. 30GB @sh.2000")
elif x == 5:
    print("1. Unlimited Monthly bundle @5000")
elif x == 6:
    print("Your balance is ..**..")
elif x == 7:
    print("Thanks for your reliance")
elif x == 98:
    print("Welcome To Safaricom ON DEVELOPMENT")
else:
    print("Invalid Choice")
