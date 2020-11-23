//
//  main.cpp
//  calg
//
//  Created by Parth Raghav on 11/9/20.
//  Copyright © 2020 Parth Raghav. All rights reserved.
//

#include <iostream>
#include <vector>

class Matrix {

    std::vector<int> mat;
    
    int index2d(int j, int i) {
        return j*w+i;
    }
    
public:
    int w;
    int h;
    
    Matrix(int nCols, int nRows) : h(nCols), w(nRows), mat(nCols * nRows) {
        assert(h > 0 && w > 0);
    }

    void read() {
        printf("%s", "Enter values down below\n");
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                printf("M[%d][%d]\t",j,i);
                scanf("%d", &mat[index2d(j, i)]);
            }
        }
    }
    
    void print() {
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                printf("%d\t",mat[index2d(j,i)]);
            }
            printf("\n");
        }
    }
    
    void set(int j, int i, int val) {
        mat[index2d(j, i)] = val;
    }
    
    int get(int j, int i) {
        return mat[index2d(j, i)];
    }
    
    Matrix transpose() {
        Matrix resultant_mat = Matrix(w, h);
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                resultant_mat.set(i, j, this->get(j, i));
            }
        }
        return resultant_mat;
    }
    
    Matrix operator + (Matrix &other) {
        Matrix resultant_mat = Matrix(h, w);
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                int a = this->get(j, i);
                int b = other.get(j, i);
                resultant_mat.set(j, i, a + b);
            }
        }
        return resultant_mat;
    }

    Matrix operator - (Matrix other) {
        Matrix resultant_mat = Matrix(h, w);
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                int a = this->get(j, i);
                int b = other.get(j, i);
                resultant_mat.set(j, i, a - b);
            }
        }
        return resultant_mat;
    }
    
    Matrix operator * (Matrix other) {
        assert(this->w == other.h);
        Matrix resultant_mat = Matrix(h, w);
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                for(int k = 0; k < other.w; k++) {
                    int a = this->get(i, k);
                    int b = other.get(k, j);
                    resultant_mat.set(j, i, resultant_mat.get(j, i) + (a * b));
                }
            }
        }
        return resultant_mat;
    }

    void operator = (Matrix &other) {
        assert(this->w == other.h);
        for(int j = 0; j < h; j++) {
            for(int i = 0; i < w; i++) {
                for(int k = 0; k < other.w; k++) {
                    this->set(j, i, other.get(j, i));
                }
            }
        }
    }
};

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
