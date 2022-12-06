import React from "react";
import "./App.css";
import logo from "./images/UdaConnectLogo.svg";
import Persons from "./components/Persons";
import Realtime from "./components/Realtime.js";

function App() {
  return (
    <div className="App">
      <div className="header">
        <img src={logo} className="App-logo" alt="UdaConnect" />
      </div>
      <div>
        <Realtime />
        <Persons />
      </div>
    </div>
  );
}

export default App;
