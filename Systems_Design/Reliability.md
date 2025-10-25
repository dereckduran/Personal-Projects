# Reliability

Reliability is the capacity for a system to continue working when things go wrong. Faults in this context means componenets deviating from their specs. Failures are complete stops in service to users. For example, a sudden spike in traffic is a fault,

## Types

### Hardware Faults
Hard disks crash, faulty RAMs, power grid blackout, somebody unplugs the wrong cable...
Redundancy helps tolerates these faults by adding extra components to serve as backups while the pieces are fixed

### Software Faults
Bugs, race conditions, noisy neighbors, persistent monoliths...
Carefully think about assumptions and interactions
Test the system, integration & unit tests
### Human Errors
Design systems that minimize the opportunity for error 
Use sanbox envs
Test thouroughly
Proper DevOps for rollbacks and continuos code integrations
Detailed and clear monitoring

