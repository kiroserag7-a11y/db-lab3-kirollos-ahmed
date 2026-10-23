/* Browser-side checks. The server repeats the same rules (never trust the browser). */
(function () {
  "use strict";

  var NAME_MAX = 100, EMAIL_MAX = 255, TITLE_MAX = 200, PASSWORD_MAX_BYTES = 72;

  function val(form, name) {
    var el = form.elements[name];
    return el ? el.value : "";
  }

  var rules = {
    register: function (f) {
      var e = [];
      var name = val(f, "name").trim(), email = val(f, "email").trim();
      var pw = val(f, "password"), cf = val(f, "confirm_password");
      if (!name) e.push("Name is required");
      else if (name.length > NAME_MAX) e.push("Name is too long (" + NAME_MAX + " characters at most)");
      if (!email) e.push("Email is required");
      else if (email.length > EMAIL_MAX) e.push("Email is too long (" + EMAIL_MAX + " characters at most)");
      if (!pw) e.push("Password is required");
      else if (new TextEncoder().encode(pw).length > PASSWORD_MAX_BYTES)
        e.push("Password is too long (" + PASSWORD_MAX_BYTES + " bytes at most)");
      if (!cf) e.push("Confirm password is required");
      if (pw && cf && pw !== cf) e.push("Passwords do not match");
      return e;
    },
    login: function (f) {
      var e = [];
      if (!val(f, "email").trim()) e.push("Email is required");
      if (!val(f, "password")) e.push("Password is required");
      return e;
    },
    todo: function (f) {
      var t = val(f, "title").trim();
      if (!t) return ["Title is required"];
      if (t.length > TITLE_MAX) return ["Title is too long (" + TITLE_MAX + " characters at most)"];
      return [];
    }
  };

  function showErrors(form, list) {
    var ul = form.querySelector("[data-errors]");
    if (!ul) return;
    ul.innerHTML = "";
    list.forEach(function (msg) {
      var li = document.createElement("li");
      li.textContent = msg;
      ul.appendChild(li);
    });
    ul.hidden = list.length === 0;
  }

  document.querySelectorAll("form[data-validate]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      var list = rules[form.dataset.validate](form);
      if (list.length) {
        ev.preventDefault();   // nothing is sent when the form is wrong
        showErrors(form, list);
      }
    });
  });

  /* R7: ask "are you sure?" before deleting */
  document.querySelectorAll("form[data-confirm]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      if (!window.confirm(form.dataset.confirm)) ev.preventDefault();
    });
  });

  /* Bonus: filter all / open / done (browser side only) */
  var chips = document.querySelectorAll("[data-filter]");
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var mode = chip.dataset.filter, shown = 0;
      chips.forEach(function (c) { c.classList.toggle("is-on", c === chip); });
      document.querySelectorAll("#todo-list .todo").forEach(function (li) {
        var done = li.dataset.done === "1";
        var show = mode === "all" || (mode === "done" && done) || (mode === "open" && !done);
        li.hidden = !show;
        if (show) shown++;
      });
      var empty = document.getElementById("filter-empty");
      if (empty) empty.hidden = shown !== 0;
    });
  });
})();
