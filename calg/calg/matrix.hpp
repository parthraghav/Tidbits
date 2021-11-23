//
//  matrix.hpp
//  calg
//
//  Created by Parth Raghav on 11/23/20.
//  Copyright © 2020 Parth Raghav. All rights reserved.
//

#ifndef matrix_hpp
#define matrix_hpp

#include <stdio.h>
#include <iostream>
#include <vector>

class Matrix {
    
    std::vector<int> mat;
    
    int index2d(int j, int i);
    
public:
    int w;
    int h;
    
    Matrix(int nCols, int nRows);

    void read();
    
    void print();
    
    void set(int j, int i, int val);
    
    int get(int j, int i);
    
    Matrix transpose();
    
    Matrix operator + (Matrix &other);

    Matrix operator - (Matrix other);
    
    Matrix operator * (Matrix other);

    void operator = (Matrix &other);
};


#endif /* matrix_hpp */
