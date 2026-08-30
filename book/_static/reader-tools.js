(function () {
  "use strict";

  const glossary = {
    "argument": "A value supplied when calling a function or method.",
    "array": "A multidimensional collection of values, usually stored by NumPy.",
    "attribute": "Information stored on an object and accessed without calling it, such as array.shape.",
    "Boolean mask": "An array or Series of True and False values used to select observations.",
    "method": "A function accessed through an object or class, such as text.lower().",
    "mutable": "Able to change in place.",
    "immutable": "Unable to change in place after creation.",
    "class": "A definition describing a kind of object and its behaviour.",
    "dictionary": "A mutable collection that maps unique keys to values.",
    "function": "A named unit of code that can accept inputs and return a result.",
    "object": "A Python value with a type, data, and available operations.",
    "parameter": "A name in a function definition that receives an argument.",
    "return value": "The object produced by a function call.",
    "axis": "One dimension of an array. Its meaning depends on the dataset.",
    "broadcasting": "NumPy rules for operations on arrays with compatible shapes.",
    "DataFrame": "A labelled, two-dimensional pandas table.",
    "estimator": "A model-like object with methods such as fit and predict.",
    "feature": "An input variable supplied to a model.",
    "feature matrix": "A samples by features table commonly named X.",
    "target": "The outcome a supervised model is trained to predict, commonly named y.",
    "pipeline": "An ordered sequence of preprocessing and modelling steps fitted together.",
    "data leakage": "Information unavailable at prediction time accidentally influences model training or evaluation.",
    "epoch": "A segment of recorded signal aligned to an event or time interval.",
    "evoked response": "A signal obtained by averaging aligned epochs, usually across trials.",
    "shape": "A tuple containing the size of every array dimension.",
    "interpreter": "The Python program that executes the code.",
    "kernel": "The process that executes notebook cells and retains variables between runs.",
    "dependency": "A package required by a project.",
    "module": "A Python file containing names that can be imported.",
    "package": "An installable collection of Python modules.",
    "path": "An object or string describing a location in a filesystem.",
    "virtual environment": "An isolated Python installation and package set.",
    "working directory": "The directory used to interpret relative paths."
  };

  function addExerciseNavigator() {
    const article = document.querySelector("article.bd-article");
    if (!article) return;
    const exercises = Array.from(article.querySelectorAll(".exercise[id]"));
    if (exercises.length < 2) return;

    const details = document.createElement("details");
    details.className = "exercise-navigator";
    const summary = document.createElement("summary");
    summary.textContent = `Exercises on this page (${exercises.length})`;
    const list = document.createElement("ol");

    exercises.forEach(function (exercise, index) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      const title = exercise.querySelector(":scope > .admonition-title");
      link.href = `#${exercise.id}`;
      link.textContent = title ? title.textContent.trim() : `Exercise ${index + 1}`;
      item.appendChild(link);
      list.appendChild(item);
    });

    details.append(summary, list);
    exercises[0].before(details);
  }

  function copyText(text, button) {
    function complete() {
      const previous = button.textContent;
      button.textContent = "Copied";
      window.setTimeout(function () { button.textContent = previous; }, 1200);
    }

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(complete);
      return;
    }

    const helper = document.createElement("textarea");
    helper.value = text;
    helper.style.position = "fixed";
    helper.style.opacity = "0";
    document.body.appendChild(helper);
    helper.select();
    document.execCommand("copy");
    helper.remove();
    complete();
  }

  function addCopyButtons() {
    document.querySelectorAll("article.bd-article div.highlight > pre").forEach(function (pre) {
      const highlight = pre.parentElement;
      if (highlight.querySelector(":scope > .workshop-copy-button")) return;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "workshop-copy-button";
      button.textContent = "Copy";
      button.setAttribute("aria-label", "Copy code");
      button.addEventListener("click", function () { copyText(pre.innerText, button); });
      highlight.appendChild(button);
    });
  }

  let pyodidePromise;

  function getPyodide() {
    if (pyodidePromise) return pyodidePromise;
    pyodidePromise = new Promise(function (resolve, reject) {
      const start = function () {
        window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/"
        }).then(resolve, reject);
      };

      if (window.loadPyodide) {
        start();
        return;
      }

      const script = document.createElement("script");
      script.src = "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js";
      script.onload = start;
      script.onerror = function () { reject(new Error("Could not download the Python runtime.")); };
      document.head.appendChild(script);
    });
    return pyodidePromise;
  }

  function initialiseLivePython() {
    document.querySelectorAll(".live-python").forEach(function (widget) {
      const editor = widget.querySelector("textarea");
      const button = widget.querySelector("button");
      const output = widget.querySelector("pre");
      if (!editor || !button || !output) return;
      const idleLabel = button.dataset.idleLabel || "Run code";

      // MyST can interpret blank lines inside raw textareas as paragraphs, and
      // Sphinx typography can curl quotation marks. Neither belongs in Python code.
      editor.value = editor.value
        .replace(/<\/?p>/gi, "")
        .replace(/[“”]/g, '"')
        .replace(/[‘’]/g, "'")
        .replace(/^\s+|\s+$/g, "");

      button.addEventListener("click", async function () {
        button.disabled = true;
        button.textContent = "Starting Python...";
        output.textContent = "";
        const oldImage = widget.querySelector(".live-python-output-image");
        if (oldImage) oldImage.remove();
        try {
          const pyodide = await getPyodide();
          button.textContent = "Running...";
          await pyodide.loadPackagesFromImports(editor.value);
          pyodide.setStdout({ batched: function (text) { output.textContent += `${text}\n`; } });
          pyodide.setStderr({ batched: function (text) { output.textContent += `${text}\n`; } });
          const result = await pyodide.runPythonAsync(editor.value);
          if (result !== undefined && result !== null) output.textContent += String(result);
          if (!output.textContent) output.textContent = "Code completed without printed output.";
          if (pyodide.FS && pyodide.FS.analyzePath("/tmp/live_plot.png").exists) {
            const bytes = pyodide.FS.readFile("/tmp/live_plot.png");
            const image = document.createElement("img");
            image.className = "live-python-output-image";
            image.alt = "Plot generated by the code above";
            image.src = URL.createObjectURL(new Blob([bytes], { type: "image/png" }));
            widget.appendChild(image);
          }
        } catch (error) {
          output.textContent = String(error);
        } finally {
          button.disabled = false;
          button.textContent = idleLabel;
        }
      });
    });
  }

  function initialiseAxisExplorer() {
    document.querySelectorAll(".axis-explorer").forEach(function (widget) {
      const select = widget.querySelector("select");
      const output = widget.querySelector("output");
      const meanings = ["trials", "channels", "time samples"];
      const shape = [80, 32, 500];
      function update() {
        const axis = Number(select.value);
        const result = shape.filter(function (_size, index) { return index !== axis; });
        output.textContent = `mean(axis=${axis}) removes ${meanings[axis]} and returns (${result.join(", ")})`;
      }
      select.addEventListener("change", update);
      update();
    });
  }

  function initialiseFigureExplorer() {
    document.querySelectorAll(".figure-explorer").forEach(function (widget) {
      const amplitude = widget.querySelector("[data-amplitude]");
      const noise = widget.querySelector("[data-noise]");
      const svg = widget.querySelector("svg");
      const description = widget.querySelector("output");

      function points(offset, phase) {
        const amp = Number(amplitude.value);
        const jitter = Number(noise.value);
        const values = [];
        for (let index = 0; index < 80; index += 1) {
          const x = 35 + index * 6.8;
          const signal = Math.sin(index / 9 + phase) * amp;
          const deterministicNoise = Math.sin(index * 2.41 + phase) * jitter;
          values.push(`${x.toFixed(1)},${(115 - offset - signal - deterministicNoise).toFixed(1)}`);
        }
        return values.join(" ");
      }

      function update() {
        svg.querySelector("[data-line-a]").setAttribute("points", points(0, 0));
        svg.querySelector("[data-line-b]").setAttribute("points", points(18, 0.55));
        description.textContent = `Signal amplitude ${amplitude.value}; added noise ${noise.value}.`;
      }

      amplitude.addEventListener("input", update);
      noise.addEventListener("input", update);
      update();
    });
  }

  function addGlossaryTooltips() {
    const article = document.querySelector("article.bd-article");
    if (!article) return;
    const counts = new Map();
    const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    let tooltipIndex = 0;

    nodes.forEach(function (node) {
      const parent = node.parentElement;
      if (!parent || parent.closest("code, pre, a, abbr, h1, h2, h3, button, figure, .admonition-title")) return;

      for (const [term, definition] of Object.entries(glossary).sort(function (a, b) {
        return b[0].length - a[0].length;
      })) {
        if ((counts.get(term) || 0) >= 2) continue;
        const pattern = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(" ", "\\s+");
        const match = node.data.match(new RegExp(`\\b${pattern}s?\\b`, "i"));
        if (!match) continue;

        const before = node.data.slice(0, match.index);
        const after = node.data.slice(match.index + match[0].length);
        const tooltip = document.createElement("button");
        const bubble = document.createElement("span");
        tooltipIndex += 1;
        const bubbleId = `glossary-tooltip-${tooltipIndex}`;
        tooltip.type = "button";
        tooltip.className = "glossary-tooltip";
        tooltip.setAttribute("aria-describedby", bubbleId);
        tooltip.setAttribute("aria-expanded", "false");
        tooltip.appendChild(document.createTextNode(match[0]));
        bubble.id = bubbleId;
        bubble.className = "glossary-tooltip__bubble";
        bubble.setAttribute("role", "tooltip");
        bubble.textContent = definition;
        tooltip.appendChild(bubble);
        tooltip.addEventListener("pointerenter", function () {
          tooltip.classList.add("glossary-tooltip--hovered");
        });
        tooltip.addEventListener("pointerleave", function () {
          tooltip.classList.remove("glossary-tooltip--hovered");
        });
        tooltip.addEventListener("click", function (event) {
          event.stopPropagation();
          const opening = tooltip.getAttribute("aria-expanded") !== "true";
          document.querySelectorAll(".glossary-tooltip[aria-expanded='true']").forEach(function (other) {
            if (other !== tooltip) other.setAttribute("aria-expanded", "false");
          });
          tooltip.setAttribute("aria-expanded", String(opening));
        });
        node.replaceWith(document.createTextNode(before), tooltip, document.createTextNode(after));
        counts.set(term, (counts.get(term) || 0) + 1);
        break;
      }
    });

    document.addEventListener("click", function () {
      document.querySelectorAll(".glossary-tooltip[aria-expanded='true']").forEach(function (tooltip) {
        tooltip.setAttribute("aria-expanded", "false");
      });
    });
  }

  function initialiseReaderTools() {
    addCopyButtons();
    initialiseLivePython();
    initialiseAxisExplorer();
    initialiseFigureExplorer();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialiseReaderTools);
  } else {
    initialiseReaderTools();
  }
})();
