# Test Case 1 :
    ## Normal Budget  
         Enter the Destination : Hyderabad 
Enter the number of days for the trip: 5
Enter the Planned Budget : 20000
Enter the Estimated Expenses for  Travel : 5000
Enter the Estimated Expenses for  Food : 3000
Enter the Estimated Expenses for  Hotel : 6000
Enter the Estimated Expenses for  Others : 1000

----Estimated Expenses Summary----
Destination :  Hyderabad
number of days for the trip :  5
Planned Budget : $  20000.0
Estimated Total : $  15000.0
Remaining Budget : $  5000.0
Estimated Expenses are within the Planned Budget
Highest Budget Category : Hotel with amount $6000.00 (40.0%)
estimated daily average: $3000.00
Enter the Actual Expenses for Travel : 5500
Enter the Actual Expenses for Food : 2800
Enter the Actual Expenses for Hotel : 6500
Enter the Actual Expenses for Others : 1200

----Estimated vs Actual Expenses Comparison----
Category       Estimated      Actual         Difference     
------------------------------------------------------------
Travel         $5000.00       $5500.00       $500.00        
Food           $3000.00       $2800.00       $-200.00       
Hotel          $6000.00       $6500.00       $500.00        
Others         $1000.00       $1200.00       $200.00        
------------------------------------------------------------
Total          $15000.00      $16000.00      $1000.00       

----Actual Expenses Summary----
Actual Total : $16000.00
Difference between Actual and Estimated Total : $1000.00
Final Budget Balance : $4000.00
actual daily average: $3200.00
Trip spending is within the planned budget.  


# Test Case 2 :
    ## expenses Exactly Equals the budget 

    Enter the Destination : Delhi
Enter the number of days for the trip: 10
Enter the Planned Budget : 20000
Enter the Estimated Expenses for  Travel : 5000
Enter the Estimated Expenses for  Food : 4000
Enter the Estimated Expenses for  Hotel : 6000
Enter the Estimated Expenses for  Others : 2000

----Estimated Expenses Summary----
Destination :  Delhi
number of days for the trip :  10
Planned Budget : $  20000.0
Estimated Total : $  17000.0
Remaining Budget : $  3000.0
Estimated Expenses are within the Planned Budget
Highest Budget Category : Hotel with amount $6000.00 (35.3%)
estimated daily average: $1700.00
Enter the Actual Expenses for Travel : 6000
Enter the Actual Expenses for Food : 5000
Enter the Actual Expenses for Hotel : 7000
Enter the Actual Expenses for Others : 2000

----Estimated vs Actual Expenses Comparison----
Category       Estimated      Actual         Difference     
------------------------------------------------------------
Travel         $5000.00       $6000.00       $1000.00       
Food           $4000.00       $5000.00       $1000.00       
Hotel          $6000.00       $7000.00       $1000.00       
Others         $2000.00       $2000.00       $0.00          
------------------------------------------------------------
Total          $17000.00      $20000.00      $3000.00       

----Actual Expenses Summary----
Actual Total : $20000.00
Difference between Actual and Estimated Total : $3000.00
Final Budget Balance : $0.00
actual daily average: $2000.00
Trip spending is exactly equal to the planned budget.   


# Test case 3 :
   ## Overspending 

   Enter the Destination : kerala
Enter the number of days for the trip: 10
Enter the Planned Budget : 2000
Enter the Estimated Expenses for  Travel : 5000
Enter the Estimated Expenses for  Food : 4000
Enter the Estimated Expenses for  Hotel : 6000
Enter the Estimated Expenses for  Others : 2000

----Estimated Expenses Summary----
Destination :  kerala
number of days for the trip :  10
Planned Budget : $  2000.0
Estimated Total : $  17000.0
Remaining Budget : $  -15000.0
Remaining Buffer: 750.0%
Warning : Estimated Expenses exceed the Planned Budget
Highest Budget Category : Hotel with amount $6000.00 (35.3%)
estimated daily average: $1700.00
Enter the Actual Expenses for Travel : 8000
Enter the Actual Expenses for Food : 6000
Enter the Actual Expenses for Hotel : 9000
Enter the Actual Expenses for Others : 3000

----Estimated vs Actual Expenses Comparison----
Category       Estimated      Actual         Difference     
------------------------------------------------------------
Travel         $5000.00       $8000.00       $3000.00       
Food           $4000.00       $6000.00       $2000.00       
Hotel          $6000.00       $9000.00       $3000.00       
Others         $2000.00       $3000.00       $1000.00       
------------------------------------------------------------
Total          $17000.00      $26000.00      $9000.00       

----Actual Expenses Summary----
Actual Total : $26000.00
Difference between Actual and Estimated Total : $9000.00
Final Budget Balance : $-24000.00
actual daily average: $2600.00
Warning: Trip spending exceeds the planned budget. 

# Test case 4 :
   ## Invalid Inputs 
    A. Negative budget 
         
        Enter the Destination : delhi
Enter the number of days for the trip: 12
Enter the Planned Budget : -500
Error: Budget can not be zero or negative
Enter the Planned Budget : -199
Error: Budget can not be zero or negative
Enter the Planned Budget : 


    B. Negative Expenses  

       Enter the Destination : delhi
Enter the number of days for the trip: 12
Enter the Planned Budget : 2000
Enter the Estimated Expenses for  Travel : -200
Expenses can not be negative
Enter the Estimated Expenses for  Travel : -9797
Expenses can not be negative
Enter the Estimated Expenses for  Travel : -2772
Expenses can not be negative
Enter the Estimated Expenses for  Travel : 200
Enter the Estimated Expenses for  Food : 

 
     C. Non - Numeric input 

          Enter the Destination : delhi
Enter the number of days for the trip: 12
Enter the Planned Budget : 2000
Enter the Estimated Expenses for  Travel : abc
Enter a valid number.
Enter the Estimated Expenses for  Travel : dsds
Enter a valid number.
Enter the Estimated Expenses for  Travel : chagy
Enter a valid number.
Enter the Estimated Expenses for  Travel : TWENTY
Enter a valid number.
Enter the Estimated Expenses for  Travel : 120
Enter the Estimated Expenses for  Food :  


    D. Zero trip duration 

     Enter the Destination : hyd
Enter the number of days for the trip: 0
Trip duration must be greater than zero.
Enter the number of days for the trip: 0
Trip duration must be greater than zero.
Enter the number of days for the trip: -1
Trip duration must be greater than zero.
Enter the number of days for the trip: -100
Trip duration must be greater than zero.
Enter the number of days for the trip: 12
Enter the Planned Budget :  