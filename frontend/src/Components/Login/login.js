import React, { useState } from "react";

function Login() {
  const [phoneNumber, setPhoneNumber] = useState();
  const [temporary, setTemporary] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    setPhoneNumber(temporary);
    setTemporary("");
 
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h1>Login</h1>
        <input
        className="inputs"
          type="tel"
          onChange={(e) => {
            setTemporary(e.target.value);
          }}
          placeholder="Enter the phone number"
          value={temporary}
        />
        <br/>
        <button type="submit" className="buttons">Submit</button>
        <h3>{phoneNumber}</h3>
      </form>
    </div>
  );
}

export default Login;
