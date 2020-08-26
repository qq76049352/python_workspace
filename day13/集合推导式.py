# lst = ["麻花藤","马化腾","张建忠","张建忠","张雪白","张雪峰","张雪峰"]
#
# s = {i for i in lst}
# print(s)

def add(a, b):
    return a + b
def test():
    for r_i in range(4):
        yield r_i
g = test()
# for n in [2, 10,5]:
#     g = (add(n, i) for i in g)
#     g = (add(n, i) for i in test())
#     g = (add(n, i) for i in add(n, i) for i in test())
n = 5
g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in test())))

print(list(g))