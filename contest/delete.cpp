#include <iostream>
#include <fstream>
#include <string>

int main()
{

    std::string name = "C:/Users/Danish Amin/source/repos/RayTracing/Project3/Project3/res/shaders/basic.shader";
    std::ifstream stream(name);
    std::string line;

    while (std::getline(stream, line))
    {
        std::cout<<line<<std::endl;
    }

    return 0;
}