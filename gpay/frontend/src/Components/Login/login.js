import React, { useState } from "react";


function Login() {
  const [phoneNumber, setPhoneNumber] = useState();
  const [temporary, setTemporary] = useState("");


  
  const handleSubmit = () => {

    setPhoneNumber(temporary);
    setTemporary("");
 
  };
  return (
    <div>
      <form  method="POST" action="/auth">
        <h1>Login</h1>
        <input
        className="inputs"
        name="phonenumber"


          type="tel"
          onChange={(e) => {
            setTemporary(e.target.value);
          }}
          placeholder="Enter the phone number"
          value={temporary}
        />
        <br/>
        <button type="submit" className="buttons" onClick={handleSubmit}>Submit</button>
        <h3>{phoneNumber}</h3>


      </form>
    </div>
  );
}

export default Login;
