from multiprocessing import Pool
import time

def fun(n):
    # s = 0
    # for i in range(1000):
    #     s+=i*i
    # return s
    return n*n

if __name__=="__main__":
    # t1 = time.time()
    # p = Pool()
    # res = p.map(fun,range(10000))
    # p.close()
    # p.join()
    # print("Pool tooks: ",time.time()-t1)

    # t2 = time.time()
    # res = []
    # for i in range(10000):
    #     res.append(fun(i))
    # print("Serial Processing took ",time.time()-t2)

    p = Pool(3)
    res = p.map(fun,[1,2,3,4,5])
    for i in res:
        print(i)