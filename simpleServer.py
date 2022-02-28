import bottle
from bottle import Bottle, run, template, static_file
from io import StringIO
from os import listdir
from os.path import exists, dirname, isfile, join
from contextlib import redirect_stdout

class Global:
	Path = dirname(__file__)
	@staticmethod
	def Pages():
		return [f for f in listdir(Global.Path) if isfile(join(Global.Path, f)) and f.startswith('page_')]

class HTMLTemplate:
	Default = {
		'title': 'My App',

		# Either None or a list of stylesheet filenames
		'css': ['base.css','test.css'],

		# Either None or a list of javascript filenames
		'javascript': ['test.js'],
		# The route "/page/<pagename>" will do the following:
		# 1. Execute the python file "page_<pagename>.py", which must be in the same folder as simpleServer.py
		# 2. Any output from "page_<pagename>.py" is captured and fed into content. Full HTML is accepted.
		#
		# The route "/" will display the default content set here.
		'content': '<main>' +
			'<h2>Welcome to SimpleServer Framework</h2>' +
			'Navigate to: <ul>' + ''.join(['<li><a href="/page/{0}">{0}</a></li>'.format(str[5:-3]) for str in Global.Pages()]) + '</ul>' +
			'</main>'
	}
	Name = 'html.tpl'
	@staticmethod
	def Values(**values):
		for key in HTMLTemplate.Default.keys():
			if not key in values:
				values[key] = HTMLTemplate.Default[key]
		return values

class PagePipeline:
	def __init__(self, pagename):
		self.error = False
		self.pagePathName = Global.Path + '/page_' + pagename + '.py'
		if not exists(self.pagePathName):
			self.error = True
	def run(self):
		if self.error:
			return 'The page: {}, does not exist.'.format(self.pagePathName)
		else:
			output = StringIO()
			with redirect_stdout(output):
				with open(self.pagePathName) as file:
					exec(file.read())
			return output.getvalue()

class App:
	# Should not need to change this.
	Host = 'localhost'

	# Port may need to be changed if port 8082 is already used. Just pick some other number, say 8083
	Port = 8082

	# Debug=True will causes templates to be rebuilt on each page load.
	Debug = True

	Path = {
		'local': Global.Path,
		'css': Global.Path + '/css',
		'javascript': Global.Path + '/javascript',
		'views': Global.Path + '/views'
	}
	
	Pages = [f for f in listdir(Global.Path) if isfile(join(Global.Path, f)) and f.startswith('page_')]

	def __init__(self):
		bottle.TEMPLATE_PATH.insert(0,App.Path['views'])
		self.app = Bottle()
	def run(self):
		@self.app.route('/')
		def home_route():
			return template(HTMLTemplate.Name, HTMLTemplate.Values())

		@self.app.route('/css/<filename>')
		def css_static(filename):
			return static_file(filename, root=App.Path['css'])

		@self.app.route('/javascript/<filename>')
		def javascript_static(filename):
			return static_file(filename, root=App.Path['javascript'])

		@self.app.route('/page/<pagename>')
		def page_route(pagename):
			path = HTMLTemplate.Name
			return template(path, HTMLTemplate.Values(content = PagePipeline(pagename).run()))

		self.app.run(host=App.Host, port=App.Port, debug=App.Debug)

App().run()