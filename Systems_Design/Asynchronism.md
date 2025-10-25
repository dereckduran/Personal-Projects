# Asynchronism vs Synchronism

Asynchronous workflows help reduce request times for expensive operations that would otherwise be performed in-line. They can also help by doing time-consuming work in advance, such as periodic aggregation of data.

Martin Fowler has a great blog on approaching the decision to build microservices. Once decided, a microservice architecture requires careful deliberation around its execution flow style. For a write, heavy system asynchronous is the best bet with a sync-over-async wrapper. Whereas, for a read-heavy system, synchronous communication works well.

CQRS, or Command Query Responsibility Segregation, is a software architecture pattern that separates read and write operations into distinct models. This allows for optimized performance and scalability by using different data models for commands (which modify data) and queries (which retrieve data)



## Synchronous

Synchronous communication is a style of communication where the caller waits until a response is available. It is a prominent and widely used approach. Its conceptual simplicity allows for a straightforward implementation making it a good fit for most of the situations.

Synchronous communication is closely associated with HTTP protocol. However, other protocols remain an equally reasonable way to implement synchronous communication. A good example of an alternative is RPC calls. Each component exposes a synchronous interface that other services call.

An interceptor near the entry point intercepts the business flow request. It then pushes the request to downstream services. All the subsequent calls are synchronous in nature. These calls can be parallel or sequential until processing is complete. Handling of the calls within the system can vary in style. An orchestrator can explicitly orchestrate all the calls. Or calls can percolate organically across components. Let’s look at few possible mechanisms.

### Trade offs

Although, synchronous calls are simpler to grasp, debug and implement, there are certain trade-offs which are worth acknowledging in a distributed setup.

Balanced capacity

It requires a deliberate balancing of the capacity for all the services. A temporary burst at one component can flood other services with requests. In asynchronous style, queues can mitigate temporary bursts. Synchronous communication lacks this mediation and requires service capacity to match up during bursts. Failing this, a cascading failure is possible. Alternatively, resilience paradigms like circuit breakers can help mitigate a traffic burst in a synchronous system.

Risk of cascading failures

Synchronous communication leaves upstream services susceptible to cascading failure in a microservices architecture. If downstream service fail or worst yet, take too long to respond back, the resources can deplete quickly. This can cause a domino effect for the system. A possible mitigation strategy can involve consistent error handling, sensible timeouts for connections and enforcing SLAs. In a synchronous environment, the impact of a deteriorating service ripple through other services immediately. As mentioned previously, prevention of cascading errors can happen by implementing a bulkhead architecture or with circuit breakers.

Increased load balancing & service discovery overhead

The redundancy and availability needs for a participating service can be addressed by setting them up behind a load balancer. This adds a level of indirection per service. Additionally, each service needs to participate in a central service discovery setup. This allows it to push its own address and resolve the address of the downstream services.

Coupling

A synchronous system can exhibit much tighter coupling over a period of time. Without abstractions in between, services bind directly to the contracts of the other services. This develops a strong coupling over a period of time. For simple changes in the contract, the owning service is forced to adopt versioning early on. Thereby increasing the system complexity. Or it trickles down a change to all consumer services which are coupled to the contract.

With emerging architectural paradigms like service mesh, it is possible to address some of the stated issues. Tools like Istio, Linkerd, Envoy etc. allow for a service mesh creation. This space is maturing and remains promising. It can help build systems that are synchronous, more decoupled and fault tolerant.


## Asynchronous

Asynchronous communication is well suited for a distributed architecture. It removes the need to wait for a response thereby decoupling the execution of two or more services. Implementation of asynchronous communication is possible with several variations. Direct calls to a remote service over RPC (for instance grpc) or via a mediating message bus are few examples. Both orchestrated message passing and event choreography use message bus as a channel.

One of the advantages of a central message bus is consistent communication and message delivery semantics. This can be a huge benefit over direct asynchronous communication between services. It is common to use a medium like a message bus that facilitates communication consistently across services. The variations of asynchronous communications discussed below will assume a central message pipeline.

### Back Pressure
If queues start to grow significantly, the queue size can become larger than memory, resulting in cache misses, disk reads, and even slower performance. Back pressure can help by limiting the queue size, thereby maintaining a high throughput rate and good response times for jobs already in the queue. Once the queue fills up, clients get a server busy or HTTP 503 status code to try again later. Clients can retry the request at a later time, perhaps with exponential backoff.

### Task Queues

Tasks queues receive tasks and their related data, runs them, then delivers their results. They can support scheduling and can be used to run computationally-intensive jobs in the background.

Celery has support for scheduling and primarily has python support.

### Message Queues

Message queues receive, hold, and deliver messages. If an operation is too slow to perform inline, you can use a message queue with the following workflow:

    An application publishes a job to the queue, then notifies the user of job status
    A worker picks up the job from the queue, processes it, then signals the job is complete

The user is not blocked and the job is processed in the background. During this time, the client might optionally do a small amount of processing to make it seem like the task has completed. For example, if posting a tweet, the tweet could be instantly posted to your timeline, but it could take some time before your tweet is actually delivered to all of your followers.

    Redis is useful as a simple message broker but messages can be lost.
    RabbitMQ is popular but requires you to adapt to the 'AMQP' protocol and manage your own nodes.
    AWS SQS is hosted but can have high latency and has the possibility of messages being delivered twice.
    Apache Kafka is a distributed event store and stream-processing platform.


### Trade Offs

Service flows that are asynchronous in nature can be hard to follow through the system. There are some trade-offs that a system adopting asynchronous communication will make. Let’s look at some of them.

Higher system complexity

Asynchronous systems tend to be significantly more complex than synchronous ones. However, the complexity of system and demands of performance and scale are justified for the overhead. Once adopted both orchestrator and individual components need to embrace the asynchronous execution.

Reads/Queries require mediation

Unless handled specifically synchronous consumers are most affected by an asynchronous architecture. Either the consumers need to adapt to work with an asynchronous system, or the system should present a synchronous interface for the consumers.

Asynchronous architecture is a natural fit for the write-heavy system. However, it needs mediation for synchronous reads/queries. There are several ways to manage this need. Each one has certain complexity associated with it.

Sync wrapper

Simplest of all approaches is building a sync wrapper over an async system. This is an entry point that can invoke asynchronous flows downstream. At the same time, it holds the request awaiting until the response returns or a timeout occurs. A synchronous wrapper is a stateful component. An incoming request ties itself to the server it lands on. The response from downstream services needs to arrive at the server where original request is waiting. This isn’t ideal for a distributed system, especially one that operates at scale. However, it is simple to write and easy to manage. For a system with reasonable scaling and performance needs it can fit the bill. A sync wrapper should be a consideration before a more drastic restructuring.

Dual support

There is a middle ground here between a sync wrapper and a CQRS implementation. Each service/component can support synchronous queries and asynchronous writes. This works well for a system which is operating at a medium scale. So read queries can hop between components to finish reads synchronously. Writes to the system, on the other hand, will flow down asynchronous channels. There is a trade-off here though. The optimization of a system for both reads and writes independently is not possible. Something, that is beneficial for a system operating at high traffic.

Message bus is a central point of failure

This is not a trade-off, but a precaution. In the asynchronous communication style, message bus is the backbone of the system. All services constantly produce-to and consume-from the message bus. This makes the message bus the Achilles heel of the system as it remains a central point of failure. It is important for a message bus to support horizontal scaling otherwise it can work against the goals of a distributed system.

Eventual consistency

An asynchronous system can be eventually consistent. It means that results in queries may not be latest, even though the system has issued the writes. While this trade-off allows the system to scale better, it is something to factor-in into system’s design and user experience both.

#### References
https://medium.com/inspiredbrilliance/patterns-for-microservices-e57a2d71ff9e