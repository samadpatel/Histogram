"""Name of the program: CLI extraction of database values and plotting of histogram.

Name: Samad Patel"""

import argparse
import sqlite3
from tabulate import tabulate
import matplotlib.pyplot as plot
import pandas as pd
import pylab as pl


"""Database function created which takes the parser arguments from the main function."""

def database(p,d,s,**kwargs):
    try:
        parser = argparse.ArgumentParser() 
        conn = sqlite3.connect(d)
        c = conn.cursor()
        r=c.execute(s)
        data=r.fetchall()

        """Check if the optional argument exists on the CLI command if it exists then display the histogram or else 
        it will print the table of the chinook.db from sub-project2"""

        if p is True:
            df=pd.DataFrame(data)
            df.plot.hist(color="#0504aa",width=0.5)
            pl.suptitle("Histogram")
            plot.xlabel("Total")
            plot.ylabel("BillingCountry")
            plot.savefig("Histogram.png",bbox_inches='tight')
            plot.show()    
        else:
            print(f'{tabulate(data)}')
    except:
        
        """Print help if something went wrong."""
        parser.print_help()


"""This is the main function where all the arguments are added and then 
passed to the function above for further processing."""

def main():
    
    try:
        parser = argparse.ArgumentParser()  
        parser.set_defaults(method = database) 
        parser.add_argument('-p',action='store_true',help="Give correct argument")   
        parser.add_argument('-d', help="Give correct argument")
        parser.add_argument('-s',help="Give correct argument")   
        args= parser.parse_args()
        args.method(**vars(args))
    
    except:
        """Print help if something went wrong."""
        parser.print_help()

"""Calls the main function"""
if __name__ == '__main__':
    main()