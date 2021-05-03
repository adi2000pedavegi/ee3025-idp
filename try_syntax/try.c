# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>
typedef double complex cp;

double pi =  3.141592653589793238;

void fft(cp* X, int n){
    if (n == 1)
        return;

   
    cp *Xeven = (cp *) malloc(n/2 * sizeof(cp));
    cp *Xodd = (cp *) malloc(n/2 * sizeof(cp));
    for (int i = 0;i < n/2;i++) 
    {
        Xeven[i] = X[2*i];
        Xodd[i] = X[(2*i)+1];
    }

    fft(Xeven, n/2);
    fft(Xodd, n/2);

    
    cp eraised;
    for (int i = 0;i < n/2;i++) 
    {
		eraised = CMPLX(cos(2*pi*i/n),-sin(2*pi*i/n));
		
	    X[i] = Xeven[i] + eraised * Xodd[i];
        X[i+n/2] = Xeven[i] - eraised * Xodd[i];
       
    }
    free(Xeven);
    free(Xodd);
}




int main(){
    int n = pow(2,21);
    /*cp *x = (cp *) malloc(n * sizeof(cp)); */
    double *x = (double *) malloc(n *sizeof(double));
    cp *H = (cp *) malloc(n * sizeof(cp)); 
    cp *Y = (cp *) malloc(n * sizeof(cp));
    cp *y = (cp *) malloc(n * sizeof(cp));
    cp *X = (cp *) malloc(n * sizeof(cp));
    FILE *fi1, *fo1;

    fi1 = fopen("x.dat", "r");
    
    /*int count = 0;*/
    for(int i=0;i<n;i++) 
    {
        double data;
        fscanf(fi1, "%lf", &data);
        x[i] = data;
    }

    
    for(int i = 0; i < n; i++)
    {
        X[i] = x[i];
    }

    fft(X, n);

    fo1  = fopen("X.dat", "w");
    
    for(int i = 0; i < n; i++)
    {
        fprintf(fo1, "%lf+%lfi\n", creal(X[i]), cimag(X[i]));
    }
    
    fclose(fo1);
    fclose(fi1);
    

    return 0;
}
