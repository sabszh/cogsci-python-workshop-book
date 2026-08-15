(function () {
  "use strict";

  function makeSidebarHeadingsClickable() {
    document.querySelectorAll("nav.bd-links p.caption").forEach(function (caption) {
      caption.addEventListener("click", function (event) {
        if (event.target.closest("button.workshop-nav-toggle")) return;

        const toggle = caption.querySelector("button.workshop-nav-toggle");
        if (toggle) toggle.click();
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", makeSidebarHeadingsClickable);
  } else {
    makeSidebarHeadingsClickable();
  }
})();
