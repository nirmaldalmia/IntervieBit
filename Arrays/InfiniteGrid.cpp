#include<stdio.h>
#include<stdlib.h>
int main() {
	int A[2] = {-7,-13};
	int B[2] = {1,-5};
	int n1=2;
	int n2=2;
	int steps = 0;
    if (n1 != n2) {
        return 0;
    }
    int i = 0;
    while(i != n1 -1) {
        int xi = A[i];
        int yi = B[i];
        int xf = A[i+1];
        int yf = B[i+1];
        int xdiff = abs(xf-xi);
        //printf("X Diff is: %d\n", xdiff);
        int ydiff = abs(yf-yi);
        //printf("Y Diff is: %d\n", ydiff);
        if (xdiff >= ydiff) {
            steps = steps + xdiff;
        } else if (xdiff < ydiff) {
            steps = steps + ydiff;
        } else {
        	//printf("%d", steps);
            return steps;
        }
        i++;
    }
    //printf("%d\n", steps);
    return steps;
}
