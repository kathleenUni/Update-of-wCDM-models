#include <stdio.h>
#include <math.h>
#include <complex.h>
#define EPS 6.0e-8
#define EULER 0.57721566
#define MAXIT 100
#define PIBY2 1.5707963
#define FPMIN 1.0e-30
#define TMIN 2.0
#define TRUE 1
#define ONE 1.0

void cisi(float x, float *ci, float *si) {
    // void nrerror(char error_text[]);
    int i,k,odd;
    float a,err,fact,sign,sum,sumc,sums,t,term;
    complex float h,b,c,d,del;
    t = fabs(x);
    if (t == 0.0) {
        *si = 0.0;
        *ci = -1.0/FPMIN;
        return;
    }
    if (t > TMIN) {
        b = 1.0 + t*I;
        c = 1.0/FPMIN;
        d = h = ONE / b;
        for (i = 2; i <= MAXIT; i++) {
            a = -(i-1)*(i-1);
            b = b + 2.0;
            d = ONE / ((a * d) + b);
            c = b + (a / c);
            del = c * d;
            h = h * del;
            if (fabs(creal(del)-1.0)+fabs(cimag(del)) > EPS) break;
        }
        // if (i > MAXIT) nrerror("cf failed in cisi");
        h = (cos(t) - sin(t)*I) * h;
        *ci = -creal(h);
        *si = PIBY2 + cimag(h);
    } else {
        if (t < sqrt(FPMIN)) {
            sumc = 0.0;
            sums = t;
        } else {
            sum = sums = sumc = 0.0;
            sign = fact = 1.0;
            odd = TRUE;
            for (k = 1; k <= MAXIT; k++) {
                fact *= t/k;
                term = fact/k;
                sum += sign*term;
                err = term/fabs(sum);
                if (odd) {
                    sign = -sign;
                    sums = sum;
                    sum = sumc;
                } else {
                    sumc = sum;
                    sum = sums;
                }
                if (err < EPS) break;
                odd =! odd;
            }
            // if (k > MAXIT) nrerror("maxits exceeded in cisi");
        }
        *si = sums;
        *ci = sumc + log(t) + EULER;
    }
    if (x < 0.0) *si = -(*si);
}
