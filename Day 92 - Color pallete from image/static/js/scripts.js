document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('input[type="checkbox"]').forEach(function (checkbox) {
    if (checkbox.id.includes("done")) {
      return;
    }
    checkbox.addEventListener("change", function () {
      fetch("/toggle/" + this.id.split("-")[1], {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Requested-With": "XMLHttpRequest",
        },
        body: JSON.stringify({ done: this.checked }),
      })
        .then((response) => response.json())
        .then((data) => {
          // Optionally update UI or handle response
        });
    });
  });
});
