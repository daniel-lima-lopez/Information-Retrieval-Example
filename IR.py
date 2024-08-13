# libraies importation
import pandas as pd

class Searcher:
    def __init__(self, data_path='shortjokes.csv', postings_path='postings.txt'):
        # jokes data
        self.data = pd.read_csv(data_path)
        self.jokes = self.data['Joke']
        
        # postings information
        self.postings = {} # empty dictionary
        with open(postings_path, 'r') as t:
            lines = t.readlines()
            for li in lines:
                key = li.split(' ')[0]
                inds = li.split(' ')[1]

                auxs = set()
                for id in inds.split(','):
                    auxs.add(int(id))
                self.postings[key] = auxs
        
        # auxiliary set containing all indices
        self.all_set = set()
        for i in range(len(self.jokes)):
            self.all_set.add(i)

    # genereates not token sets
    def get_not(self, token):
        posting = self.postings[token]
        return self.all_set-posting # sets difference operation

    # returns the indexes resulting from a command
    def filter(self, command):
        split = command.split(' ') # split in words
        out_set = set() # empty set
        i = 0 # word's pointer
        while i<len(split): # while theres is still words on command
            #identify next operation
            if i==0: # the first operation is the union of an empty set and the first set on the command
                next_op = 'or'
            else:
                next_op = split[i]
                i += 1
            
            # identify next set
            if split[i]=='not':
                next_set = self.get_not(split[i+1]) # get negation set
                i += 2
            else:
                next_set = self.postings[split[i]] # set of posting for the token
                i += 1
            
            # perform set operations
            if next_op == 'and':
                out_set = out_set & next_set
            elif next_op == 'or':
                out_set = out_set | next_set

        return out_set
    
    # returns a list of jokes in a set of indexes
    def get_jokes(self, ids): 
        outs = [self.jokes[i] for i in ids]
        return outs
    

if __name__=='__main__':
    test = Searcher() # instantiate the Searcher class
    command = input('Enter a valid command: ') # command
    #command = 'people and danger'
    inds = test.filter(command) # indexes resulting from the input command
    jokes = test.get_jokes(inds)

    print('Results:')
    for ji in jokes:
        print(f' - {ji}')