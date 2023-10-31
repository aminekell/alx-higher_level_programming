import random

# توليد رقم عشوائي باستخدام random.randint(-10، 10)
number = random.randint(-10، 10)

# عرض الرقم وفحص علامته
print(f"{number} ", end='')

if number > 0:
    print("إيجابي")
elif number == 0:
    print("صفر")
else:
    print("سالب")

