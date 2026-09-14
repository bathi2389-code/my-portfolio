import { useState } from "react";

function Contact() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/contact", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        email: email,
        message: message,
      }),
    });

    const data = await response.json();

    console.log(data);
    setEmail("");
    setMessage("");
    setName("");
  }

  return (
    <section id="contact">
      <h2>Contact Me</h2>

      <form onSubmit={handleSubmit}>
        <input
        type="text"
        id="name"
        name="name"
        placeholder="Your Name"
        value={name}
        onChange={(event) => setName(event.target.value)}
        />
        <input
        type="email"
        id="email"
        name="email"
        placeholder="Your Email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
        />
        <textarea
        id="message"
        name="message"
        placeholder="Your Message"
        rows="5"
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        ></textarea>

        <button type="submit">
          Send Message
        </button>
      </form>
    </section>
  );
}

export default Contact;