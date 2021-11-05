#include "lexerAnalyzer.h"


Lexer::Lexer() : comment(false) {}

Lexer::~Lexer() {}

std::vector<Lexer::Token> Lexer::lex(std::stringstream &buffer, int lineNumber)
{
	std::vector<Token> tokens;
	Token *token;
	char c;
	int transition;
	std::string lexeme = "";
	std::string tokenStr = "";
	int prevState = 0;
	int currState = 0;

	while (buffer.get(c))
	{

		if (comment | (c == '[' && buffer.peek() == '*'))
		{

			while (c != '*' | buffer.peek() != ']')
			{

				if (buffer.eof())
				{
					comment = true;
					c = ' ';
					break;
				}

				buffer.get(c);
			}


			if (!buffer.eof() && c == '*')
			{
				comment = false;

				buffer.get(c).get(c);
			}
		}

		transition = getTransition(c);

		if (transition == OPERATOR)
		{
			if ((lexeme == "+") || (lexeme == "-") || (lexeme == ">") || (lexeme == "*"))
			{
			}
			else if (c == '<' && buffer.peek() == '=')
			{
				lexeme.push_back(c);
				buffer.get(c);
			}
			else if (c == '=' && buffer.peek() == '=')
			{
				lexeme.push_back(c);
				buffer.get(c);
			}
			else if (c == '=' && buffer.peek() == '>')
			{
				lexeme.push_back(c);
				buffer.get(c);
			}
			else if (c == '/' && buffer.peek() == '=')
			{
				lexeme.push_back(c);
				buffer.get(c);
			}
			else
			{
			}
		}

		if (transition == FUNCTIONSEPARATOR)
		{
		  if (buffer.peek() == '%')
		  {
			  lexeme.push_back(c);
		      buffer.get(c);
		  }
		  else if (c == '%' && buffer.peek() != '%')
		  {
		    transition = REJECT;
		  }
		}


		currState = Lexer::stateTable[currState][transition];


		if (currState == EXT)
		{
			tokenStr = stateToString(prevState);

			if (tokenStr != "Illegal")
			{

				if (tokenStr == "Identifier")
				{

					if (isKeyword(lexeme))
					{
						tokenStr = "Keyword";
					}
				}

				token = new Token(tokenStr, lexeme, lineNumber);
				tokens.push_back(*token);


				currState = SS;
				lexeme.clear();
				tokenStr.clear();


				if (!isspace(c))
				{
					buffer.putback(c);
				}
			}
			else
			{

				if (!lexeme.empty())
				{
					token = new Token(tokenStr, lexeme, lineNumber);
					tokens.push_back(*token);
				}


				currState = SS;
				lexeme.clear();
				tokenStr.clear();
			}
		}
		else
		{
			if (!isspace(c))
			{
				lexeme.push_back(c);
			}
		}

		prevState = currState;

	}

	tokenStr = stateToString(prevState);

	if (tokenStr != "Illegal")
	{
		if (tokenStr == "Identifier")
		{
			if (isKeyword(lexeme))
			{
				tokenStr = "Keyword";
			}
		}

		token = new Token(tokenStr, lexeme, lineNumber);
		tokens.push_back(*token);
	}

	return tokens;
}

int Lexer::getTransition(char c) const
{
	int transition = REJECT;

	if (isdigit(c))
	{
		transition = INTEGER;
	}
	else if (isalpha(c))
	{
		transition = IDENTIFIER;
	}
	else if (c == '.')
	{
		transition = REAL;
	}
	else if (c == '_')
	{
		transition = UNDERSCORE;
	}
	else if (isValidOperator(c))
	{
		transition = OPERATOR;
	}
	else if (isValidSeparator(c))
	{
		transition = SEPARATOR;
	}
	else if (c == '%')
	{
		transition = FUNCTIONSEPARATOR;
	}


	return transition;
}

std::string Lexer::stateToString(int state) const
{
	std::string stateStr = "Illegal";

	switch (state)
	{
	case S01:
		stateStr = "Identifier";
		break;
	case S02:
		stateStr = "Integer";
		break;
	case S03:
		stateStr = "Illegal";
		break;
	case S04:
		stateStr = "Underscore";
		break;
	case S05:
		stateStr = "Operator";
		break;
	case S06:
		stateStr = "Separator";
		break;
	case S07:
		stateStr = "Separator";
		break;
	}

	return stateStr;
}

bool Lexer::isValidSeparator(char c) const
{
	return separators.count(c);
}

bool Lexer::isValidOperator(char c) const
{
	return operators.count(c);
}

bool Lexer::isKeyword(std::string token) const
{
	return keywords.count(token);
}
