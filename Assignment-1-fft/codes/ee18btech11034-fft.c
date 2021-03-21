# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>
typedef double complex cp;

double pi =  3.141592653589793238;

void elementwise_multiply(cp* Y,cp* X,cp* Hz,int n)
{
	for(int i=0;i<n;i++)
	{
		Y[i] = Hz[i]*X[i];
	}
}

	
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

void ifft(cp* X, int n){
    if (n == 1)
        return;

   
    cp *Xeven = (cp *) malloc(n/2 * sizeof(cp));
    cp *Xodd = (cp *) malloc(n/2 * sizeof(cp));
    for (int i = 0;i < n/2;i++) 
    {
        Xeven[i] = X[2*i];
        Xodd[i] = X[(2*i)+1];
    }

    ifft(Xeven, n/2);
    ifft(Xodd, n/2);

    
    cp eraised;
    for (int i = 0;i < n/2;i++) 
    {
		eraised = CMPLX(cos(2*pi*i/n),sin(2*pi*i/n));
		
	    X[i] = Xeven[i] + eraised * Xodd[i];
        X[i+n/2] = Xeven[i] - eraised * Xodd[i];
       
    }
    free(Xeven);
    free(Xodd);
}



int main(){
    int n = pow(2,21);
    
    double *x = (double *) malloc(n *sizeof(double));
    cp *Hz = (cp *) malloc(n * sizeof(cp)); 
    cp *Y = (cp *) malloc(n * sizeof(cp));
    cp *y = (cp *) malloc(n * sizeof(cp));
    cp *X = (cp *) malloc(n * sizeof(cp));
    FILE *fi1, *fo1,*fi2,*fo2,*fo3;

    fi1 = fopen("../files/x_fft.dat", "r");
    
    /*int count = 0;*/
    for(int i=0;i<n;i++) 
    {
        double data;
        fscanf(fi1, "%lf", &data);
        x[i] = data;
    }

    fclose(fi1);
    for(int i = 0; i < n; i++)
    {
        X[i] = x[i];
    }

    fft(X, n);

    fo1  = fopen("../files/X_fft.dat", "w");
    
    for(int i = 0; i < n; i++)
    {
        fprintf(fo1, "%lf+j%lf\n", creal(X[i]), cimag(X[i]));
    }
    
    fclose(fo1);
    
    fi2 = fopen("../files/H_z.dat","r");
    for(int i=0;i<n;i++) 
    {
        double re,im;
        fscanf(fi2, "%lf" "%lf", &re,&im);
        Hz[i] = CMPLX(re,im);
    }
    fclose(fi2);
    elementwise_multiply(Y,X,Hz,n);
    
    fo2 = fopen("../files/Y_fft.dat","w");
    for(int i = 0; i < n; i++)
    {
        fprintf(fo2, "%lf+j%lf\n", creal(Y[i]), cimag(Y[i]));
    }
    fclose(fo2);
    
    for(int i=0;i<n;i++)
    {
		y[i] = Y[i];
	}
	
    ifft(y,n);
    
    fo3 = fopen("../files/y_fft.dat","w");
    for(int i=0;i<n;i++)
    {
		y[i] = y[i]/n;
		fprintf(fo3, "%lf %lf\n", creal(y[i]), cimag(y[i]));
	}
	fclose(fo3);

    return 0;
}

