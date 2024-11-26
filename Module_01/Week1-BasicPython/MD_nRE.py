def MD_nRE(y, y_hat, n, p):
    return (y ** (1/n) - y_hat ** (1/n)) ** p


print(MD_nRE(y=100, y_hat=99.5, n=2, p=1))
print(MD_nRE(y=50, y_hat=49.5, n=2, p=1))
print(MD_nRE(y=20, y_hat=19.5, n=2, p=1))
print(MD_nRE(y=0.6, y_hat=0.1, n=2, p=1))
