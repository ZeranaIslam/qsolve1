5.Create a program that calculates the discount based on the purchase.Tf the purchase amount is greater than 100 dollars,
  apply a 10% discount;otherwise,apply a 5% discount.


amount = int(input("Enter bill amount: "))
if(amount>0):
    if amount >=100:
        discount = amount*10/100
    elif amount <100:
        discount = amount*5/100
    print("discount :",discount)
    print("Total pay : ",amount-discount)
else:
    print("invalid amount")
