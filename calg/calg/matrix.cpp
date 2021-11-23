//
//  matrix.cpp
//  calg
//
//  Created by Parth Raghav on 11/23/20.
//  Copyright © 2020 Parth Raghav. All rights reserved.
//

#include "matrix.hpp"

Matrix::Matrix(int nCols, int nRows) : h(nCols), w(nRows), mat(nCols * nRows) {
    assert(h > 0 && w > 0);
}

void Matrix::read() {
    printf("%s", "Enter values down below\n");
    for(int j = 0; j < h; j++) {
        for(int i = 0; i < w; i++) {
            printf("M[%d][%d]\t",j,i);
            scanf("%d", &mat[index2d(j, i)]);
        }
    }
}

void Matrix::print() {
    for(int j = 0; j < h; j++) {
        for(int i = 0; i < w; i++) {
            printf("%d\t",mat[index2d(j,i)]);
        }
        printf("\n");
    }
}

void Matrix::set(int j, int i, int val) {
    mat[index2d(j, i)] = val;
}

int Matrix::get(int j, int i) {
    return mat[index2d(j, i)];
}

Matrix Matrix::transpose() {
    Matrix resultant_mat = Matrix(w, h);
    for(int j = 0; j < h; j++) {
        for(int i = 0; i < w; i++) {
            resultant_mat.set(i, j, this->get(j, i));
        }
    }
    return resultant_mat;
}

Matrix Matrix::operator + (Matrix &other) {
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

Matrix Matrix::operator - (Matrix other) {
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

Matrix Matrix::operator * (Matrix other) {
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

void Matrix::operator = (Matrix &other) {
    assert(this->w == other.h);
    for(int j = 0; j < h; j++) {
        for(int i = 0; i < w; i++) {
            for(int k = 0; k < other.w; k++) {
                this->set(j, i, other.get(j, i));
            }
        }
    }
}
