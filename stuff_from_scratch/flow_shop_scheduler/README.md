# Flow Shop Scheduler
Original problem and solution: https://aosabook.org/en/500L/a-flow-shop-scheduler.html  
Benchmarks are also included in the site.

## Problem statement
Flow shop scheduling problem is an optimization problem.  
Imagine a car manufacturer with an assembly line - each part of the car is completed sequentially on different machines.
Here, each car is a new **job**, every job has the same number of **tasks** to complete.

### Variables
Conceptually, we have jobs, tasks, stations. Number of tasks same for all jobs. Number of stations = number of jobs.

**J :** Number of jobs  
**S :** Number of stations (also called machines). Equal to number of tasks under a job (T) 
**P(j, t) :** Processing time of task t under job j  
**Perm :** Permutation of jobs

### Objective
**Minimize** total time taken to complete all jobs, thus minimizing idle time.

### Constraints
**C1:** Task number t is assigned to station s, where s = t.   
**C2:** Task t must be completed before starting t+1, so order of the tasks follow the order of machines available.  
**C3:** One task at a time for any station.  
**C4:** We're constructing a permutation, so a job can have one rank.

### Why is this a problem?
Order of tasks within a job is predetermined, so our solution will be represented as a **permutation of jobs.** 

Consider a simple example with 2 jobs and 2 stations.  
Job1 has tasks A (takes 1 min), B (2 min).  
Job2 has tasks C (2 min), D (1 min).

Recall that Station1 can work on A, C (task number 1). Station2 can work on B, D.

Permutation (Job2, Job1) yields:  
Station1: | C (2 min) | A (1 min) | - (2 min) |  
Station2: | - (2 min) | D (1 min) | B (2 min) |  
Total time: 5 min, Idle time: 2 min

Permutation (Job1, Job2) yields:  
Station1: | A (1 min) | C (2 min) | - (2 min) |  
Station2: | - (1 min) | B (2 min) | D (1 min) |  
Total time: 4 min, Idle time: 1 min

## Constructed solution
We will use **local search** - an approximate optimization approach, trying possible solutions and returning the best.
Local search improves the existing solution heuristically by considering similar solutions (visiting neighbors).

The solver uses a variety of strategies to find similar solutions, and choose the promising one to explore next. It
also dynamically changes its strategy, based on which strategies work well.

The questions we answer:
1. What should be the initial solution?
2. Given a solution, what are neighboring solutions to be considered?
3. Given neighborhood, which neighbor to move to next?
