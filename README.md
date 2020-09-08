# bitcoin-historical-data


# TODO

**Features**
- [ ] Write scripts to load the data to a Database table (PostgreSQL preferred)
- [ ] Write ETL scripts to load transform data to a separate database (Warehouse). ETL jobs should have at least these features: 
    * **a.**          : Job Scheduler
    * **b.**          : Retry at failures
    * **c.**          : Email at failures
    * **d.**          : Back population
- [ ] Do exploratory analysis and find as many insights as you can (visualizations strongly preferred)
- [ ] The  warehouse  should  be  transformed  in  such  a  way  that,  at  least  the following  questions should be answered:
    * **a.**          : Daily/Monthly/Yearly transaction reports
    * **b.**          :  predicting/Forecasting Pricing, Number of Transactions, etc.
- [ ] Propose and Implement a solution for real-time anomaly detection or suspicious pricing alerts.


**Detection**
- [ ] **Data lake**: Store the data into s3 using AWS boto framework 
- [ ] **Notification service**: use aws sns for email notification
- [ ] **Intermediate DB service**: use RDS for inserting 

