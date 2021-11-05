#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

//Class to create the simulation of memory management
class Simulator
{
public:
  
  //Data structure for memory management
  struct MM
  {
    bool free = true;
    int pID = 0;
    int page = 0;
  };
  
  //Data structure to contain each process's data
  struct Process
  {
    int processID = 0;
    int arrivalTime = 0;
    int memSize = 0;
    float lifeTime = 0;
    float lifeTimeInMemory = 0;
    bool que = false;
    bool life = true;
    bool mm = false;

  };
 
 //Initializing basic global variables
  ofstream out;
  int memSize = 0;
  float numOfProcesses = 0;
  int const max_Time = 100000;
  int max_Memory = 0;
  int page_Size = 0;
  int current_Time = 0;
  float totalArrivalTime = 0.0;

//Initializing vector of type Process to hold each Process object
  vector<Process> components;
  vector<Process> queue;

//Basic constructor to read file input and store it
  Simulator(string file);
  vector<MM> MM;
  
  //Main loop function to calculate memory management
  void memoryManager();

  //Helper functions to manage memory data  
  void addMM(int pID, int pMem);
  void removeMM( int pID, int pMem);
  void outputMM();
};

//Simulator.cpp

Simulator::Simulator(string file)
{
    fstream inData;
    inData.open(file);
    int tempProcessID = 0;
    float tempArrivalTime = 0;
    int tempMemSize = 0;
    float totalProcesses = 0;
    float tempLifeTimeInMemory = 0;

    Process temp;
    
    inData >> numOfProcesses;

  while(!inData.eof())
  {
    int totalMem = 0;
    int mem = 0;
    inData >> tempProcessID;
    inData >> tempArrivalTime >> tempLifeTimeInMemory;
    inData >> totalProcesses;
    while (totalProcesses > 0)
    {
        
        inData >> mem;
        totalMem += mem;
        totalProcesses--;
    }
    tempMemSize = totalMem;

    if(!inData.good())
    {
        //checks for end of file
        break;
    }

    tempLifeTimeInMemory += tempArrivalTime;

    temp.processID = tempProcessID;
    temp.arrivalTime = tempArrivalTime;
    temp.memSize = tempMemSize;
    temp.lifeTimeInMemory = tempLifeTimeInMemory;
    temp.lifeTime = tempLifeTimeInMemory;

    components.push_back(temp);
  }
  
  inData.close();
  
}

void Simulator::memoryManager()
{

    //Initializing basic variables
    float it = numOfProcesses;
    int current_Memory = 0;
    bool print = true;
    float totalTime = 0.0;
    float average = 0.0;

    //Main Loop
    while(current_Time <= max_Time && it > 0)
    {
        int counter = 0;
        print = true;


        //Loop to check if a process has reached life time and removes from MM
        for(int i = 0; i < components.size(); i++)
        {
            if(components.at(i).lifeTime == current_Time && components.at(i).mm == true)
            {
                if (print == true)
                {
                    out << "t = " << current_Time << ": Process " << components.at(i).processID << " completes" << endl;
                }
                else
                {
                    out << "\t\tProcess " << components.at(i).processID << " completes" << endl;
                }
                print = false;
                components.at(i).life = false;
                totalArrivalTime+= components.at(i).arrivalTime;
                totalTime+= components.at(i).lifeTime;
                current_Memory -= components.at(i).memSize;
                removeMM(components.at(i).processID, components.at(i).memSize);
                outputMM();
                it--;
            }
            if(components.at(i).life == true)
            {
                counter++;
            }
        }
        it = counter;


        //Loop to check when processes arrive and adds them into the queue
        for(int i = 0; i <= components.size() - 1; i++)
        {
            if(components.at(i).arrivalTime == current_Time)
            {  
                out << "t = " << current_Time << ":  Process " << components.at(i).processID << " arrives" << endl;

                components.at(i).que = true;
                queue.push_back(components.at(i));


                out << "\t\tInput Queue: [";
                for (int i = 0; i < queue.size(); i++)
                {
                    out << queue.at(i).processID << " ";
                }
                out << "]" << endl;
                outputMM();
            }
        }

        //Statement and Loop to check if it is valid to add process from queue into MM
        if (queue.size() > 0)
        {
            for(int i = 0; i < queue.size(); i++)
            {
                if(((queue.at(i).memSize + current_Memory) <= max_Memory) && (queue.at(i).que == true) && (queue.at(i).arrivalTime == current_Time))
                {
                    out << "\t\tMM moves Process " << queue.at(i).processID << " to memory" << endl;
                    addMM(queue.at(i).processID, queue.at(i).memSize);
                    current_Memory += queue.at(i).memSize;
                    queue.at(i).mm = true;

                    for(int j = 0; j < components.size(); j++)
                    {
                        if(queue.at(i).processID == components.at(j).processID)
                        {
                            components.at(j).mm = true;
                        }
                    }

                    out << "\t\tInput Queue: [";
                    for (int i = 0; i < queue.size(); i++)
                    {
                        if(queue.at(i).mm == false)
                        {
                            out << queue.at(i).processID << " ";
                        }
                    }
                        out << "]" << endl;
                        outputMM();
                }
                else
                {
                    if(((queue.at(i).memSize + current_Memory) <= max_Memory) && (queue.at(i).que == true) && (queue.at(i).mm == false))
                    {
                        out << "\t\tMM moves Process " << queue.at(i).processID << " to memory" << endl;
                        addMM(queue.at(i).processID, queue.at(i).memSize);
                        current_Memory += queue.at(i).memSize;
                        queue.at(i).mm = true;
                    }
                    for(int j = 0; j < components.size(); j++)
                    {
                        if(queue.at(i).processID == components.at(j).processID)
                        {
                            components.at(j).mm = true;
                        }
                    }
                    out << "\t\tInput Queue: [";
                    for (int i = 0; i < queue.size(); i++)
                    {
                        if(queue.at(i).mm == false)
                        {
                            out << queue.at(i).processID << " ";
                        }
                    }
                        out << "]" << endl;
                        outputMM();
                }
                
            }
        }

        //Statement to check if queue has been added to MM and then removes it from queue if valid
        if (queue.size() > 0)
        {
            queue.erase(std::remove_if(queue.begin(), queue.end(), [&](Process const & queue)
            {
                return queue.mm;
            }), queue.end());
        }

        current_Time+= 100;

    }

    //Outputting total average turnaround time after loop is complete and checks whether loop exited via time or via completion
    out << fixed << setprecision(2);
    if(it > 0)
    {
        average = (totalTime - totalArrivalTime) / (numOfProcesses - it);
    }
    else
    {
        average = (totalTime - totalArrivalTime) / numOfProcesses;
    }
    out << endl << "Average Turnaround Time: " << average  << endl;
}

void Simulator::addMM(int pID, int pMem)
{
    int loop = (pMem + page_Size - 1) / page_Size;
    int page = 1;
    int i = 0;

    while (loop > 0 && i < (max_Memory / page_Size))
    {
        if(MM.at(i).free == true)
        {
            MM.at(i).free = false;
            MM.at(i).pID = pID;
            MM.at(i).page = page;
            page++;
            loop--;
        }
        i++;
    }
}

void Simulator::removeMM(int pID, int pMem)
{
    int loop = (pMem + page_Size - 1) / page_Size;
    int i = 0;
    while (loop > 0 && i < (max_Memory / page_Size))
    {
        if(MM.at(i).pID == pID)
        {
            MM.at(i).free = true;
            loop--;
        }
        i++;
    }
}

void Simulator::outputMM()
{
    int count = 0;
    out << "\t\tMemory map:" << endl;
    for(int i = 0; i < MM.size(); i++)
    {
        if (MM.at(i).free == true)
        {
            count++;
            if (count == (MM.size()))
            {
                out << "\t\t\t\t0-" << ((page_Size * MM.size()) - 1) << ": Free frame(s)" << endl;
            }
            if (count != 20 && i == MM.size() - 1)
            {
                out << "\t\t\t\t" << ((i - count + 1) * page_Size) << "-" << ((page_Size * MM.size()) - 1) << ": Free frame(s)" << endl;
            }
        }
        else
        {
            if (count > 1)
            {
                out << "\t\t\t\t" << ((i - count) * page_Size) << "-" << ((i * page_Size) - 1) << ": Free frame(s)" << endl;
                out << "\t\t\t\t" << (i * page_Size) << "-" << (((i * page_Size) + page_Size) - 1) << " Process " << MM.at(i).pID << " Page " << MM.at(i).page << endl;
                count = 0;
            }
            else
            {
                out << "\t\t\t\t" << (i * page_Size) << "-" << (((i * page_Size) + page_Size) - 1) << " Process " << MM.at(i).pID << " Page " << MM.at(i).page << endl;
            }
        }
        
    }
}
