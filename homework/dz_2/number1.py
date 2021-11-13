import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--str1', dest='str1', type=str)
    parser.add_argument('--str2', dest='str2', type=str)
    res = []
    k = 1
    tr_fl = False
    for i, element in enumerate('str1'):
        if tr_fl:
            if k > len('str2') - 1:
                tr_fl = False
                k = 1
            elif element == 'str2'[k]:
                k += 1
            elif element != 'str2'[k]:
                res = res[:-1]
                k = 1
                tr_fl = False
        if not tr_fl:
            tr_fl = True
            res.append(i)
    for r in res:
        print(str(r))
