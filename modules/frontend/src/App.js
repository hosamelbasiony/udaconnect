import React from "react";
import "./App.css";
import logo from "./images/UdaConnectLogo.svg";
import Persons from "./components/Persons";
import Realtime from "./components/Realtime.js";
import { useAppStore } from './appStore'

function App() {

  const store = useAppStore();

  return (
    <div className="App">
      <div className="header">
        <img src={logo} className="App-logo" alt="UdaConnect" />
      </div>
      <div>
        <Realtime store={store} />
        <Persons store={store} />
      </div>
    </div>
  );
}

export default App;
