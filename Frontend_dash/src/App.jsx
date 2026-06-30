import { useState } from "react";

import "./App.css";

import Navbar from "./components/Navbar";
import Home from "./components/Home";
import About from "./components/About";
import Team from "./components/Team";
import Signup from "./components/Signup";
import Dashboard from "./components/Dashboard";
import Login from "./components/Login";

function App() {

  const [page, setPage] = useState("home");

  return (
    <div>

      <Navbar setPage={setPage} />

      {page === "home" && <Home setPage={setPage} />}

      {page === "about" && <About />}

      {page === "team" && <Team />}

      {page === "signup" && <Signup setPage={setPage} />}

      {page === "login" && <Login setPage={setPage} />}
      
      {page === "dashboard" && <Dashboard />}

    </div>
  );
}

export default App;
