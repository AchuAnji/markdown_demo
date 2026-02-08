# Architecture Decision Records

## Title
Overall System Architecture for Internal Quality Dashboard

## Status
Accepted

## Context
This project is an internal web application for a fictional manufacturing company (SteelWorks, LLC).
The system will be used by operators, engineers, and managers to analyze inspection and defect data.

Key constraints and inputs:
- Small user base (single user or small team)
- Internal business application
- Data volume in the range of hundreds to thousands of rows
- Excel files act as the source of truth
- No real-time processing requirements
- Small development team (1–2 developers)
- Timeline measured in weeks

## Decision
We will use a **Client–Server, Monolithic, Layered architecture** with:
- Synchronous request–response interaction
- A single database
- Server-side business logic handling data aggregation and analysis

## Alternatives Considered
- **Event-driven architecture**: Rejected due to lack of real-time or cross-system integration needs
- **Microservices architecture**: Rejected due to unnecessary operational complexity for a small internal tool
- **Asynchronous processing**: Rejected since users expect immediate responses for analysis queries

## Consequences

### Positive
- Simple to understand, build, and maintain
- Fast development with minimal operational overhead
- Well-suited for internal tools and reporting use cases
- Easy debugging and deployment

### Negative
- Limited scalability for future high-concurrency use cases
- Tight coupling between components
- Harder to evolve into distributed systems without refactoring
