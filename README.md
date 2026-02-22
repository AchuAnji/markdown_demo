# Operations Defect Recurrence Dashboard

A Streamlit-based web application for analyzing and visualizing recurring defects across manufacturing lots. This dashboard helps identify quality issues by distinguishing between recurring defects (appearing in multiple lots) and one-off incidents.

## Table of Contents

- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Usage Examples](#usage-examples)
- [How to Run Tests](#how-to-run-tests)
- [Project Structure](#project-structure)

## Project Description

### Overview

The Operations Defect Recurrence Dashboard aggregates inspection data and provides insights into manufacturing quality by analyzing defect patterns. It distinguishes between:

- **Recurring Defects**: Defect types that appear across multiple lots, indicating systemic quality issues
- **One-Off Defects**: Defects appearing in only a single lot, typically representing isolated incidents

### Key Features

- Automated defect aggregation from inspection records
- Real-time dashboard visualization of defect metrics
- Classification of defects by recurrence patterns
- Support for PostgreSQL and SQLite databases

### Use Cases

- Quality assurance teams identifying systemic defect trends
- Operations managers prioritizing quality improvement initiatives
- Data analysts investigating product quality patterns over time

## Tech Stack

- **Language**: Python 3.9+
- **Web Framework**: Streamlit
- **Database**: PostgreSQL (or SQLite for development)
- **Data Processing**: Pandas, NumPy
- **Database Driver**: psycopg2 (PostgreSQL)

See `requirements.txt` for complete dependency list.

## How to Run

### Prerequisites

- Python 3.9 or higher
- PostgreSQL database (or SQLite for development)
- pip or conda for package management

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd markdown_demo
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure PostgreSQL is running
   - Create a database for the project
   - Set the `DATABASE_URL` environment variable:
     ```bash
     export DATABASE_URL="postgresql://username:password@localhost:5432/defect_db"
     ```

5. **Initialize the database schema**:
   ```bash
   psql -U username -d defect_db -f db/schema.sql
   psql -U username -d defect_db -f db/seed.sql
   ```

### Running the Application

Start the Streamlit development server:

```bash
streamlit run UI/app.py
```

The application will open in your default browser at `http://localhost:8501`.

### Build for Production

To create a production-ready deployment:

```bash
# Install production dependencies
pip install -r requirements.txt

# Configure DATABASE_URL for production database
export DATABASE_URL="your-production-database-url"

# Run the app
streamlit run UI/app.py --logger.level=info
```

## Usage Examples

### Viewing the Dashboard

1. **Start the application** (see [How to Run](#how-to-run))
2. **Navigate to the web interface** at `http://localhost:8501`
3. **View two main sections**:
   - **Recurring Defects**: Table showing defect types that appear in multiple lots
   - **One-Off Defects**: Table showing defects appearing in only one lot

### Example Workflow

**Scenario**: Quality analyst investigating defect patterns in weekly production

1. Open the dashboard
2. Review the "Recurring Defects" section to identify systemic issues
3. Note defects with high affected lot counts
4. Cross-reference with production data to determine root causes
5. Track improvements by monitoring defect counts over time

### Sample Data Interpretation

```
Recurring Defects Table Output:
| defect_name      | affected_lots |
|------------------|---------------|
| Surface Scratch  | 12            |
| Color Variation  | 8             |
| Dimension Error  | 5             |

One-Off Defects Table Output:
| defect_name      | affected_lots |
|------------------|---------------|
| Packaging Damage | 1             |
| Label Misprint   | 1             |
```

## How to Run Tests

### Running Unit Tests

The project uses Python's standard testing framework. To run tests:

```bash
# Run all tests
python -m pytest

# Run tests with verbose output
python -m pytest -v

# Run tests in a specific file
python -m pytest tests/test_defect_analysis.py

# Run tests with coverage report
python -m pytest --cov=. --cov-report=html
```

### Manual Testing

For manual testing of the dashboard:

1. **Start with sample data**:
   ```bash
   psql -U username -d defect_db -f db/seed.sql
   ```

2. **Launch the app**:
   ```bash
   streamlit run UI/app.py
   ```

3. **Verify functionality**:
   - Check that the "Recurring Defects" section displays results
   - Check that the "One-Off Defects" section displays results
   - Confirm no warning messages appear for valid data

### Database Validation

To verify the database schema and data:

```bash
# View schema
psql -U username -d defect_db -c "\dt"

# Run sample queries
psql -U username -d defect_db -f db/sample_queries.sql
```

## Project Structure

```
markdown_demo/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── UI/
│   └── app.py                        # Streamlit application
├── db/
│   ├── schema.sql                    # Database schema definition
│   ├── seed.sql                      # Sample data initialization
│   └── sample_queries.sql            # Reference SQL queries
├── docs/
│   ├── architecture_decision_records.md
│   ├── assumptions_scope.md          # Project scope and assumptions
│   ├── data_design.md                # Data model documentation
│   └── tech_stack_decision_records.md # Technology decisions
```

## Configuration

### Environment Variables

- `DATABASE_URL`: PostgreSQL connection string (required)
  ```bash
  postgresql://[user[:password]@][netloc][:port][/dbname]
  ```

### Streamlit Configuration

Create a `.streamlit/config.toml` file for advanced configuration:

```toml
[server]
port = 8501
headless = true

[logger]
level = "info"
```

## Troubleshooting

### Database Connection Error

**Error**: `psycopg2.OperationalError: could not connect to server`

**Solution**:
- Verify PostgreSQL is running
- Check `DATABASE_URL` environment variable is set correctly
- Confirm database exists and user has permissions

### No Data Displayed

**Possible causes**:
- Database has no inspection or defect data
- Run `db/seed.sql` to load sample data
- Verify schema matches expected table structure

### Streamlit Port Already in Use

**Error**: `Port 8501 is already in use`

**Solution**:
```bash
streamlit run db/UI/app.py --server.port=8502
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure quality
4. Submit a pull request

## License

See LICENSE file for details.

## Support

For issues or questions, please refer to the documentation in the `docs/` directory or contact the development team.