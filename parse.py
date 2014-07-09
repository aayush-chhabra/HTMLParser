from HTMLParser import HTMLParser


fileToRead = open('index.html', 'r')
fileContent = fileToRead.read()


class MyHTMLParser(HTMLParser):
	fileContentData = ""
	def handle_starttag(self, tag, attrs):
		#print "Encountered a start tag:", tag
		print "Got a start Tag"
	def handle_endtag(self, tag):
		#print "Encountered an end tag :", tag
		print "Got a end Tag"
	def handle_data(self, data):
		#print "Encountered some data  :", data
		data = data.strip()
		self.fileContentData += data + "\n";
		#print "In here"


parser = MyHTMLParser()
parser.feed(fileContent)
#print "Hello"
#print parser.fileContentData

fileToWrite = open('dataFile.txt','w')
fileToWrite.write(parser.fileContentData)