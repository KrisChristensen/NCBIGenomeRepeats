##########################################################
### Import Necessary Modules

import argparse		               #provides options at the command line
import sys		               #take command line arguments and uses it in the script
import gzip		               #allows gzipped files to be read
import re		               #allows regular expressions to be used

##########################################################
### Command-line Arguments
parser = argparse.ArgumentParser(description="A script to count the number of lowercase in a fasta file for defined windows, returns percent in window")
parser.add_argument("-file", help = "The location of the fasta (accepts .gz format)", default=sys.stdin, required=True)
parser.add_argument("-win", help = "The size of the window to use, default = 100000", default=100000)
args = parser.parse_args()

#########################################################
### Open file (object-oriented programming)

class OpenFile(): 
    ### Opens the file and either directs it to an appropriate line-reader
    def __init__ (self, filename, fileType):
        if re.search(".gz$", filename):
            self.filename = gzip.open(filename, 'rb')
        else:
            self.filename = open(filename, 'r')             
        if fileType == "fasta":
            self.readLinesFasta(self.filename)

    ### Reads the fasta file
    def readLinesFasta(self, f):
        self.header = "NA"
        self.seq = []
        for self.line in f:
            try:
                self.line = self.line.decode('utf-8')
            except:
                pass     
            self.line = self.line.rstrip('\n')
            if re.search("^\>", self.line):
                if self.header == "NA":
                    self.header = self.line[1:].split()[0]
                else:
                    self.histogram(self.seq, self.header)
                    del self.seq[:]
                    self.header = self.line[1:].split()[0]
            elif re.search("\w", self.line):
                self.seq.append(self.line)
        self.histogram(self.seq, self.header)

    ### Finds the number of lowercase's in a sequence
    def histogram(self, seq, head):
        sys.stderr.write("\tAnalyzing: {}\n".format(head))
        self.sequence = "".join(seq)
        for self.window in range(0, len(self.sequence), int(args.win)):
            if int(self.window) + int(args.win) > len(self.sequence):
                self.end = len(self.sequence)
            else:
                self.end = int(self.window) + int(args.win)
            self.subSeq = self.sequence[int(self.window):int(self.end)]
            self.lcCount = self.n_lower_chars(self.subSeq)
            self.lcPercent = float(self.lcCount)/len(self.subSeq)
            print ("{}\t{}\t{}\t{}".format(head, self.window + 1, self.end, self.lcPercent, self.subSeq))
            #print ("\thead:{} start:{} end:{} per:{} seq:{}".format(head, self.window + 1, self.end, self.lcPercent, self.subSeq))

    ###From https://stackoverflow.com/questions/10953189/count-lower-case-characters-in-a-string            
    def n_lower_chars(self, string):
        return sum(1 for c in string if c.islower())

            

if __name__ == '__main__':            
    open_fasta = OpenFile(args.file, "fasta")
