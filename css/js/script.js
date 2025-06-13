// Theme toggle
const themeToggle = document.getElementById("theme-toggle");
const themeToggleCircle = document.getElementById("theme-toggle-circle");

themeToggle.addEventListener("click", () => {
  const body = document.body;
  body.classList.toggle("dark-mode");
  body.classList.toggle("light-mode");
  themeToggleCircle.textContent = body.classList.contains("dark-mode") ? "☀️" : "🌙";
});

// Menu toggle
const menuIcon = document.getElementById("menu-icon");
const menuDropdown = document.getElementById("menu-dropdown");

menuIcon.addEventListener("click", () => {
  menuDropdown.classList.toggle("open");
});

// Close menu if clicked outside
document.addEventListener("click", (event) => {
  if (
    !menuIcon.contains(event.target) &&
    !menuDropdown.contains(event.target) &&
    menuDropdown.classList.contains("open")
  ) {
    menuDropdown.classList.remove("open");
  }
});

// Smooth scroll
document.querySelectorAll(".menu-item").forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    const targetId = item.getAttribute("href").substring(1);
    const target = document.getElementById(targetId);
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
      menuDropdown.classList.remove("open");
    }
  });
});
