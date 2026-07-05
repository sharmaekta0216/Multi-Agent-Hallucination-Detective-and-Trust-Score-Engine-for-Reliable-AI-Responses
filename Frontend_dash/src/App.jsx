// import { useState } from "react";

// import "./App.css";

// import Navbar from "./components/Navbar";
// import Home from "./components/Home";
// import About from "./components/About";
// import Team from "./components/Team";
// import Signup from "./components/Signup";
// import Dashboard from "./components/Dashboard";
// import Login from "./components/Login";

// function App() {

//   const [page, setPage] = useState("home");

//   return (
//     <div>

//       <Navbar setPage={setPage} />

//       {page === "home" && <Home setPage={setPage} />}

//       {page === "about" && <About />}

//       {page === "team" && <Team />}

//       {page === "signup" && <Signup setPage={setPage} />}

//       {page === "login" && <Login setPage={setPage} />}
      
//       {page === "dashboard" && <Dashboard />}

//     </div>
//   );
// }

// export default App;
// import { useState } from "react";
// import "./App.css";

// import Navbar from "./components/Navbar";
// import Home from "./components/Home";
// import About from "./components/About";
// import Team from "./components/Team";
// import Signup from "./components/Signup";
// import Login from "./components/Login";
// import Dashboard from "./components/Dashboard";
// import Footer from "./components/Footer";

// function App() {
//   const [page, setPage] = useState("home");
//   const [darkMode, setDarkMode] = useState(false);

//   return (
//     <div className={darkMode ? "app dark" : "app"}>

//       {/* Navigation */}
//       <Navbar
//         setPage={setPage}
//         darkMode={darkMode}
//         setDarkMode={setDarkMode}
//       />

//       {/* Pages */}
//       {page === "home" && (
//         <Home setPage={setPage} />
//       )}

//       {page === "dashboard" && (
//         <Dashboard />
//       )}

//       {page === "about" && (
//         <About />
//       )}

//       {page === "team" && (
//         <Team />
//       )}

//       {page === "signup" && (
//         <Signup setPage={setPage} />
//       )}

//       {page === "login" && (
//         <Login setPage={setPage} />
//       )}

//       {/* Footer */}
//       <Footer />

//     </div>
//   );
// }

// export default App;
// import React from "react";
// import { BrowserRouter, Routes, Route } from "react-router-dom";

// import Navbar from "./components/Navbar";
// import Home from "./components/Home";
// import Dashboard from "./components/Dashboard";
// import Team from "./components/Team";
// import Login from "./components/Login";
// import Signup from "./components/Signup";
// import Charts from "./components/Charts";

// function App() {
//   return (
//     <BrowserRouter>

//       <Navbar />

//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/dashboard" element={<Dashboard />} />
//         <Route path="/team" element={<Team />} />
//         <Route path="/login" element={<Login />} />
//         <Route path="/signup" element={<Signup />} />
//         <Route path="/charts" element={<Charts />} />
//       </Routes>

//     </BrowserRouter>
//   );
// }

// export default App;


// function App() {
//   return <h1>Hello World</h1>;
// }

// export default App;
// import Home from "./components/Home";

// function App() {
//   return <Home />;
// }

// export default App;


// import Navbar from "./components/Navbar";

// function App() {
//   return <Navbar />
      
    

// }

// export default App;
// import { BrowserRouter } from "react-router-dom";
// import Navbar from "./components/Navbar";

// function App() {
//   return (
//     <BrowserRouter>
//       <Navbar />
//     </BrowserRouter>
//   );
// }

// export default App;
/* <BrowserRouter>
  <Navbar />

  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/dashboard" element={<Dashboard />} />
    <Route path="/team" element={<Team />} />
    <Route path="/login" element={<Login />} />
    <Route path="/signup" element={<Signup />} />
    <Route path="/charts" element={<Charts />} />
  </Routes>
</BrowserRouter>
export default App; */


import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";
import Team from "./components/Team";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Charts from "./components/Charts";
import About from "./components/About";

import "./Styles/App.css";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/charts" element={<Charts />} />
        <Route path="/team" element={<Team />} />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
