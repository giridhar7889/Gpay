import React, { useState } from "react";
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function Login() {
   
const csrftoken = getCookie('csrftoken');
  //var csrftoken = '{{ csrf_token }}';
  const [phoneNumber, setPhoneNumber] = useState();
  const [temporary, setTemporary] = useState("");

  const handleSubmit = () => {
    setPhoneNumber(temporary);
    setTemporary("");
  };
  return (
    <div>
      <form method="POST" action="http://localhost:8000/auth/" >
        {csrftoken}
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
        <br />
        <button type="submit" className="buttons" onClick={handleSubmit}>
          Submit
        </button>
        <h3>{phoneNumber}</h3>
      </form>
    </div>
  );
}

export default Login;
