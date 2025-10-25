# Load Balancers

Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:

    Preventing requests from going to unhealthy servers
    Preventing overloading resources
    Helping to eliminate a single point of failure

Load balancers can be implemented with hardware (expensive) or with software such as HAProxy. Additional benefits include:

    SSL termination - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
        Removes the need to install X.509 certificates on each server
    Session persistence - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions

Disadvantages of load balancer

    The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
    Introducing a load balancer to help eliminate a single point of failure results in increased complexity.
    A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.


## Algorithms
Dynamic load balancing algorithms: Dynamic load balancing uses algorithms that take into account the current state of each server and distribute traffic accordingly

    Least connection: Checks which servers have the fewest connections open at the time and sends traffic to those servers. This assumes all connections require roughly equal processing power.
    Weighted least connection: Gives administrators the ability to assign different weights to each server, assuming that some servers can handle more connections than others.
    Weighted response time: Averages the response time of each server, and combines that with the number of connections each server has open to determine where to send traffic. By sending traffic to the servers with the quickest response time, the algorithm ensures faster service for users.
    Resource-based: Distributes load based on what resources each server has available at the time. Specialized software (called an "agent") running on each server measures that server's available CPU and memory, and the load balancer queries the agent before distributing traffic to that server.

Static load balancing algorithms:  distributes traffic without making these adjustments.

    Round robin: Round robin load balancing distributes traffic to a list of servers in rotation using the Domain Name System (DNS). An authoritative nameserver will have a list of different A records for a domain and provides a different one in response to each DNS query.
    Weighted round robin: Allows an administrator to assign different weights to each server. Servers deemed able to handle more traffic will receive slightly more. Weighting can be configured within DNS records.
    IP hash: Combines incoming traffic's source and destination IP addresses and uses a mathematical function to convert it into a hash. Based on the hash, the connection is assigned to a specific server


## Layer 7 Load Balancing

Layer 7 load balancers look at the application layer to decide how to distribute requests. This can involve contents of the header, message, and cookies. Layer 7 load balancers terminate network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.

Start with this one because og the high availability, session stickiness, websockets, content-based routing, container based apps. Use until you can find a valid reason not to. 

At the cost of flexibility, layer 4 load balancing requires less time and computing resources than Layer 7, although the performance impact can be minimal on modern commodity hardware.

## Layer 4 Load Balancing

Layer 4 load balancing uses information defined at the networking transport layer (Layer 4) as the basis for deciding how to distribute client requests across a group of servers. For Internet traffic specifically, a Layer 4 load balancer bases the load-balancing decision on the source and destination IP addresses and ports recorded in the packet header, without considering the contents of the packet.

Today the term “Layer 4 load balancing” most commonly refers to a deployment where the load balancer’s IP address is the one advertised to clients for a web site or service (via DNS, for example). As a result, clients record the load balancer’s address as the destination IP address in their requests.

When the Layer 4 load balancer receives a request and makes the load balancing decision, it also performs Network Address Translation (NAT) on the request packet, changing the recorded destination IP address from its own to that of the content server it has chosen on the internal network. Similarly, before forwarding server responses to clients, the load balancer changes the source address recorded in the packet header from the server’s IP address to its own. (The destination and source TCP port numbers recorded in the packets are sometimes also changed in a similar way.)

## Horizontal Scaling

Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called Vertical Scaling. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.
Disadvantages of horizontal scaling

    Scaling horizontally introduces complexity and involves cloning servers
        Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
        Sessions can be stored in a centralized data store such as a database (SQL, NoSQL) or a persistent cache (Redis, Memcached)
    Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out.



#### References
https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/
https://www.f5.com/glossary/layer-4-load-balancing