def create_small_set(fname, out_name):
    k = 0
    out = open(out_name, 'w+')
    with open(fname) as f:
        for i, l in enumerate(f):
            if k < 5000:            
                out.write(l)
                k += 1
            else:
                out.close()
                break

create_small_set('orig_train.csv', 'train.csv')
create_small_set('orig_test.csv', 'test.csv')
