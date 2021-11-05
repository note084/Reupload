#include "symbolTable.h"


SymbolTable::SymbolTable() : memaddress(5000) {}


SymbolTable::~SymbolTable()
{
    instr_address = 1;
}


void SymbolTable::incrementMem()
{
    ++this->memaddress;
}


bool SymbolTable::insert(Lexer::Token t, std::string type)
{
    bool success = false;

    if (!lookup(t))
    {
        Symbol *s = new Symbol(t, this->memaddress, type);
        this->table.push_back(*s);
        incrementMem();
        success = true;
    }

    return success;
}

int SymbolTable::lookup(Lexer::Token t)
{
    std::vector<Symbol>::iterator it = this->table.begin();
    bool found = false;

    while (!found && it != this->table.end())
    {
        if (it->token.lexeme == t.lexeme && it->token.token == t.token)
        {
            found = true;
        }
        else
        {
            ++it;
        }
    }

    return found ? it->address : 0;
}


bool SymbolTable::remove(Lexer::Token t)
{
    bool success = false;
    int pos = 0;

    if (lookup(t))
    {
        std::vector<Symbol>::const_iterator it = this->table.begin();
        while (!success && it != this->table.end())
        {
            if (it->token.lexeme == t.lexeme)
            {
                this->table.erase(this->table.begin() + pos);
                success = true;
            }
            else
            {
                ++pos;
                ++it;
            }
        }
    }

    return success;
}


std::string SymbolTable::list()
{
    std::ostringstream os;
    const int COL_WIDTH = 15;

    os << std::left << std::setw(COL_WIDTH) << "Identifier" << std::setw(COL_WIDTH) << "Type"
       << "Memory Address" << std::endl;
	os << std::setfill('-') << std::setw(COL_WIDTH * 2 + 14) << '-' << std::setfill(' ') << std::endl;

    for (std::vector<Symbol>::const_iterator it = this->table.begin(); it != this->table.end(); ++it)
    {
        os << std::setw(COL_WIDTH) << it->token.lexeme << std::setw(COL_WIDTH) << it->type << it->address << std::endl;
    }

    return os.str();
}


std::string SymbolTable::list_instr()
{
    std::ostringstream os;
    const int COL_WIDTH = 15;

    os << std::left << std::setw(COL_WIDTH) << "Address" << std::setw(COL_WIDTH) << "OpCode"
       << "Operand" << std::endl;
	os << std::setfill('-') << std::setw(COL_WIDTH * 2 + 7) << '-' << std::setfill(' ') << std::endl;

    for (std::vector<Instr>::const_iterator it = this->instructions.begin(); it != this->instructions.end(); ++it)
    {
        os << std::setw(COL_WIDTH) << it->address << std::setw(COL_WIDTH) << it->op;

        if (it->operand != NIL)
        {
            os << it->operand;
        }

        os << std::endl;
    }

    return os.str();
}


void SymbolTable::gen_instr(std::string op, int operand)
{
    Instr *instr = new Instr(op, operand);

    this->instructions.push_back(*instr);
}


void SymbolTable::push_jumpstack(int address)
{
    this->jumpstack.push_back(address);
}


void SymbolTable::back_patch(int jump_addr)
{
    const int addr = jumpstack.back();
    jumpstack.pop_back();

    if (this->instructions.size() >= addr)
    {
        this->instructions.at(addr - 1).operand = jump_addr;
    }
    else
    {
        // TODO: ERROR
    }
}


int SymbolTable::get_address(Lexer::Token token)
{
    return lookup(token);
}


int SymbolTable::get_mem()
{
    return this->memaddress;
}


int SymbolTable::get_instr_address() const
{
    return instr_address;
}


void SymbolTable::push_typestack(std::string type)
{
    this->typestack.push(type);
}


bool SymbolTable::pop_typestack()
{
    bool success = false;

    if(!this->typestack.empty())
    {
        success = true;
        this->typestack.pop();
    }

    return success;
}


std::string SymbolTable::top_typestack() const
{
    return this->typestack.top();
}


std::string SymbolTable::get_type(Lexer::Token token) const
{
    std::string type = "";

    for(Symbol s : this->table)
    {
        if(s.token.lexeme == token.lexeme)
        {
            type = s.type;
            break;
        }
    }

	if (token.token == "Integer")
	{
		type = "int";
	}

    return type;
}


bool SymbolTable::typestack_empty() const
{
    return this->typestack.empty();
}