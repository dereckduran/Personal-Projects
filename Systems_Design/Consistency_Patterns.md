# Consistency Partterns

When working with distributed systems, we need to think about managing the data across different servers. 

Consistency patterns refer to the ways in which data is stored and managed in a distributed system and how that data is made available to users and applications

## Strong Consistency
    After an update is made to the data, it will be immediately visible to any subsequent read operations. The data is replicated in a synchronous manner, ensuring that all copies of the data are updated at the same time.

highly available and has high latency

## Weak Consistency
    After an update is made to the data, it is not guaranteed that any subsequent read operation will immediately reflect the changes made. The read may or may not see the recent write.

high availability and low latency.

## Eventual Consistency
    Eventual consistency is a form of Weak Consistency. After an update is made to the data, it will be eventually visible to any subsequent read operations. The data is replicated in an asynchronous manner, ensuring that all copies of the data are eventually updated.

highly available and has low latency, but it also means that there may be inconsistencies and conflicts between different versions of the data.

#### References
https://cs.fyi/guide/consistency-patterns-week-strong-eventual
