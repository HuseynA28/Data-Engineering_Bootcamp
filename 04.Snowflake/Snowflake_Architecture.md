# Snowflake Architecture Overview

Snowflake’s architecture is a hybrid of traditional shared-disk and shared-nothing database designs. It utilizes a central data repository for persistent storage (like shared-disk systems) and processes queries via massively parallel processing (MPP) compute clusters (like shared-nothing systems).

Below is an overview of Snowflake's architecture:

![Architecture Overview](/04.Snowflake/Snowflake_documentation/architecture-overview.png)

Snowflake’s architecture consists of three key layers:

1. **Database Storage**
2. **Query Processing**
3. **Cloud Services**

---

## 1. Database Storage Layer

This layer is responsible for storing all persistent data, including tables and query results.

### Data Storage Format

- **Columnar Format:**  
  Data is stored in columns, which improves query performance.
  
- **Micro-partitions:**  
  Data is automatically divided into micro-partitions, each containing between 50 MB and 500 MB of uncompressed data (the actual stored size is smaller due to compression).

### Data Management

- **Automatic Management:**  
  Snowflake manages data organization, file sizing, compression, metadata, and statistics automatically.

- **Clustering (Cluster Keys):**  
  For large tables, you can define cluster keys to enhance query performance.  
  - **What is a Cluster Key?**  
    A cluster key organizes data within micro-partitions based on one or more columns. When defined, Snowflake automatically re-clusters the data to minimize the number of micro-partitions scanned during queries.

### Micro-partitions & Data Clustering

Snowflake stores metadata for every micro-partition, including:

- The range of values for each column.
- The number of distinct values.
- Additional properties used for both optimization and efficient query processing.

![Clustering and Micro-partitions](/Snowflake_documentation/clustering.png)

**Benefits of Micro-partitioning:**

- **Automatic Derivation:**  
  Micro-partitions are created automatically.
  
- **Efficient Compression:**  
  Snowflake determines the most efficient compression algorithm for each column.
  
- **Independent Column Storage:**  
  Each column is stored independently, which optimizes query performance.

### Handling Dropped Columns

- **Dropping a Column:**  
  When a column is dropped, the micro-partitions containing its data are **not** immediately re-written. The dropped data remains until a write operation (insert, update, delete, etc.) causes the micro-partition to be re-written.

- **Reclaiming Space Immediately:**  
  To force space reclamation:
  1. Use a `CREATE TABLE AS SELECT (CTAS)` statement to create a new table containing only the desired columns.
  2. Optionally, set the `DATA_RETENTION_TIME_IN_DAYS` parameter to 0 for the old table.
  3. Drop the old table.

---

## 2. Query Processing Layer

This layer is where your queries (written in SQL, Python, etc.) are executed using virtual warehouses.

### Virtual Warehouses

- **Compute Clusters:**  
  Queries are processed by virtual warehouses, which are compute clusters that can be scaled up or down with ease.
  
- **Auto-Suspend & Auto-Resume:**  
  These features optimize resource usage by suspending warehouses when idle and resuming them when needed.

### Scalability & Concurrency

- **Multi-cluster Warehouses:**  
  Ideal for improving query concurrency. They allow additional clusters to be added during periods of high demand.
  
- **Scaling Policies:**
  - **Standard (Default):**
    - The first cluster starts immediately when a query is queued.
    - Each subsequent cluster starts 20 seconds after the previous one.
    - Scaling adjustments are made after 2–3 consecutive successful checks (performed at 1-minute intervals).
  - **Economy:**
    - Additional clusters are launched only if the system estimates that the new cluster will remain busy for at least 6 minutes.
    - Scaling decisions are based on 5–6 consecutive successful checks (at 1-minute intervals).

- **Note:**  
  Multi-cluster warehouses are best for boosting concurrency. For slow-running queries or data loading, resizing the warehouse is often more beneficial.

---

## 3. Cloud Services Layer

This layer acts as the "brain" of Snowflake, coordinating system operations and managing various services.

### Key Responsibilities

- **Query Optimization:**  
  Coordinates and optimizes query execution.

- **Infrastructure Management:**  
  Oversees the underlying cloud infrastructure.

- **Metadata Management:**  
  Maintains data statistics and metadata to improve performance.

- **Security & Access Control:**  
  Handles authentication and enforces access policies.

- **Serverless Tasks:**  
  Manages tasks such as Snowpipe, scheduled tasks, materialized views, and routine maintenance.

> **Note:** Users cannot modify this layer; it is fully managed by Snowflake to ensure optimal performance, security, and reliability.

---

