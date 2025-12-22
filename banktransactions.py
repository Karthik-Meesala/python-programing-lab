import numpy as np
transactions = np.array([
    [500, -200, 300, -100, 400],   # Account 1
    [1000, -500, -200, 300, 400],  # Account 2
    [200, 300, -100, -50, 150]     # Account 3
])
print("Transactions Data :\n", transactions)
print("\nTotal balance change per account:",np.sum(transactions,axis=1))
print("Average transaction per account:", np.average(transactions,axis=1))
print("Maximum transaction per account:",np.max(transactions,axis=1))
print("Minimum transaction per account:",np.min(transactions,axis=1))
print("\nTransaction Status (Deposit/Withdrawal):\n",np.where(transactions > 0, "Deposit", "Withdrawal"))
