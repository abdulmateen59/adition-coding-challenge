
## TASK 04
Dump out of HDFS is missing some entries (that are in the dump out of MySQL). The logs differ in format so they cannot be compared directly.
- Find the missing entries and explain us how you did so.
- Find a pattern that will make it easier for us to identify the source of the problem.\

## Findings
- Hadoop is missing `16` records, and there is a record with id `6221538613950677149` that exists in Hadoop but not in Mysql.
    - To see that specific record uncomment line `68`.
- Missing records have a certain pattern i.e.
    - all missing records is of content-type `JAVASCRIPT`
    - There `secreen_resoultion` is `(10, 182, 184, 175, 0, -1)`
    - And the `browser` is `(8, 6, 12)`