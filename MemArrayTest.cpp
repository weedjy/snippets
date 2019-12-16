#include <iostream>

int main()
{
    int x[3];
    x[0] = 1;
    x[1] = 1;
    x[2] = 1;
    void *p0 = (void*)&x[0];
    //������ ���� ����� 4
    std::cout << (int)(&x[0]) << " " << 
                 (int)(&x[1]) << " " <<
                 (int)(&x[2]) << std::endl;
    //���� ����� char*, �� +4 ���� ������ �������, � +1,+2,+3 �����
    //������� 1 16777216(m) 65536(m) 256(m) 1--��� ������ �������
    std::cout << (int)(*((int*)((char*)p0 + 0))) << " " <<
                 (int)(*((int*)((char*)p0 + 1))) << " " <<
                 (int)(*((int*)((char*)p0 + 2))) << " " <<
                 (int)(*((int*)((char*)p0 + 3))) << " " <<
                 (int)(*((int*)((char*)p0 + 4))) << std::endl;
    //���� ����� int*, �� +1 ���� ������ �������, � +2 ������
    //� +3 � +4 �����
    //1 1 1 m m
    std::cout << (int)(*((int*)((int*)p0 + 0))) << " " <<
                 (int)(*((int*)((int*)p0 + 1))) << " " <<
                 (int)(*((int*)((int*)p0 + 2))) << " " <<
                 (int)(*((int*)((int*)p0 + 3))) << " " <<
                 (int)(*((int*)((int*)p0 + 4))) << std::endl;
}
