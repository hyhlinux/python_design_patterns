#coding:utf-8
#show data

class QuoteTerminalView(object):
	"""docstring for QuoteTerminalView"""
	def show(self, quote):
		print('And the quote is :"{}"'.format(quote))

	def error(self, msg):
		print('Error :{}'.format(msg))

	def select_quote(self):
		return input('whic quote number would you like to see?')


def test():
	view = QuoteTerminalView()
	print'-'*20
	view.show('为你写诗')
	view.error('为你写诗')
	view.select_quote()
	pass

if __name__ == '__main__':
	test()
