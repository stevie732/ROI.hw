Investment = 4000 
Rent = 700
Loss = 1000

def ROI(Investment, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Investment)*100
    print(ROI)

ROI(Investment, Rent, Loss)