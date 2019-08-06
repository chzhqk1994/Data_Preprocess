test_dict = {"left": [0, 720], "top": [457, 286], "right": [1280, 720]}

lx, ly = test_dict["left"]
rx, ry = test_dict["right"]
tx, ty = test_dict["top"]

m1 = ((ty - ly) / (tx - lx))
n1 = ly - (m1 * lx)
print('m1 : ', m1)
print('n1 : ', n1)
polynomial1 = lambda ax: m1 * ax + n1

m2 = ((ty - ry) / (tx - rx))
n2 = (ry - (m2 * rx))
print('m2 : ', m2)
print('n2 : ', n2)
polynomial2 = lambda bx: m2 * bx + n2

# title 출력
if n1 > 0:
    title = 'linear equation graph : y = ' + str(m1) + 'x + ' + str(abs(n1))
elif n1 < 0:
    title = 'linear equation graph : y = ' + str(m1) + 'x - ' + str(abs(n1))
else:  # n == 0이면
    title = 'linear equation graph : y = ' + str(m1) + 'x'
print(title)

# title 출력
if n2 > 0:
    title = 'linear equation graph : y = ' + str(m2) + 'x + ' + str(abs(n2))
elif n2 < 0:
    title = 'linear equation graph : y = ' + str(m2) + 'x - ' + str(abs(n2))
else:  # n == 0이면
    title = 'linear equation graph : y = ' + str(m2) + 'x'
print(title)


print(lx, ly)
print(rx, ry)
print(tx, ty)

xmid = 428
ymid = 334

# 두 직선의 안쪽에 Bounding Box 의 중심 점이 위치한 경우에만 처리
if (ymid >= int(polynomial1(xmid))) and (ymid >= int(polynomial2(xmid))):
    print(polynomial1(xmid))
    print(polynomial2(xmid))
    print('pass')
else:
    print('nope')
