function Skills() {
  const skills = [
    "Python",
    "Data Structures",
    "SQL",
    "React",
    "FastAPI",
    "PostgreSQL",
    "Git & GitHub",
    "Docker",
  ];

  return (
    <section id="skills">
      <h2>Skills</h2>

      <div>
        {skills.map((skill) => (
          <div key={skill}>
            {skill}
          </div>
        ))}
      </div>
    </section>
  );
}

export default Skills;