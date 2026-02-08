# Tech Stack Decision Records

## Title
Tech Stack Selection for Internal Quality Dashboard

## Status
Accepted

## Context
The system architecture is a client–server, monolithic, layered, synchronous application with a single database.
The tech stack must support:
- Rapid development
- Strong AI assistance
- Simple deployment
- Data-driven analysis and reporting
- A clear upgrade path if architecture evolves in the future

## Decision
We will use the following tech stack:

- **Language**: Python
- **Web Framework / UI**: Streamlit
- **ORM / Data Access**: SQLAlchemy
- **Database**: SQLite (early stage), PostgreSQL (later stage)

## Alternatives Considered
- **Spring Boot + Thymeleaf + JPA + PostgreSQL**
- **Node.js + Express + Server-rendered views + PostgreSQL**

## Consequences

### Positive
- Excellent AI support and tooling for Python
- Strong ecosystem for data processing and analytics
- Very fast prototyping and iteration
- Minimal boilerplate code
- Easy transition from SQLite to PostgreSQL
- Clear path toward more advanced architectures if needed

### Negative
- Streamlit is less flexible for complex UI customization
- Not ideal for high-scale or highly concurrent workloads
- Python performance may be lower than JVM-based stacks for large systems
