```sql
-- ------------------------------------------------------------
-- Use the ACCOUNTADMIN role
-- ------------------------------------------------------------
USE ROLE ACCOUNTADMIN;

-- ------------------------------------------------------------
-- Create and assign roles
-- ------------------------------------------------------------
CREATE ROLE IF NOT EXISTS dbt_role;
GRANT ROLE dbt_role TO ROLE ACCOUNTADMIN;

-- ------------------------------------------------------------
-- Create warehouse and grant privileges
-- ------------------------------------------------------------
CREATE WAREHOUSE IF NOT EXISTS dbt_warehouse;
GRANT OPERATE ON WAREHOUSE dbt_warehouse TO ROLE dbt_role;
GRANT ALL ON WAREHOUSE dbt_warehouse TO ROLE dbt_role;

-- ------------------------------------------------------------
-- Create user and assign role
-- ------------------------------------------------------------
CREATE USER IF NOT EXISTS dbt_user
  PASSWORD = 'StrongPasword'
  LOGIN_NAME = 'dbt'
  DEFAULT_WAREHOUSE = 'dbt_warehouse'
  DEFAULT_ROLE = dbt_role        -- Updated default role to dbt_role
  MUST_CHANGE_PASSWORD = FALSE;

GRANT ROLE dbt_role TO USER dbt_user;

-- ------------------------------------------------------------
-- Create database and schema; grant privileges
-- ------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS AIRBNB;
CREATE SCHEMA IF NOT EXISTS AIRBNB.AIRBNB_DATA;

GRANT ALL ON DATABASE AIRBNB TO ROLE dbt_role;
GRANT ALL ON ALL SCHEMAS IN DATABASE AIRBNB TO ROLE dbt_role;
GRANT ALL ON FUTURE SCHEMAS IN DATABASE AIRBNB TO ROLE dbt_role;
GRANT ALL ON ALL TABLES IN SCHEMA AIRBNB.AIRBNB_DATA TO ROLE dbt_role;
GRANT ALL ON FUTURE TABLES IN SCHEMA AIRBNB.AIRBNB_DATA TO ROLE dbt_role;

-- ------------------------------------------------------------
-- Create stage for file ingestion
-- ------------------------------------------------------------
CREATE STAGE IF NOT EXISTS AIRBNB_STAGE;

-- (Optional) To view stage details:
-- DESC STAGE AIRBNB_STAGE;
-- LIST @AIRBNB_STAGE;

-- ------------------------------------------------------------
-- Create file formats for CSV ingestion
-- ------------------------------------------------------------

CREATE OR REPLACE FILE FORMAT AIRBND_FILE_FORMAT
  TYPE = 'CSV'
  PARSE_HEADER = TRUE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE FILE FORMAT AIRBND_FILE_FORMAT_COPY_INTO_TABLE
  TYPE = 'CSV'
  PARSE_HEADER = FALSE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  SKIP_HEADER = 1;

-- ------------------------------------------------------------
-- Create and load temporary table: REVIEWS_DETAILS
-- ------------------------------------------------------------
CREATE OR REPLACE TEMPORARY TABLE REVIEWS_DETAILS (
    listing_id   INTEGER,
    id           INTEGER,
    review_date  TIMESTAMP,
    reviewer_id  STRING,
    reviewer_name STRING,
    comments     STRING
);

COPY INTO REVIEWS_DETAILS (
  listing_id,
  id,
  review_date,
  reviewer_id,
  reviewer_name,
  comments
)
FROM @AIRBNB_STAGE
FILES = ('reviews_details.csv')
FILE_FORMAT = (FORMAT_NAME = 'AIRBND_FILE_FORMAT_COPY_INTO_TABLE');

-- ------------------------------------------------------------
-- Create and load temporary table: listings
-- ------------------------------------------------------------
CREATE OR REPLACE TEMPORARY TABLE listings (
    id                    INTEGER,
    name                  STRING,
    host_id               INTEGER,  
    host_name             STRING,
    neighbourhood_group   STRING,
    neighbourhood         STRING,
    latitude              FLOAT,
    longitude             FLOAT,
    room_type             STRING,
    price                 DECIMAL(10,2),
    minimum_nights        INTEGER,
    number_of_reviews     INTEGER,
    last_review_date      TIMESTAMP,
    reviews_per_month     FLOAT,
    calculated_listings   INTEGER,
    availability_365      INTEGER
);

COPY INTO listings (
  id,
  name,
  host_id,
  host_name,
  neighbourhood_group,
  neighbourhood,
  latitude,
  longitude,
  room_type,
  price,
  minimum_nights,
  number_of_reviews,
  last_review_date,
  reviews_per_month,
  calculated_listings,
  availability_365
)
FROM @AIRBNB_STAGE
FILES = ('listings.csv')
FILE_FORMAT = (FORMAT_NAME = 'AIRBND_FILE_FORMAT_COPY_INTO_TABLE');

-- ------------------------------------------------------------
-- Create and load temporary table: calendar
-- ------------------------------------------------------------
CREATE OR REPLACE TEMPORARY TABLE calendar (
    listing_id    INTEGER,
    calendar_date TIMESTAMP,
    available     BOOLEAN,
    price         STRING
);

COPY INTO calendar (
  listing_id,
  calendar_date,
  available,
  price
)
FROM @AIRBNB_STAGE
FILES = ('calendar.csv')
FILE_FORMAT = (FORMAT_NAME = 'AIRBND_FILE_FORMAT_COPY_INTO_TABLE');

-- ------------------------------------------------------------
-- Create and load temporary table: reviews
-- ------------------------------------------------------------
CREATE OR REPLACE TEMPORARY TABLE reviews (
    listing_id   INTEGER,
    reviews_date TIMESTAMP
);

COPY INTO reviews (
  listing_id,
  reviews_date
)
FROM @AIRBNB_STAGE
FILES = ('reviews.csv')
FILE_FORMAT = (FORMAT_NAME = 'AIRBND_FILE_FORMAT_COPY_INTO_TABLE');

-- ------------------------------------------------------------
-- Grant SELECT privilege on REVIEWS_DETAILS to dbt_role
-- ------------------------------------------------------------
GRANT SELECT ON REVIEWS_DETAILS TO ROLE dbt_role;
```

