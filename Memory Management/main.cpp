#include "p2.h"

int main()
{
    int max_Memory = 0;
    int page_Size = 0;
    int input = 0;
    bool loop = true;
    string file;

    while (loop == true)
    {
        cout << "Memory Size> ";
        cin >> max_Memory;
        cout << endl;
        cout << "Page Size (1:100, 2: 200, 3:400)> ";
        cin >> input;
        cout << endl;

        if (input == 1)
        {
            page_Size = 100;
            loop = false;
        }
        else if(input == 2)
        {
            page_Size = 200;
            loop = false;
        }
        else if(input == 3)
        {
            page_Size = 400;
            loop = false;
        }
        else
        {
            cout << "Invalid input." << endl << endl;
        }
    }

    cout << "File name> ";
    cin >> file;
    Simulator test(file);
    test.max_Memory = max_Memory;
    test.page_Size = page_Size;
    test.MM.resize(max_Memory/page_Size);
    test.out.open("output.txt");
    
    test.memoryManager();

}