#ifndef LEXER_H
#define LEXER_H

#include <iostream>
#include <vector>
#include <unordered_set>
#include <sstream>
#include <iomanip>

class Lexer
{
public:
	enum State
	{
		SS = 0,
		S01,
		S02,
		S03,
		S04,
		S05,
		S06,
		S07,
		S08,
		S09,
		EXT
	};

	enum TransitionType
	{
		IDENTIFIER = 0,
		INTEGER,
		REAL,
		UNDERSCORE,
		OPERATOR,
		SEPARATOR,
		FUNCTIONSEPARATOR,
		REJECT
	};
	                        // L    d     .    _   op   sep func rej
	int stateTable[10][8] = {{S01, S02, S08, S08, S05, S06, S07, EXT},   //Starting State
							{S01, S01, EXT, S01, EXT, EXT, EXT, EXT},  // 1
						    {EXT, EXT, EXT, EXT, EXT, EXT, EXT, EXT},  // 2
							{S08, S09, S08, S08, S08, S08, S08, S08},  // 3 
							{EXT, EXT, EXT, EXT, EXT, EXT, EXT, EXT},  // 4
                            {EXT, EXT, EXT, EXT, EXT, EXT, EXT, EXT},  // 5
                            {EXT, EXT, EXT, EXT, EXT, EXT, EXT, EXT},  // 6
                            {EXT, EXT, EXT, EXT, EXT, EXT, EXT, EXT},  // 7
                            {EXT, EXT, EXT, EXT, EXT, EXT, EXT, EXT},  //8
							{EXT, S09, EXT, EXT, EXT, EXT, EXT, EXT}};  // 9 

	std::unordered_set<std::string>keywords = { "int", "boolean", "function", "if", "fi", "otherwise", "return", "put", "get", "while", "true", "false" };
	std::unordered_set<char> separators = { '(', ')', '{', '}', ',', ';' };
	std::unordered_set<char> operators = { '+', '*', '/', '-', '=', '<', '>' };


	struct Token
	{
		Token() : token("nil"), lexeme("nil"), lineNumber(-1) {};
		Token(std::string token, std::string lexeme, int lineNumber)
		{
			this->token = token;
			this->lexeme = lexeme;
			this->lineNumber = lineNumber;
		}

		std::string token;
		std::string lexeme;
		int lineNumber;
	};


	Lexer();


	~Lexer();

	std::vector<Token> lex(std::stringstream &buffer, int lineNumber);

private:

	bool isValidOperator(char c) const;

	bool comment;

	int getTransition(char tokenChar) const;

	std::string stateToString(int state) const;

	bool isValidSeparator(char c) const;

	bool isKeyword(std::string token) const;


};

#endif