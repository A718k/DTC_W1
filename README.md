# NYC Taxi Pipeline Homework

This repository contains my homework submission.  

I built AI-assited (basically it did it all xD) **dlt pipeline** to extract, transform, and load NYC Yellow Taxi trip data via a **custom REST API**. Additionally, I utilised AI agent to answer the workshop questions.

---

## Pipeline

- **Source**: REST API serving NYC taxi trip records
- **Destination**: DuckDB local database (`taxi_pipeline.duckdb`)
- **Pagination**: Handled automatically using page number pagination
- **Data Selector**: JSONPath `$[*]` to select trip records from API responses
- **Refresh Mode**: `drop_sources` during testing to clean previous loads

The pipeline fetches all available trip data from the API and loads it into a table named `nyc_taxi`.

---

## Workshop Questions and Answers

**Question 1:** 
![Answer for Q1](images/Q1.png)


**Question 2: What proportion of trips are paid with credit card?**  
**Answer:** 26.66%

**Question 3: What is the total amount of money generated in tips?**  
**Answer:** $6,063.41

> I used a combination of AI-assisted prompts and manual exploration of the dataset to find these answers. The pipeline made it easy to query aggregated results quickly.

---

## Usage

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
