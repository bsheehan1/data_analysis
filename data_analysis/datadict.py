class DataDict:
    def __init__(self,fp):
        f = open(fp)
        s = f.read().split('\n')
        self.keys = s[0].split('\t')
        self.raw = s[1:]
        self.array = []
        for s in self.raw:
            x = s.split('\t')
            self.array.append(x)
        self.dictionary = {}
        for i in range(len(self.keys)):
            l = []
            for x in self.array:
                l.append(x[i])
            self.dictionary[self.keys[i]] = l
        print(self.dictionary)
        f.close()

    


if __name__ == '__main__':
    x = DataDict('/Users/bksheehan/Desktop/data_dict.txt')
