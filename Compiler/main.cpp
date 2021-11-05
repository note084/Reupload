#include <iostream>
#include <fstream>
#include "syntaxAnalyzer.h"

int main()
{

	std::ifstream fin;
	std::string inFile;
	std::vector<Lexer::Token> lineTokens;
	std::vector<Lexer::Token> tokens;
	std::stringstream *buffer;
	std::string line;
	std::string input;
	std::cout << "Please enter in the test file name." << std::endl;
	std::cin >> input;

	std::vector<std::string> files = { input };
	std::ofstream out;
	out.open("output.txt");

	for (std::string file : files)
	{

		fin.open(file.c_str());

		if (!fin)
		{
			std::cout << "file not found" << std::endl;
			out << "file not found" << std::endl;
			continue;
		}

		std::cout 	<< std::endl
					<< "RUNNING TEST CASE FILE \"" << file << "\"" << std::endl
					<< std::endl;
		out << std::endl
			<< "RUNNING TEST CASE FILE \"" << file << "\"" << std::endl
			<< std::endl;

		Lexer *lexer = new Lexer();

		int lineNumber = 1;

		while (getline(fin, line))
		{
			buffer = new std::stringstream(line);
			lineTokens = lexer->lex(*buffer, lineNumber);

			tokens.insert(tokens.end(), lineTokens.begin(), lineTokens.end());

			lineNumber++;
		}
		fin.close();

		SyntaxAnalyzer *syntaxAnalyzer = new SyntaxAnalyzer(tokens, out, false);
		try
		{
			syntaxAnalyzer->Analyze();
		}
		catch (const SyntaxError &e)
		{
			out << std::endl << "ERROR: " << e.getMessage();
		}
		tokens.clear();

		out << std::endl;
	}

	out.close();
	std::cout << std::endl << "LEXICAL ANALYSIS COMPLETED. " << std::endl;


	return 0;
}