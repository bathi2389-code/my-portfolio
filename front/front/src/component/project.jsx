function Projects() {
    const projects = [
  {
    name: "Expense Tracker",
    description: "A full-stack application to manage and track expenses.",
    technology: "React, FastAPI, PostgreSQL"
  },
  {
    name: "Student Record Management System",
    description: "A system to create, update, view and manage student records.",
    technology: "Python, SQL"
  },
  {
    name: "Smart Route Finder",
    description: "An application that finds routes using data structures and algorithms.",
    technology: "Python, DSA"
  }
];
  return (
    <section id="projects">
      <h2>My Projects</h2>
      {projects.map((project) => (
        <div key={project.name}>
          <h3>{project.name}</h3>
          <p>{project.description}</p>
          <p><strong>Technology:</strong> {project.technology}</p>
        </div>
      ))}
    </section>
  );
}

export default Projects;