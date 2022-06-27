from textx import metamodel_from_file
import sys

from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

# tabela simbola


class TS_Element(object):
	name=""
	type=""
	param_num=0

	def __init__(self, name, type, param_num):
		self.name = name
		self.type = type
		self.param_num = param_num


class SymbolsTable(object):
	elements = []
	
	def __init__(self):
		self.elements = []


	def add_element(self, name, type, param_num):
		el = TS_Element(name, type, param_num)
		self.elements.append(el)
		print(Fore.GREEN + "Added {type} {name} to table of symbols".format(type=type, name=name));

	def name_exists(self, name, type):
		for el in self.elements:
			if el.name == name and el.type == type: return True

		return False

	def get_type(self, name):
		for i in range(len(self.elements)):
			if (self.elements[i].name == name):
				return self.elements[i].type
		return null

	def get_param_num(self, name):
		for i in range(len(self.elements)):
			if (self.elements[i].name == name):
				return self.elements[i].param_num
		return None


table_of_symbols = SymbolsTable()

# funk za proveru jel string broj

def is_number(string):
	try:
		float(string)
		return True
	except ValueError:
		return False;
	except TypeError:
		return False;

# klase za model

class VariableDeclaration(object):
	name=""

	def __init__(self, name):
		self.name = name

	def inspect(self):
		if table_of_symbols.name_exists(self.name, "variable"):
			print(Fore.YELLOW + "INFO: Varable {var} is already declared!".format(var=self.name));
		else:
			table_of_symbols.add_element(self.name, "variable", 0)

class Increment(object):
	name = ''

	def __init__(self, name):
		self.name = name

	def inspect(self):
		if table_of_symbols.name_exists(self.name, "variable") == False:
			print(Fore.RED + "ERROR: Variable in increment {name} is not declared!".format(name=self.name));

class Expression(object):
	name=""
	
	def __init__(self, name):
	 	self.name = name

	def inspect(self):
		if is_number(self.name):
			pass
		elif isinstance(self.name, str) == False :
			if is_number(self.name.name):
				pass
			elif isinstance(self.name.name, str) == False:
				if table_of_symbols.name_exists(self.name.name.name, "function") == False and table_of_symbols.name_exists(self.name.name.name, "variable") == False:
					print(Fore.RED + "ERROR: {name} not declared!".format(name=self.name.name.name))
			elif table_of_symbols.name_exists(self.name.name, "function") == False and table_of_symbols.name_exists(self.name.name, "variable") == False:
				print(Fore.RED + "ERROR: {name} not declared!".format(name=self.name.name))
		elif isinstance(self.name, str) == True :
			if table_of_symbols.name_exists(self.name, "function") == False and table_of_symbols.name_exists(self.name, "variable") == False:
				print(Fore.RED + "ERROR: {name} not declared!".format(name=self.name))

class FunctionCall(object):
	name=''
	args = []

	def __init__(self, name, args):
		self.name = name
		self.args= args

	def inspect(self):
		if table_of_symbols.name_exists(self.name, "function") == False:
			print(Fore.RED + "ERROR: Function {name} does not exits!".format(name=self.name))
		if table_of_symbols.get_param_num(self.name) != len(self.args):
			print(Fore.RED + "ERROR: Invalid param number!")

class FunctionBody(object):
	statements=""

	def __init__(self, statements):
		self.statements = statements

	def inspect(self):
		pass

class FunctionDeclaration(object):
	name=""
	args=""
	body=""

	def __init__(self, name, args, body):
		self.name = name
		self.args = args
		self.body = FunctionBody(body)

	def inspect(self):
		if table_of_symbols.name_exists(self.name, "function"):
			print(Fore.RED + "ERROR: Function already declared!");
		else:
			table_of_symbols.add_element(self.name, "function", len(self.args))

		for arg in self.args:
			if table_of_symbols.name_exists(arg, "variable"):
				print(Fore.YELLOW + "INFO: Varable {var} is already declared!".format(var=arg));
			else:
				table_of_symbols.add_element(arg, "variable", 0)

		# self.body.inspect()


# funkcije za proveru semantike

def numerical_expression_processor(exp):
	ex1 = Expression(exp.exp1)
	ex1.inspect()

	if(exp.exp2 != None):
		ex2 = Expression(exp.exp2)
		ex2.inspect()

def expression_processor(expression):
	ex = Expression(expression.name)
	ex.inspect()

def function_declaration_processor(function):
	func_decl = FunctionDeclaration(function.name, function.add_params, function.body)
	func_decl.inspect()


def variable_declaration_processor(variable):
	var = VariableDeclaration(variable.name)
	var.inspect()

def function_call_processor(function):
	f = FunctionCall(function.name, function.params)
	f.inspect()

def increment_processor(increment):
	inc = Increment(increment.name)
	inc.inspect()

my_metamodel = metamodel_from_file('parser.tx')
my_metamodel.register_obj_processors({'FunctionDeclaration': function_declaration_processor,
									'VariableDeclaration': variable_declaration_processor,
									'IncrementStatement': increment_processor,
									'Expression': expression_processor,
									"NumericalExpression" : numerical_expression_processor,
									'FunctionCall': function_call_processor})


my_model = my_metamodel.model_from_file(sys.argv[1])
