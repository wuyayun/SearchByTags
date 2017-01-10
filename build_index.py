import os, collections, json

contentDir = '.'
tagsFileName = 'tags.txt'
indexDir = 'support/index'

class buildIndex:
    def __init__(self):
        self.infoList = []
        self.forwardIndex = []
        self.invertedIndex = collections.defaultdict(lambda: collections.defaultdict(list))
    def __readTags(self, ID, tagsNamespace, tagsFile):
        line = tagsFile.readline()
        while line and line.lstrip()[0] != '<':
            tags = line.split('|')
            for tag in tags:
                self.forwardIndex[ID][tagsNamespace].append(tag.strip())
                self.invertedIndex[tagsNamespace][tag.strip()].append(ID)
            line = tagsFile.readline()
        return line
    def __readTitle(self, info, tagsFile):
        line = tagsFile.readline()
        while line and line.lstrip()[0] != '<':
            info['title'] = line.strip()
            line = tagsFile.readline()
        return line
    def __readImages(self, info, path, tagsFile):
        line = tagsFile.readline()
        while line and line.lstrip()[0] != '<':
            info['images'].append(os.path.join(path, line.strip()))
            line = tagsFile.readline()
        return line
    def __readDescriptions(self, info, tagsFile):
        line = tagsFile.readline()
        while line and line.lstrip()[0] != '<':
            info['descriptions'].append(line.strip())
            line = tagsFile.readline()
        return line
    def parseOneTagsFile(self, path, tagsFile):
        info = {'path': path, 'title': path, 'images': [], 'descriptions': []}
        
        ID = len(self.infoList)
        self.forwardIndex.append(collections.defaultdict(list))
        
        line = tagsFile.readline()
        while line:
            line = line.strip()
            if line[0:5].lower() == '<tag>':
                tagsNamespace = line[5:].lstrip()
                line = self.__readTags(ID, tagsNamespace, tagsFile)
            elif line[0:6].lower() == '<tags>':
                tagsNamespace = line[6:].lstrip()
                line = self.__readTags(ID, tagsNamespace, tagsFile)
            elif line.lower() == '<title>':
                line = self.__readTitle(info, tagsFile)
            elif line.lower() == '<image>' or line.lower() == '<images>':
                line = self.__readImages(info, path, tagsFile)
            elif line.lower() == '<description>' or line.lower() == '<descriptions>':
                line = self.__readDescriptions(info, tagsFile)
            else:
                line = tagsFile.readline()
        
        self.infoList.append(info)
    def parseAllTagsFiles(self, root, filename):
        for path, subdirList, fileList in os.walk(root):
            if filename in fileList:
                tagsFile = open(os.path.join(path, filename), 'r')
                self.parseOneTagsFile(path, tagsFile)
                tagsFile.close()
    def saveIndex(self, saveDir):
        f = open(os.path.join(saveDir, 'infoList'), 'w')
        json.dump(self.infoList, f)
        f.close()
        f = open(os.path.join(saveDir, 'forwardIndex'), 'w')
        json.dump(self.forwardIndex, f)
        f.close()
        f = open(os.path.join(saveDir, 'invertedIndex'), 'w')
        json.dump(self.invertedIndex, f)
        f.close()

def main():
    i = buildIndex()
    i.parseAllTagsFiles(contentDir, tagsFileName)
    i.saveIndex(indexDir)

if __name__ == '__main__':
    main()
