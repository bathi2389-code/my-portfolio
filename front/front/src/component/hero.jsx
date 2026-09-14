function Hero() {
  return (
    <section id="hero">
      <p>Hello, I'm</p>

      <h1>Venkatesh Bathi</h1>

      <h2>Python & Full-Stack Developer</h2>

      <p>
        B.Tech AIML student passionate about Python, DSA,
        React, FastAPI and building real-world applications.
      </p>

      <button onClick={()=>
        {
            document.getElementById("projects").scrollIntoView({
                behavior:"smooth"
            });
        }
      }> View My Projects</button>
    </section>
  );
}

export default Hero;