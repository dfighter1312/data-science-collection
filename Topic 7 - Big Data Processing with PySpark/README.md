# Topic 7 - Working with PySpark

## What this repository do?

This is a simple demonstration of PySpark. There are 3 sets of practice on PySpark that I worked with.

- Set 1: PySpark fundmental courses notes. You can find it from `.ipynb` files starting with the letter `c` and a number (c1, c2, c3, c4, c7).
- Set 2: Practice with the social bot dataset. The dataset I am referring to is the Twibot-22 dataset with 1 million users and over 80 million tweets for processing.
- Set 3: Real time streaming applictaion. The instruction to run can be found as below.

## How to run this repository?

### Spark SQL Dataframe

**Step 1:** Go to the directory
```bash
cd "Topic 7 - Big Data Processing with PySpark"
```

**Step 2:** Install `pyspark`. You may encounter several problems during installation and they depend on your OS, therefore, please go to [Pyspark documentation page](https://spark.apache.org/docs/latest/api/python/getting_started/install.html).

**Step 3:** Run the notebook `pyspark_basics.ipynb`.

### Streaming

(If step 1 and 2 in Spark SQL Dataframe are performed) Open 2 terminals.

First terminal:
```bash
nc -lk 8083
```

Second terminal:
```bash
spark-submit real_time_streaming.py localhost 8083
```

Try the text cleaning application by typing some sentences onto the first terminal. The result will be displayed on the second terminal after a moment.

## Pyspark Q&A

**1. What is Spark? Difference between Spark and Hadoop MapReduce**

Apache Spark:
- is a lightning fast real-time processing framework, doing in-memory computations to analyze data in real-time.
- takes care of batch processing as well.
- supports interactive queries and iterative algorithms.
- leverages Apache Hadoop for both storage and processing, which uses HDFS for storage.

Different between Spark and Hadoop:
- Hadoop is based on the concept of batch processing where the processing happens of blocks of data that have already been stored over a period of time.
- Spark can process data in real-time and is about 100x faster than Hadoop MapReduce in batch processing large data sets.

**2. What is PySpark?**

Apache Spark is written in *Scala*, therefore, in order to support Python with Spark, PySpark is released building on *Py4j* library.

**3. What is SparkContext?**

SparkContext is the entry point to any Spark functionality (from version 2.0). SparkContext uses Py4J to launch a JVM and creates a JavaSparkContext.

**4. What is RDD?**

RDD (Resilent Distributed Dataset), which includes elements that run and operate on multiple nodes to do parallel processing on a cluster. RDDs are immutable elements (cannot be changed).

Operations on RDD:
- Transformation: join, union, filter, map on existing RDDs will produce a new RDD. Transformations are lazy (not execute RDD immediately but instead a lineage is created that tracks all the transformations to be applied on a RDD).
- Action: count, first, reduct which returns values after computations.

**5. What is the difference between an RDD, a Dataframe and a Dataset?**

|  | **RDD** | **DataFrame** | **Dataset** |
|---|---|---|---|
| **Definition** | Read-only partition collection of records | Organized data with columns and rows | An extension of DataFrame API which provides type-safe, object-oriented programming interface. |
| **Released Version** | 1.0 and above | 1.3 and above | 1.6 and above |
| **Data Representation** | Distributed collection of data elements spread across many machines in the cluster. | Distributed collection of data organized into named columns |  |
| **Data Formats** | Structured and unstructured | Structured | Structured and unstructured |
| **Data Source** | Any sources | AVRO, CSV, JSON, and storage system HDFS, HIVE tables, MySQL | Any sources |
| **Immutability and Interoperability** | Immutable (Immutability helps to achieve consistency in computations). Can move from RDD to DataFrame (If RDD is in tabular format) by toDF() method or we can do the reverse by the .rdd method. | After transforming into DataFrame one cannot regenerate a domain object. For example, if you generate testDF from testRDD, then you won’t be able to recover the original RDD of the test class. | Can convert the existing RDD and DataFrames into Datasets. |
| **Compile-time type safety** | Yes | No | Yes |
| **Optimization** | Not available | Optimization takes place using catalyst optimizer. | Optimization takes place using catalyst optimizer. |
| **Lazy Evaluation** | The system just remembers the transformation applied to some base data set.  Spark computes Transformations only when an action needs a result to sent to the driver program. | Computation happens only when action appears. | Computation happens only when action appears. |
| **Aggregation Speed** | Slow | Fast | Very Fast |
| **Supported Programming Languges** | Java, Scala, Python, and R | Java, Scala, Python, and R | Scala and Java |
| **Schema Projection** | Manually defined | Automatically defined | Automatically defined |

**6. What is the differences between a PySpark Dataframe and a Pandas Dataframe?**

| **Pandas DataFrame** | **Spark DataFrame** |
|---|---|
| Single Node | Multiple Nodes |
| Eager Execution (computation is executed immediately) | Lazy Execution (Computation isn't executed until necessary which allows optimization of tasks across cluster) |
| Constraint by Computer Hardware | Scales Horizontally by adding more nodes |
| Computation done in-memory | Computation done in-memory |
| Data is mutable | Data is immutable |
| Api offers more operations and methods | Methods require additional programming to enable parallel computing |

Performance comparison between Pandas and Spark depends on the infrastructure and the use-cases. With an extra-large amount of data and a powerful computation system, Spark can achieve a relatively high performance compared to Pandas. However, using a local machine will output a lower stability on Spark.

## References

- [PySpark tutorial for beginners](https://sparkbyexamples.com/pyspark-tutorial/)
- [Benchmarking Pandas vs. Spark](https://hirazone.medium.com/benchmarking-pandas-vs-spark-7f7166984de2)
- [Beginners Guide to PySpark](https://towardsdatascience.com/beginners-guide-to-pyspark-bbe3b553b79f)
- [Pandas DataFrame vs. Spark DataFrame: When Parallel Computing Matters](https://towardsdatascience.com/parallelize-pandas-dataframe-computations-w-spark-dataframe-bba4c924487c)
- [Apache Spark RDD vs DataFrame vs DataSet](https://data-flair.training/blogs/apache-spark-rdd-vs-dataframe-vs-dataset/#:~:text=Spark%20Dataframe%20APIs%20%E2%80%93%20Unlike%20an,%2C%20allowing%20higher%2Dlevel%20abstraction.)
- [Tutorialspoint - PySpark tutorial](https://www.tutorialspoint.com/pyspark/index.htm)
- [Spark Real-time Streaming](https://hevodata.com/learn/spark-real-time-streaming/)

## Must-read material

- [Apache Spark with Python: Big Data with PySpark and Spark](https://www.oreilly.com/videos/apache-spark-with/9781789133394/)