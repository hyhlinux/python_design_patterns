#coding:utf-8
# link data <---> view

from quotemodel import QuotesModel
from quoteview import QuoteTerminalView

class QuoteController(object):
	"""docstring for QuoteController"""
	def __init__(self):
		self.view = QuoteTerminalView()
		self.model = QuotesModel()

	def run(self):
		valid_input = False
		while not valid_input:
			n = self.view.select_quote()
			try:
				n = int(n)
			except ValueError as err:
				self.view.error('Incorrect index "{}"'.format(n))
			else:
				valid_input = True
		quote = self.model.get_quote(n)
		self.view.show(quote)	
		
def main():
	controller = QuoteController()
	controller.run()
		    
if __name__ == '__main__':
	main()