import Navbar from "./component/navbar";
import Hero from "./component/hero";
import About from "./component/about";
import Skills from "./component/skills";
import Projects from "./component/project";
import Education from "./component/education";
import Contact from "./component/contacts";
import './App.css'
function App() {
  return (
    <div>
      <h1>Venkatesh Portfolio</h1>
      <Navbar />
      <Hero/>
      <About/>
      <Skills/>
      <Projects/>
      <Education/>
      <Contact/>

    
    </div>
  );
}

export default App;