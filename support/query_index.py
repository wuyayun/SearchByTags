import os, collections

class queryIndex:
    def __init__(self):
        self.universe = set()
        self.invertedIndex = collections.defaultdict(lambda: collections.defaultdict(list))
        self.query = ''
        self.errorOutput = []
    def loadIndex(self, listLength, invertedIndex):
        self.universe = set(range(listLength))
        self.invertedIndex = collections.defaultdict(lambda: collections.defaultdict(list))
        self.invertedIndex.update((key, collections.defaultdict(list, value)) for key, value in invertedIndex.items())
    def __oneTag(self):
        end = self.query.find('|')
        if end == -1:
            self.errorOutput.append('error: invalid tag: missing \'|\'')
            return set()
        tagsNamespace = self.query[0:end].rstrip()
        self.query = self.query[end+1:].lstrip()
        end = self.query.find('>')
        if end == -1:
            self.errorOutput.append('error: invalid tag: missing \'>\'')
            return set()
        tag = self.query[0:end].rstrip()
        self.query = self.query[end+1:].lstrip()
        result = self.invertedIndex[tagsNamespace][tag]
        if len(result) == 0:
            self.errorOutput.append('warning: no item has tag <{}|{}>'.format(tagsNamespace, tag))
        return result
    def __operator(self):
        if self.query == '':
            self.errorOutput.append('error: unexpected end')
            return set()
        elif self.query[0] == '<':
            self.query = self.query[1:].lstrip()
            return self.__oneTag()
        elif self.query[0] == '(':
            self.query = self.query[1:].lstrip()
            return self.__brackets()
        else:
            self.errorOutput.append('error: unexpected symbol at {}'.format(self.query))
            return set()
    def __brackets(self):
        result = self.universe
        while self.query:
            if self.query[0] == ')':
                self.query = self.query[1:].lstrip()
                return result
            #logical AND: default for joining
            elif self.query[0] == '<':
                self.query = self.query[1:].lstrip()
                result = result.intersection(self.__oneTag())
            elif self.query[0] == '(':
                self.query = self.query[1:].lstrip()
                result = result.intersection(self.__brackets())
            #logical AND: 'and' or '&'
            elif self.query[0:3].lower() == 'and':
                self.query = self.query[3:].lstrip()
                result = result.intersection(self.__operator())
            elif self.query[0] == '&':
                self.query = self.query[1:].lstrip()
                result = result.intersection(self.__operator())
            #logical OR: 'or' or '|'
            elif self.query[0:2].lower() == 'or':
                self.query = self.query[2:].lstrip()
                result = result.union(self.__operator())
            elif self.query[0] == '|':
                self.query = self.query[1:].lstrip()
                result = result.union(self.__operator())
            #logical NOT: 'not' or '-'
            elif self.query[0:3].lower() == 'not':
                self.query = self.query[3:].lstrip()
                result = result.difference(self.__operator())
            elif self.query[0] == '-':
                self.query = self.query[1:].lstrip()
                result = result.difference(self.__operator())
            else:
                self.errorOutput.append('error: unexpected symbol at {}'.format(self.query))
                return set()
        self.errorOutput.append('error: unexpected end')
        return set()
    def startQuery(self, query):
        self.errorOutput = []
        self.query = query.strip() + ')'
        result = self.__brackets()
        if len(result) == 0:
            self.errorOutput.append('warning: no result')
        elif self.query:
            self.errorOutput.append('warning: unmatched right bracket before {}'.format(self.query))
        return result
