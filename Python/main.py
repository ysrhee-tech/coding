# main.py

def calculate_change(payment, cost):
    # 코드를 작성하세요.
    change = payment - cost
    count_50000 = change // 50000

    change = change % 50000
    count_10000 = change // 10000

    change = change % 10000
    count_5000 = change // 5000

    change = change % 5000
    count_1000 = change // 1000

    print("%d원 지폐: %d장" % (50000, count_50000))
    print("%d원 지폐: %d장" % (10000, count_10000))
    print("%d원 지폐: %d장" % (5000, count_5000))
    print("%d원 지폐: %d장" % (1000, count_1000))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
