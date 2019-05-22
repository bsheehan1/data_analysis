class DataStruct:
    def __init__(self,fp):
        f = open(fp)
        s = f.read().split('\n')
        self.keys = s[0].split('\t')
        self.raw = s[1:]
        self.array = []
        self.x = []
        self.y = []
        for s in self.raw:
            v = s.split('\t')
            if len(v) > 1:
                self.array.append(v)
                self.x.append(v[:-1])
                self.y.append(v[-1])
        self.dictionary = {}
        for i in range(len(self.keys)):
            l = []
            for x in self.array:
                l.append(x[i])
            self.dictionary[self.keys[i]] = l
        f.close()

    


if __name__ == '__main__':
    a = DataStruct('./test/data_dict.txt')
    b = DataStruct('./test/mlr.txt')
