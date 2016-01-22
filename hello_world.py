import bottle

@bottle.route('/')
def home_page():
	mythings = ['red', 'blue', 'green', 'purple']
	return bottle.template('hello_world', username='Perry', things=mythings)
	# return 'hello_world\n'

@bottle.route('/testpage')
def test_page():
	return 'this is a test page'

bottle.debug(True)
bottle.run(host='localhost', port=8081)

