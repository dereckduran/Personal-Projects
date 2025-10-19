import React, { useEffect, useState } from 'react'

function index() {

  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState([]);
  const [counter, setCounter] = useState(0);

  useEffect(() => {
    fetch("http://localhost:8080/api/home").then(
      response => response.json()
    ).then(
      data => {
        setMessage(data.message)
        setPeople(data.people)
      }
    )
  }, []);

  return (
    <div>
     <p>{counter}</p>
     <button onClick={() => setCounter(counter + 1)}>
      Press Me
     </button>
    </div>
  )
}

export default index
