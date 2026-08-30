(function () {
  "use strict";

  const storagePrefix = "cogsci-python-workshop:answer:";

  function storageAvailable() {
    try {
      const key = `${storagePrefix}test`;
      window.localStorage.setItem(key, "test");
      window.localStorage.removeItem(key);
      return true;
    } catch (_error) {
      return false;
    }
  }

  function exerciseKey(exercise, index) {
    const identity = exercise.id || `exercise-${index + 1}`;
    return `${storagePrefix}${window.location.pathname}#${identity}`;
  }

  function addAnswerBox(exercise, index, canStore) {
    if (exercise.querySelector(":scope > .personal-answer")) return;

    const key = exerciseKey(exercise, index);
    const wrapper = document.createElement("section");
    wrapper.className = "personal-answer";

    const heading = document.createElement("label");
    const textareaId = `personal-answer-${index + 1}`;
    heading.className = "personal-answer__label";
    heading.htmlFor = textareaId;
    heading.textContent = "Your answer";

    const textarea = document.createElement("textarea");
    textarea.id = textareaId;
    textarea.className = "personal-answer__input";
    textarea.rows = 5;
    textarea.placeholder = "Write your prediction or explanation before revealing the solution…";
    textarea.setAttribute("aria-describedby", `${textareaId}-privacy ${textareaId}-status`);

    const footer = document.createElement("div");
    footer.className = "personal-answer__footer";

    const privacy = document.createElement("span");
    privacy.id = `${textareaId}-privacy`;
    privacy.className = "personal-answer__privacy";
    privacy.textContent = canStore
      ? "Private to this browser: saved automatically"
      : "Private note: automatic saving is unavailable in this browser";

    const actions = document.createElement("span");
    actions.className = "personal-answer__actions";

    const status = document.createElement("span");
    status.id = `${textareaId}-status`;
    status.className = "personal-answer__status";
    status.setAttribute("aria-live", "polite");

    const clear = document.createElement("button");
    clear.type = "button";
    clear.className = "personal-answer__clear";
    clear.textContent = "Clear note";

    if (canStore) {
      textarea.value = window.localStorage.getItem(key) || "";
      let saveTimer;

      textarea.addEventListener("input", function () {
        window.clearTimeout(saveTimer);
        status.textContent = "Saving…";
        saveTimer = window.setTimeout(function () {
          if (textarea.value) {
            window.localStorage.setItem(key, textarea.value);
          } else {
            window.localStorage.removeItem(key);
          }
          status.textContent = "Saved";
        }, 300);
      });

      clear.addEventListener("click", function () {
        textarea.value = "";
        window.localStorage.removeItem(key);
        status.textContent = "Cleared";
        textarea.focus();
      });
    } else {
      clear.addEventListener("click", function () {
        textarea.value = "";
        status.textContent = "Cleared";
        textarea.focus();
      });
    }

    actions.append(status, clear);
    footer.append(privacy, actions);
    wrapper.append(heading, textarea, footer);
    exercise.append(wrapper);
  }

  function initialisePersonalAnswers() {
    const canStore = storageAvailable();
    const codeRunExercises = new Set([
      "figure-rescue",
      "uncertainty-plot",
      "figure-showdown",
      "epochs-evoked-challenge",
    ]);
    document.querySelectorAll(".exercise").forEach(function (exercise, index) {
      if (codeRunExercises.has(exercise.id)) return;
      addAnswerBox(exercise, index, canStore);
    });
  }

  function initialiseSolutions() {
    document.querySelectorAll(".solution").forEach(function (solution, index) {
      if (solution.classList.contains("workshop-solution-ready")) return;

      const title = solution.querySelector(":scope > .admonition-title");
      const content = solution.querySelector(":scope > section");
      if (!content) return;

      const button = document.createElement("button");
      const contentId = content.id
        ? `${content.id}-${index + 1}`
        : `workshop-solution-${index + 1}`;

      content.id = contentId;
      button.type = "button";
      button.className = "workshop-solution__toggle";
      button.setAttribute("aria-controls", contentId);
      button.setAttribute("aria-expanded", "false");
      button.textContent = "Reveal answer";

      solution.classList.add("workshop-solution-ready", "workshop-solution-collapsed");
      if (title) title.hidden = true;
      content.hidden = true;
      solution.insertBefore(button, solution.firstChild);

      button.addEventListener("click", function () {
        const opening = content.hidden;
        content.hidden = !opening;
        if (title) title.hidden = !opening;
        solution.classList.toggle("workshop-solution-collapsed", !opening);
        button.setAttribute("aria-expanded", String(opening));
        button.textContent = opening ? "Hide answer" : "Reveal answer";
      });
    });
  }

  function initialiseSidebarGroups() {
    const navigation = document.querySelector("nav.bd-links");
    if (!navigation) return;

    navigation.querySelectorAll(":scope .bd-toc-item > p.caption").forEach(function (caption, index) {
      if (caption.querySelector(".workshop-nav-toggle")) return;

      const list = caption.nextElementSibling;
      if (!list || list.tagName !== "UL") return;

      const currentGroup = Boolean(list.querySelector(".current, [aria-current='page']"));
      const storageKey = `cogsci-python-workshop:nav-group:${index}`;
      let expanded = currentGroup;

      if (!currentGroup) {
        try {
          expanded = window.sessionStorage.getItem(storageKey) === "open";
        } catch (_error) {
          expanded = false;
        }
      }

      const button = document.createElement("button");
      const captionText = caption.querySelector(":scope > .caption-text");
      const label = caption.textContent.trim();
      const listId = list.id || `workshop-nav-group-${index + 1}`;
      list.id = listId;
      button.type = "button";
      button.className = "workshop-nav-toggle";
      button.setAttribute("aria-controls", listId);
      button.setAttribute("aria-expanded", String(expanded));
      button.setAttribute("aria-label", `Toggle ${label}`);

      const indicator = document.createElement("span");
      indicator.className = "workshop-nav-toggle__indicator";
      indicator.setAttribute("aria-hidden", "true");
      indicator.textContent = "⌄";
      button.appendChild(indicator);
      if (captionText) {
        button.appendChild(captionText);
      } else {
        const text = document.createElement("span");
        text.className = "caption-text";
        text.textContent = label;
        button.appendChild(text);
      }
      list.hidden = !expanded;
      caption.appendChild(button);

      button.addEventListener("click", function () {
        expanded = button.getAttribute("aria-expanded") !== "true";
        button.setAttribute("aria-expanded", String(expanded));
        list.hidden = !expanded;
        try {
          window.sessionStorage.setItem(storageKey, expanded ? "open" : "closed");
        } catch (_error) {
          // The navigation still works if browser storage is unavailable.
        }
      });
    });
  }

  function initialiseWorkshopInteractions() {
    initialiseSidebarGroups();
    initialisePersonalAnswers();
    initialiseSolutions();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialiseWorkshopInteractions);
  } else {
    initialiseWorkshopInteractions();
  }
})();
