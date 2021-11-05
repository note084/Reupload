#include "syntaxAnalyzer.h"

void SyntaxAnalyzer::Analyze()
{
	Rat19F();
	output << "Syntax Analysis Successful." << std::endl
		   << std::endl;
	output << this->symbolTable.list();
	output << std::endl;
	output << this->symbolTable.list_instr();
}

void SyntaxAnalyzer::Rat19F()
{
	if (print)
	{
		printCurrentToken();
		output << "\t<Rat19F> -> %% <Opt Declaration List> <Statement List> %%" << std::endl;
	}
	OptFunctionDefinitions();

	if (currentToken.lexeme == "%%")
	{

		getNextToken();
		OptDeclarationList();
		StatementList();
	}

	if (currentToken.lexeme != "%%")
	{
		throw SyntaxError("Expected '%%'.", currentToken.lineNumber);
	}
	if (print)
	{
		output << "\t<Opt Function Definitions> ->  <Function>" << std::endl;
		output << "\t<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>" << std::endl;
	}
}

void SyntaxAnalyzer::OptFunctionDefinitions()
{
	if (print)
	{
		output << "\t<Opt Function Definitions> -> <Function Definitions> | <Empty>" << std::endl;
	}

	if (currentToken.lexeme == "function")
	{
		if (print)
		{	
			output << "\t<Opt Function Definitions> -> <Function Definitions>" << std::endl;
		}
		FunctionDefinitions();
	}
	else
	{
		if (print)
		{	
			output << "\t<Opt Function Definitions> -> <Empty>" << std::endl;
		}
		Empty();
	}
}

void SyntaxAnalyzer::FunctionDefinitions()
{
	if (print)
	{
		output << "\t<Function Definitions> -> <Function> | <Function> <Function Definitions>" << std::endl;
	}

	Function();

	if (currentToken.lexeme == "function")
	{
		if (print)
		{
			output << "\t<Opt Function Definitions> -> <Function> <Function Definitions>" << std::endl;
		}
		FunctionDefinitions();
	}
}

void SyntaxAnalyzer::Function()
{	
	
	if (print)
	{
		output << "\t<Opt Function Definitions> ->  <Function>" << std::endl;
		output << "\t<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>" << std::endl;
	}
	getNextToken();
	Identifier();
	getNextToken();
	if (currentToken.lexeme != "(")
	{
		throw SyntaxError("Expected '('", currentToken.lineNumber);
	}

	getNextToken();

	OptParameterList();
	if (currentToken.lexeme != ")")
	{
		throw SyntaxError("Expected ')'", currentToken.lineNumber);
	}

	getNextToken();
	OptDeclarationList();
	Body();
}

void SyntaxAnalyzer::OptParameterList()
{
	if (print)
	{
		output << "\t<Opt Parameter List> -> <ParameterList> | <Empty>" << std::endl;
	}

	if (currentToken.lexeme == ")")
	{
		if (print)
		{
			output << "\t<Opt Parameter List> -> <Empty>" << std::endl;
		}
		Empty();
	}
	else if (currentToken.token == "Identifier")
	{
		if (print)
		{
			output << "\t<Opt Parameter List> -> <ParameterList>" << std::endl;
		}
		ParameterList();
	}
	else
	{
		throw SyntaxError("Expected ')' or identifier", currentToken.lineNumber);
	}
}

void SyntaxAnalyzer::ParameterList()
{
	if (print)
	{
		output << "\t<ParameterList> -> <Parameter> | <Parameter> , <Parameter List>" << std::endl;
	}
	
	Parameter();


	if (currentToken.lexeme == ",")
	{

		getNextToken();
		ParameterList();
	}
}

void SyntaxAnalyzer::Parameter()
{
	if (print)
	{
		output << "\t<ParameterList> -> <Parameter>" << std::endl;
		output << "\t<Parameter> -> <IDs> <Qualifier>" << std::endl;
	}

	IDs();
	Qualifier();
	getNextToken();
}

void SyntaxAnalyzer::Qualifier()
{
	if (print)
	{
		output << "\t<Qualifier> -> int | boolean | real" << std::endl;
	}
}

void SyntaxAnalyzer::Body()
{
	if (print)
	{
		output << "\t<Body> -> { <StatementList> }" << std::endl;
	}
	
	if (currentToken.lexeme != "{")
	{
		throw SyntaxError("Expected '{'", currentToken.lineNumber);
	}

	getNextToken();

	StatementList();
	if (currentToken.lexeme != "}")
	{
		throw SyntaxError("Expected '}'", currentToken.lineNumber);
	}

	getNextToken();
}

void SyntaxAnalyzer::OptDeclarationList()
{
	if (print)
		{
			output << "\t<Opt Declaration List> -> <Declaration List> | <Empty>" << std::endl;
		}

	if (currentToken.lexeme == "real" | currentToken.lexeme == "boolean" | currentToken.lexeme == "int")
	{
		if (print)
		{
			output << "\t<Opt Declaration List> -> Declaration List>" << std::endl;
		}
		DeclarationList();
	}
	else
	{
		if (print)
		{
			output << "\t<Opt Declaration List> -> <Empty>" << std::endl;
		}
	}
	
}

void SyntaxAnalyzer::DeclarationList()
{
	if (print)
	{
		output << "\t<Opt Declaration List> -> <Declaration>\n";
	}

	savedType = new std::string(currentToken.lexeme);

	this->isDeclaration = true;
	Declaration();

	if (currentToken.lexeme == ";")
	{
		symbolTable.pop_typestack();
		getNextToken();
		if (currentToken.lexeme == "real" | currentToken.lexeme == "boolean" | currentToken.lexeme == "int")
		{
			DeclarationList();
		}
		else
		{
			if (print)
			{
				output << "\t<Opt Declaration List> -> <Empty>\n";
			}
		}
		
	}
	this->isDeclaration = false;

}

void SyntaxAnalyzer::Declaration()
{
	if (print)
	{
		output << "\t<Declaration> -> <Qualifier> <IDs>" << std::endl;
	}
	Qualifier();
	getNextToken();
	if (currentToken.token == "Identifier")
	{
		if (print)
		{
			output << "\t<Declaration> -> <IDs>" << std::endl;
		}
		IDs();
	}
}

void SyntaxAnalyzer::IDs()
{
	if (print)
	{
		output << "\t<IDs> -> <Identifier> | <Identifier>, <IDs>" << std::endl;
	}

	if (isDeclaration)
	{
		if (!symbolTable.lookup(currentToken))
		{
			symbolTable.insert(currentToken, *savedType);
		}
		else
		{
			error(DUPLICATE_SYMBOL, currentToken.lineNumber, currentToken.lexeme);
		}
	}
	
	Identifier();
	getNextToken();

	if (currentToken.lexeme == ",")
	{
		getNextToken();
		if (currentToken.token == "Identifier")
		{
			IDs();
		}
		else
		{
			throw SyntaxError("Expected identifier", currentToken.lineNumber);
		}
	}
}

void SyntaxAnalyzer::StatementList()
{
	if (print)
	{	
		output << "\t<Statement List> -> <Statement> | <Statement> <Statement List>" << std::endl;
	}

	Statement();

	if (currentToken.lexeme == "get" | currentToken.lexeme == "put" | currentToken.lexeme == "while" | currentToken.lexeme == "if" |
		currentToken.lexeme == "return" | currentToken.token == "Identifier")
	{
		StatementList();
	}
}

void SyntaxAnalyzer::Statement()
{
	
	if (currentToken.lexeme == "{")
	{
		if (print)
		{	
			output << "\t<Statement List> -> <Statement>" << std::endl;
		}
		getNextToken();
		Compound();
	}
	else if (currentToken.token == "Identifier")
	{
		if (print)
		{
			output << "\t<Statement List> -> <Statement>" << std::endl;
			output << "\t<Statement> -> <Assign>" << std::endl;
		}
		Assign();
	}
	else if (currentToken.lexeme == "if")
	{
		if (print)
		{
			output << "\t<Statement List> -> <Statement>" << std::endl;
			output << "\t<Statement> -> <If>" << std::endl;
		}
		getNextToken();
		If();
	}
	else if (currentToken.lexeme == "return")
	{
		if (print)
		{
			output << "\t<Statement List> -> <Statement>" << std::endl;
			output << "\t<Statement> -> <Return>" << std::endl;
		}
		Return();
	}
	else if (currentToken.lexeme == "put")
	{
		if (print)
		{
			output << "\t<Statement List> -> <Statement>" << std::endl;
			output << "\t<Statement> -> <Print>" << std::endl;
		}
		Print();
	}
	else if (currentToken.lexeme == "get")
	{
		if (print)
		{
			output << "\t<Statement List> -> <Statement>" << std::endl;
			output << "\t<Statement> -> <Scan>" << std::endl;
		}
		getNextToken();
		Scan();
	}
	else if (currentToken.lexeme == "while")
	{
		if (print)
		{
			output << "\t<Statement List> -> <Statement>" << std::endl;
			output << "\t<Statement> -> <While>" << std::endl;
		}
		getNextToken();
		While();
	}
	else
	{
		throw SyntaxError("Expected '{', identifier or keyword", currentToken.lineNumber);
	}
}

void SyntaxAnalyzer::Compound()
{
	
	if (print)
	{
		output << "\t<Statement> -> <Compound>" << std::endl;
		output << "\t <Compound> -> { <Statement List> }" << std::endl;
	}

	StatementList();


	if (currentToken.lexeme != "}")
	{
		throw SyntaxError("Expected '}'", currentToken.lineNumber);
	}
	getNextToken();
}

void SyntaxAnalyzer::Assign()
{
	if (print)
	{
		output << "\t<Assign> -> <Identifier> = <Expression> ;" << std::endl;
	}
	Identifier();

	*save = currentToken;
	std::string type = symbolTable.get_type(*save);
	if (type == "")
	{
		error(UNDECLARED_VARIABLE, currentToken.lineNumber, currentToken.lexeme);
		this->assign = true;
	}
	else
	{
		symbolTable.push_typestack(symbolTable.get_type(*save));
	}
	getNextToken();

	if (currentToken.lexeme != "=")
	{
		throw SyntaxError("Expected '='", currentToken.lineNumber);
	}

	getNextToken();
	Expression();

	symbolTable.gen_instr("POPM", symbolTable.get_address(*save));

	if (currentToken.lexeme != ";")
	{
		throw SyntaxError("Expected ';'", currentToken.lineNumber);
	}
	else
	{
		if (print)
		output << "\t<Expression> -> e;" << std::endl;
		
	}
	
	symbolTable.pop_typestack();
	getNextToken();
}

void SyntaxAnalyzer::If()
{
	if (print)
	{
		output << "\t<If> -> if ( <Condition> ) <Statement> fi | if ( <Condition> ) <Statement> otherwise <Statement> fi" << std::endl;
	}

	if (currentToken.lexeme != "(")
	{
		throw SyntaxError("Expected '('", currentToken.lineNumber);
	}

	getNextToken();

	Condition();

	if (currentToken.lexeme != ")")
	{
		throw SyntaxError("Expected ')'", currentToken.lineNumber);
	}

	getNextToken();

	Statement();

	if (currentToken.lexeme == "otherwise")
	{
		getNextToken();
		Statement();
	}

	if (currentToken.lexeme != "fi")
	{
		throw SyntaxError("Expected 'fi' keyword", currentToken.lineNumber);
	}
	symbolTable.back_patch(symbolTable.get_instr_address());

	getNextToken();
}

void SyntaxAnalyzer::Return()
{
	if(print)
	{
		output << "\t<Return> -> return ; | return <Expression> ;" << std::endl;
	}
	getNextToken();

	if (currentToken.lexeme != ";")
	{
		if (print)
		{
			output << "\t<Return> -> return <Expression> ;" << std::endl;
		}
		Expression();
	}
	else
	{
		if (print)
		{
			output << "\t<Return> -> return ;" << std::endl;
		}
	}
	getNextToken();
}

void SyntaxAnalyzer::Print()
{
	if (print)
	{
		output << "\t<Print> -> put ( <Expression> );" << std::endl;
	}
	getNextToken();

	if (currentToken.lexeme != "(")
	{
		throw SyntaxError("Expected '('", currentToken.lineNumber);
	}

	getNextToken();
	Expression();

	if (currentToken.lexeme != ")")
	{
		throw SyntaxError("Expected ')'", currentToken.lineNumber);
	}
	getNextToken();

	if (currentToken.lexeme != ";")
	{
		throw SyntaxError("Expected ';'", currentToken.lineNumber);
	}
	symbolTable.gen_instr("STDOUT", NIL);

	getNextToken();
}

void SyntaxAnalyzer::Scan()
{
	if (print)
	{
		output << "\t<Scan> -> get ( <IDs> );" << std::endl;
	}
	
	if (currentToken.lexeme != "(")
	{
		throw SyntaxError("Expected '('", currentToken.lineNumber);
	}

	getNextToken();
	symbolTable.gen_instr("STDIN", NIL);
	int addr = symbolTable.get_address(currentToken);
	symbolTable.gen_instr("POPM", addr);

	IDs();

	if (currentToken.lexeme != ")")
	{
		throw SyntaxError("Expected ')'", currentToken.lineNumber);
	}

	getNextToken();
	if (currentToken.lexeme != ";")
	{
		throw SyntaxError("Expected ';'", currentToken.lineNumber);
	}
	getNextToken();
}

void SyntaxAnalyzer::While()
{
	if (print)
	{
		output << "\t<While> -> while ( <Condition> ) <Statement>" << std::endl;
	}

	int addr = symbolTable.get_instr_address();
	symbolTable.gen_instr("LABEL", NIL);

	if (currentToken.lexeme != "(")
	{
		throw SyntaxError("Expected '('", currentToken.lineNumber);
	}
	getNextToken();

	Condition();

	if (currentToken.lexeme != ")")
	{
		throw SyntaxError("Expected ')'", currentToken.lineNumber);
	}
	getNextToken();
	Statement();
	symbolTable.gen_instr("JUMP", addr);
	symbolTable.back_patch(symbolTable.get_instr_address());
}

void SyntaxAnalyzer::Condition()
{
	if (print)
	{
		output << "\t<Condition> -> <Expression> <Relop> <Expression>" << std::endl;
	}

	savedType = new std::string(symbolTable.get_type(currentToken));

	if (*savedType == "")
	{
		error(UNDECLARED_VARIABLE, currentToken.lineNumber, currentToken.lexeme);
	}

	Expression();
	Relop();
	getNextToken();
	Expression();

	if (*savedOp == "<")
	{
		symbolTable.gen_instr("LES", NIL);
	}
	else if (*savedOp == ">")
	{
		symbolTable.gen_instr("GRT", NIL);
	}
	else if (*savedOp == "==")
	{
		symbolTable.gen_instr("EQU", NIL);
	}
	else if (*savedOp == "^=")
	{
		symbolTable.gen_instr("NEQ", NIL);
	}
	else if (*savedOp == "=>")
	{
		symbolTable.gen_instr("GEQ", NIL);
	}
	else if (*savedOp == "=<")
	{
		symbolTable.gen_instr("LEQ", NIL);
	}

	symbolTable.push_jumpstack(symbolTable.get_instr_address());
	symbolTable.gen_instr("JUMPZ", NIL);

}

void SyntaxAnalyzer::Relop()
{
	if (currentToken.lexeme == "==")
	{
		if (print)
		{
			output << "\t<Relop> -> ==" << std::endl;
		}
	}
	else if (currentToken.lexeme == "/=")
	{
		if (print)
		{
			output << "\t<Relop> -> /=" << std::endl;
		}
	}
	else if (currentToken.lexeme == ">")
	{
		if (print)
		{
			output << "\t<Relop> -> >" << std::endl;
		}
	}
	else if (currentToken.lexeme == "<")
	{
		if (print)
		{
			output << "\t<Relop> -> <" << std::endl;
		}
	}
	else if (currentToken.lexeme == "=>")
	{
		if (print)
		{
			output << "\t<Relop> -> =>" << std::endl;
		}
	}
	else if (currentToken.lexeme == "<=")
	{
		if (print)
		{
			output << "\t<Relop> -> <=" << std::endl;
		}
	}
	else
	{
		throw SyntaxError("Expected relational operator", currentToken.lineNumber);
	}

	this->savedOp = new std::string(currentToken.lexeme);
}

void SyntaxAnalyzer::Expression()
{

	if (print)
	{
		output << "\t<Expression> -> <Term>" << std::endl;
	}
	Term();
	if (currentToken.lexeme == "+")
	{
		if (print)
		{
			output << "\t<Expression> -> <Expression> + <Term>" << std::endl;
		}
		std::string op = currentToken.lexeme;
		getNextToken();
		Term();
		symbolTable.gen_instr("ADD", NIL);

		Expression();
	}
	else if (currentToken.lexeme == "-")
	{
		if (print)
		{
			output << "\t<Expression> -> <Expression> - <Term>" << std::endl;
		}
		std::string op = currentToken.lexeme;
		getNextToken();

		Term();
		symbolTable.gen_instr("SUB", NIL);

		Expression();
	}
}


void SyntaxAnalyzer::Term()
{	
	if (currentToken.lexeme == "*")
	{
		if (print)
		{
			output << "\t<Term> -> <Term> * <Factor>" << std::endl;
		}
		
		std::string op = currentToken.lexeme;
		symbolTable.gen_instr("MUL", NIL);
		getNextToken();
		Factor();
		Term();
	}
	else if(currentToken.lexeme == "/")
	{
		if (print)
		{
			output << "\t<Term> -> <Term> / <Factor>" << std::endl;
		}

		std::string op = currentToken.lexeme;
		symbolTable.gen_instr("DIV", NIL);
		getNextToken();
		Factor();
		Term();
	}
	else
	{
		if (print)
		{
			output << "\t<Term> -> <Factor>" << std::endl;
		}
		Factor();
		if (currentToken.lexeme == "*")
		{
			
			if (print)
			{
				output << "\t<Term> -> <Term> * <Factor>" << std::endl;
			}

			std::string op = currentToken.lexeme;
			symbolTable.gen_instr("MUL", NIL);
			getNextToken();
			Factor();
			Term();
		}
		else if(currentToken.lexeme == "/")
		{
			if (print)
			{
				output << "\t<Term> -> <Term> / <Factor>" << std::endl;
			}

			std::string op = currentToken.lexeme;
			symbolTable.gen_instr("DIV", NIL);
			getNextToken();
			Factor();
			Term();
		}
	}
	
	
}


void SyntaxAnalyzer::Factor()
{

	if (currentToken.lexeme == "-")
	{
		if (print)
		{
			output << "\t<Factor> -> - <Primary>" << std::endl;
		}
		getNextToken();
	} 
	else
	{
		if (print)
		{
			output << "\t<Factor> -> <Primary>" << std::endl;
		}
		Primary();
	}
}

void SyntaxAnalyzer::Primary()
{
	if (!symbolTable.typestack_empty() && symbolTable.top_typestack() == "")
	{
		symbolTable.pop_typestack();
	}

	if (currentToken.token == "Identifier")
	{
		if (print)
		{
			output << "\t<Primary> -> <Identifier>" << std::endl;
		}

		if (symbolTable.get_type(currentToken) == "")
		{
			if (!this->assign)
			{
				error(UNDECLARED_VARIABLE, currentToken.lineNumber, currentToken.lexeme);
			}
			this->assign = false;
		}

		if (symbolTable.typestack_empty())
		{
			if (symbolTable.get_type(currentToken) != "")
			{
				symbolTable.push_typestack(*savedType);
			}
		}
		else if (symbolTable.get_type(currentToken) == "")
		{
			// error(UNDECLARED_VARIABLE, currentToken.lineNumber, currentToken.lexeme);
		}
		else if ((symbolTable.get_type(currentToken) != symbolTable.top_typestack()) && symbolTable.top_typestack() != "")
		{
			error(TYPE_MISMATCH, currentToken.lineNumber, symbolTable.top_typestack());
		}

		Identifier();
		symbolTable.gen_instr("PUSHM", symbolTable.lookup(currentToken));
		getNextToken();
		
		if (currentToken.lexeme == "(")
		{
			if (print)
			{
				output << "\t<Primary> -> <Identifier> ( <IDs> )" << std::endl;
			}
			getNextToken();
			IDs();

			if (currentToken.lexeme != ")")
			{
				throw SyntaxError("Expected ')'", currentToken.lineNumber);
			}

			getNextToken();
		}
	}
	else if (currentToken.token == "Integer")
	{
		if (print)
		{
			output << "\t<Primary> -> <Integer>" << std::endl;
		}
		if (!symbolTable.typestack_empty() && symbolTable.top_typestack() != "int")
		{
			error(TYPE_MISMATCH, currentToken.lineNumber, symbolTable.top_typestack());
		}
		Integer();
		symbolTable.gen_instr("PUSHI", stoi(currentToken.lexeme));
		getNextToken();
	}
	else if (currentToken.lexeme == "(")
	{
		if (print)
		{
			output << "\t<Primary> -> ( <Expression> )" << std::endl;
		}
		getNextToken();

		Expression();

		if (currentToken.lexeme != ")")
		{
			throw SyntaxError("Expected ')'", currentToken.lineNumber);
		}
		getNextToken();
	}
	else if (currentToken.token == "Real")
	{
		if (print)
		{
			output << "\t<Primary> -> <Real>" << std::endl;
		}

		if (!symbolTable.typestack_empty() && symbolTable.top_typestack() != "real")
		{
			error(TYPE_MISMATCH, currentToken.lineNumber, symbolTable.top_typestack());
		}

		getNextToken();
	}
	else if (currentToken.lexeme == "true")
	{
		if (print)
		{
			output << "\t<Primary> -> true" << std::endl;
		}

		if (!symbolTable.typestack_empty() && symbolTable.top_typestack() != "boolean")
		{
			error(TYPE_MISMATCH, currentToken.lineNumber, symbolTable.top_typestack());
		}

		symbolTable.gen_instr("PUSHI", 1);

		getNextToken();
	}
	else if (currentToken.lexeme == "false")
	{
		if (print)
		{
			output << "\t<Primary> -> false" << std::endl;
		}

		if (!symbolTable.typestack_empty() && symbolTable.top_typestack() != "boolean")
		{
			error(TYPE_MISMATCH, currentToken.lineNumber, symbolTable.top_typestack());
		}

		symbolTable.gen_instr("PUSHI", 0);
		getNextToken();
	}
	
}

void SyntaxAnalyzer::error(ErrorType errorType, int lineNumber, std::string expected)
{
	errCount++;
	err << "[ERR] (Line " << lineNumber << ") ";
	switch (errorType)
	{
	case TYPE_MISMATCH:
	{
		err << "TYPE MISMATCH";
		if (expected != "")
		{
			err << ". Expected \"" << expected << "\"";
		}
		break;
	}
	case DUPLICATE_SYMBOL:
	{
		err << "DUPLICATE SYMBOL";
		if (expected != "")
		{
			err << " \"" << expected << "\"";
		}
		break;
	}
	case UNDECLARED_VARIABLE:
	{
		err << "UNDECLARED VARIABLE";
		if (expected != "")
		{
			err << " \"" << expected << "\"";
		}

		break;
	}
	}
	err << std::endl;
}

void SyntaxAnalyzer::Empty()
{
	if (print)
	{
		output << "\t<Empty> -> e" << std::endl;
	}
}

void SyntaxAnalyzer::Identifier()
{
	if(print)
	{
		output << "\t<Identifier>" << std::endl;
	}
}

void SyntaxAnalyzer::Integer()
{
	if(print)
	{
		output << "\t<Integer>" << std::endl;
	}
}

SyntaxAnalyzer::SyntaxAnalyzer(const std::vector<Lexer::Token> &tokens, std::ofstream &output, bool print) : tokens(tokens), it(tokens.begin()), currentToken(*(it)), output(output), save(nullptr)
{
	this->print = print;
	this->save = new Lexer::Token();
	this->errCount = 0;
	this->isDeclaration = false;
	this->assign = false;
}


SyntaxAnalyzer::~SyntaxAnalyzer()
{
	output.close();
}


void SyntaxAnalyzer::printCurrentToken()
{
	output << std::left << std::endl
		   << std::setw(8) << "Token:" << std::setw(16) << currentToken.token << std::setw(8) << "Lexeme:" << currentToken.lexeme << std::endl
		   << std::endl;
}

SyntaxError::SyntaxError(std::string message, int lineNumber)
{
	this->message = message;
	this->lineNumber = lineNumber;
}

SyntaxError::~SyntaxError() {}

std::string SyntaxError::getMessage() const
{
	return (this->message + " Line: " + std::to_string(this->lineNumber));
}


void SyntaxAnalyzer::getNextToken()
{
	++it;
	
	if (it == this->tokens.end())
	{
		--it;
		throw SyntaxError("Unexpected end of file", currentToken.lineNumber);
	}

	this->currentToken = *(it);

	if (print)
	{
		printCurrentToken();
	}

	if (this->currentToken.token == "Illegal")
	{
		throw SyntaxError("Illegal symbol: " + this->currentToken.lexeme+ " ", this->currentToken.lineNumber);
	}
}