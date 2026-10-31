import React, { useState, useEffect } from "react";

function App() {

  const [name,setName]=useState("");
  const [records,setRecords]=useState([]);

  const loadAttendance=async()=>{

    const response=
      await fetch("http://localhost:5000/attendance");

    const data=
      await response.json();

    setRecords(data);
  };

  useEffect(()=>{
      loadAttendance();
  },[]);

  const submitAttendance=async()=>{

    await fetch(
      "http://localhost:5000/attendance",
      {
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({
          employee_name:name,
          attendance_date:
           new Date().toISOString().split('T')[0],
          status:"Present"
        })
      }
    );

    loadAttendance();
  };

  return (
    <div>
      <h1>Attendance Portal</h1>

      <input
        placeholder="Employee Name"
        value={name}
        onChange={(e)=>setName(e.target.value)}
      />

      <button onClick={submitAttendance}>
        Mark Present
      </button>

      <hr/>

      {records.map(record=>(
        <div key={record.id}>
          {record.employee_name}
          -
          {record.attendance_date}
          -
          {record.status}
        </div>
      ))}
    </div>
  );
}

export default App;