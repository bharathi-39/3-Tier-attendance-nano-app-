CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100),
    attendance_date DATE,
    status VARCHAR(20)
);