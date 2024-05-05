# Database Setup and Population Guide

**Welcome to the Database Setup and Population Guide for this repository.** This README provides a step-by-step guide on preparing your database schema, populating the database using CSV files, and executing SQL scripts for data manipulation and query execution. Whether you're setting up a new database or managing existing data, this guide will help you navigate the process smoothly.

## Getting Started

Before you begin, ensure you have PostgreSQL installed and running on your system. You'll also need access to psql, PostgreSQL's interactive terminal, and your CSV files ready for data import.

## Step 1: Preparing the Database Schema

### Creating the Database Schema

1. **Schema Definition**: The `schema.sql` file contains Data Definition Language (DDL) commands to define the structure of your database. This includes creating tables, views, and other necessary database objects.

2. **Execution**: To apply the schema to your database, run the following command in the psql terminal:
    ```
    \i schema.sql
    ```
   This command executes the SQL statements in `schema.sql`, setting up your database schema.

## Step 2: Populating the Database


### Running Population Scripts

- The `g1popu.sql` script containstables from the original dataset but are much more condense and easier to read.

- To execute this script, run the following command in the psql terminal:
    ```
    \i g1popu.sql
    ```

## Step 3: Running the application

### Running Application Steps

- in our directory, we are going to type
  ```
    \python app.py
    ```

- In the Linux VM, you can run the application locally using Python Flask with the following command:
  ``` flask run ```

- Then type into the firefox search bar:
  ``` localhost:5000/index ```
  
- Now we should have the application running with our user friendly GUI

## GUI

- The GUI is set up to be very simple, our queries are listed below in which could be accessed by just a click as shown below.

### Homepage
  
<img width="1275" alt="Screenshot 2024-05-04 at 8 40 56 PM" src="https://github.com/TCNJ-degoodj/project-group01/assets/122068476/dcecb80d-5602-4685-bfe9-5bbc023808e7">


### Example query page: Dam's and the amount of baby goats they've grafted.

<img width="1277" alt="Screenshot 2024-05-04 at 8 41 44 PM" src="https://github.com/TCNJ-degoodj/project-group01/assets/122068476/12b8dac5-c578-4539-9088-da0334eb2525">

### Stake holder topic: goat weaning and winter averages.

<img width="1279" alt="Screenshot 2024-05-04 at 8 42 25 PM" src="https://github.com/TCNJ-degoodj/project-group01/assets/122068476/092f7265-bcfe-4d6c-af68-9a9405e0daa4">

# Project Overview: 

- Our goal with this project was to create a database to store goat data and display the weights of goats over
        there life span. We also will do some calculations on the weights to help provide a prediction for how the
        goats should grow overtime. We also created some tables to show how certain traits can correlate to weights.
