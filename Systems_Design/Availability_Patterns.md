# Availability Patterns

Availability patterns are established architectural approaches used to ensure a system remains operational and accessible to users, even in the face of failures or unexpected events.

These patterns focus on minimizing downtime and maintaining a consistent level of service by incorporating *redundancy, fault tolerance, and recovery* mechanisms into the system's design. They provide a structured way to address potential points of failure and ensure business continuity.

High availability refers to the ability of a system to remain operational and accessible even in the face of failures or disruptions.

It often measured in terms of uptime of the system

### Scalability 
Horizontal scalability refers to the ability to add more servers or nodes to distribute the workload, while vertical scalability involves adding more resources to a single server or node.

Load balancing ensures that the workload is evenly distributed among multiple servers, preventing any single server from becoming a bottleneck.

Partitioning involves dividing the data into smaller subsets and distributing them across multiple servers, allowing for parallel processing and improved performance.

Caching helps reduce the load on the database by storing frequently accessed data in memory, resulting in faster response times.

Database optimization involves tuning the database to improve its performance and efficiency.

### Reliability
focuses on minimizing the occurrence and impact of failures.

Error-handling mechanisms are designed to handle unexpected errors and exceptions that may occur during the operation of a system. These mechanisms include error logging, graceful error recovery, and fallback mechanisms.

By logging errors, developers can gain insights into potential issues and take necessary actions to rectify them.

Graceful error recovery ensures that the system can gracefully handle errors without crashing or causing data loss.

Fallback mechanisms provide alternative paths or resources to ensure uninterrupted service in case of failures.

Fault-tolerant architectures are designed to minimize the impact of hardware or software failures on system performance. These architectures often involve redundancy, where multiple instances of critical components are deployed to ensure continuous operation even if one or more instances fail.

Redundancy can be achieved through techniques such as clustering, replication, and failover mechanisms.


## Strategies for High Availability

### Redundancy and Replication
By duplicating critical components or entire systems, organizations can ensure that if one fails, the redundant system takes over seamlessly, avoiding any interruption in service.

Replication involves creating multiple copies of data, ensuring that it is available even if one copy becomes inaccessible.

Redundancy and replication are commonly used in mission-critical systems such as data centers, where multiple servers are deployed to handle the workload.

### Load Balancing
Disributes workloads across multiple servers, ensuring that no single server is overwhelmed.

#### Load Balancing Strategies
Round Robin

    How it Works: Requests are distributed sequentially and equally across the servers in a rotation.
    Use Case: Effective for servers with similar specifications and when the load is evenly distributed.

Least Connections

    How it Works: Directs traffic to the server with the fewest active connections.
    Use Case: Useful when there are long-lived connections and the load varies significantly across servers.

Least Response Time

    How it Works: Sends requests to the server with the lowest average response time and fewest active connections.
    Use Case: Suitable for ensuring quick response times when server performance varies.

IP Hash

    How it Works: A hash of the IP address of the client is calculated to direct the request to a particular server.
    Use Case: Ensures that a particular user will consistently connect to the same server.

Weighted Round Robin

    How it Works: An extension of the round robin algorithm, but with servers assigned a weight. Servers with higher weights receive more connections.
    Use Case: Ideal when servers have different capacities.

Weighted Least Connections

    How it Works: Similar to the least connections method but takes server capacity into account, where each server is assigned a weight.
    Use Case: Useful for a group of servers with varying capacities.

Random

    How it Works: Requests are randomly distributed across the servers.
    Use Case: Can be effective when the load is low and the distribution doesn't need to be finely tuned.

Source IP Affinity (Session Affinity or Sticky Sessions)

    How it Works: Requests from a specific IP address are sent to the same server. This maintains session consistency.
    Use Case: Useful when it's important to keep a user connected to the same server (e.g., where session state is stored locally on the server).

Geographic

    How it Works: Traffic is directed to the server geographically closest to the user.
    Use Case: Reduces latency by serving users from a location near them; important for global services.

### Failover Clustering
A cluster of servers that work together to provide redundancy and seamless failover.

If one server fails, another server in the cluster takes over its responsibilities. This ensures continuous availability and a smooth transition for users.

#### Patterns

*Fail-Over*
Active-Active: Both primary and secondary components are active, handling requests simultaneously.
Active-Passive: The secondary component is inactive until the primary fails.
Disadvantages of Failover

    Fail-over adds more hardware and additional complexity.
    There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.


*Replication*
Leader-Leader: both systems can serve as both the primary and secondary components. They can handle both read and
writes. This type of replication can lead to conflicts if multiple servers update the same data at the same time, so some conflict resolution mechanism is needed to handle this.
Leader-Follower: write operations, providing high availability and fault tolerance.
one system acts as the leader, handling write operations, while the others (followers) replicate the data for read operations. This provides data redundancy and offloads read traffic from the master.


### Distributed Data Storage
Storing data across multiple locations or data centers

## Factors Affecting Availability
Network Connectivity:
Imagine an online banking system. If there's a network outage in a specific region, customers in that area will be unable to access their accounts or perform transactions.

Hardware and Software Failures:
A data center experiencing a power outage can lead to hardware failures and system downtime. Additionally, software bugs or vulnerabilities can cause crashes or unexpected behavior.

Scalability Issues:
During peak shopping seasons, an e-commerce website may experience a surge in traffic. If the system is not designed to scale effectively, it could become overwhelmed and experience slowdowns or outages.

Security Breaches:
A ransomware attack on a healthcare provider's network could encrypt patient data, making it inaccessible and disrupting critical operations.

External Dependencies:
 A social media platform relies on third-party services for image hosting and video streaming. If these services experience downtime, the social media platform's functionality will be affected.


#### References
https://www.designgurus.io/blog/high-availability-system-design-basics
https://www.designgurus.io/answers/detail/what-are-different-load-balancer-algorithms
https://dev.to/decoders_lord/system-design-availability-patterns-104i