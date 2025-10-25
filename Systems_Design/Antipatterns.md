# Performance Antipatterns

Performance antipatterns in system design refer to common mistakes or suboptimal practices that can lead to poor performance in a system. These patterns can occur at different levels of the system and can be caused by a variety of factors such as poor design, lack of optimization, or lack of understanding of the workload.

Some of the examples of performance antipatterns include:

    N+1 queries: This occurs when a system makes multiple queries to a database to retrieve related data, instead of using a single query to retrieve all the necessary data.
    Chatty interfaces: This occurs when a system makes too many small and frequent requests to an external service or API, instead of making fewer, larger requests.
    Unbounded data: This occurs when a system retrieves or processes more data than is necessary for the task at hand, leading to increased resource usage and reduced performance.
    Inefficient algorithms: This occurs when a system uses an algorithm that is not well suited to the task at hand, leading to increased resource usage and reduced performance.

## Improper Instantiation
Sometimes new instances of a class are continually created, when it is meant to be created once and then shared. This behavior can hurt performance and is called an improper instantiation antipattern. An antipattern is a common response to a recurring problem that is usually ineffective and might be counter-productive.
Problem description

Many libraries provide abstractions of external resources. Internally, these classes typically manage their own connections to the resource, acting as brokers that clients can use to access the resource. 

How to fix: If the class that wraps the external resource is shareable and thread-safe, create a shared singleton instance or a pool of reusable instances of the class.

## Monolithic Persistence
### Context and problem

Historically, applications used a single data store, regardless of the different types of data that the application might need to store. Organizations used this method to simplify the application design or to match the existing skill set of the development team.

Modern cloud-based systems often have extra functional and nonfunctional requirements. These systems need to store many heterogeneous types of data, such as documents, images, cached data, queued messages, application logs, and telemetry. Following the traditional approach and putting all this information into the same data store can weaken performance for two main reasons:

    Storing and retrieving large amounts of unrelated data in the same data store can cause contention, which leads to slow response times and connection failures.
    Regardless of which data store is chosen, it might not be the best fit for all types of data. Or it might not be optimized for the operations that the application performs.

Solution: Separate data according to its use. For each data set, select a data store that best matches how you use that data set. 

## Noisy Neighbor
When you build a service that multiple customers or tenants share, you can build it to be multitenanted. A benefit of multitenant systems is that resources can be pooled and shared among tenants. This resource sharing often results in lower costs and improved efficiency. However, if a single tenant uses a disproportionate amount of the resources available in the system, the overall performance of the system can suffer. The noisy neighbor problem occurs when one tenant's performance is degraded because of the activities of another tenant.

Sharing a single resource inherently carries the risk of noisy neighbor problems that you can't completely avoid. However, there are some steps that both clients and service providers can take to reduce the likelihood of noisy neighbor problems or to mitigate their effects.
    Ensure that your application handles service throttling to reduce making unnecessary requests to the service. 
    Migrate to a single-tenant instance of the service.

## Synchronous I/O
A synchronous I/O operation blocks the calling thread while the I/O completes. The calling thread enters a wait state and is unable to perform useful work during this interval, wasting processing resources.

#### References
https://learn.microsoft.com/en-us/azure/architecture/antipatterns/
https://learn.microsoft.com/en-us/azure/architecture/antipatterns/improper-instantiation/