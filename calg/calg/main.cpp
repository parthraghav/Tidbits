//
//  main.cpp
//  calg
//
//  Created by Parth Raghav on 11/9/20.
//  Copyright © 2020 Parth Raghav. All rights reserved.
//

#include <iostream>
#include <vector>
#include "matrix.hpp"


int main(int argc, const char * argv[]) {
    enum Debugging { Addition, Subtraction, Multiplication, Transpose };
    Debugging current = Transpose;
    
    Matrix m1 = Matrix(2,2);
    Matrix m2 = Matrix(2,2);
    m1.read();
    m2.read();
    
    if (current == Addition) {
        Matrix m3 = m1 + m2;
        m3.print();
    } else if (current == Subtraction) {
        Matrix m3 = m1 - m2;
        m3.print();
    } else if (current == Multiplication) {
        Matrix m3 = m1 * m2;
        m3.print();
    } else if (current == Transpose) {
        Matrix m3 = m1.transpose();
        m3.print();
    }
    printf("\n");
    
    return 0;
}
