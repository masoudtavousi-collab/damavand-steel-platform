(() => {
  "use strict";

  const navToggle = document.querySelector("[data-nav-toggle]");
  const navigation = document.querySelector("[data-navigation]");

  if (navToggle && navigation) {
    const closeNavigation = () => {
      navigation.dataset.open = "false";
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "باز کردن منوی اصلی");
    };

    navToggle.addEventListener("click", () => {
      const isOpen = navigation.dataset.open === "true";
      navigation.dataset.open = String(!isOpen);
      navToggle.setAttribute("aria-expanded", String(!isOpen));
      navToggle.setAttribute("aria-label", isOpen ? "باز کردن منوی اصلی" : "بستن منوی اصلی");
    });

    navigation.addEventListener("click", (event) => {
      if (event.target.closest("a")) {
        closeNavigation();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeNavigation();
        navToggle.focus();
      }
    });

    document.addEventListener("click", (event) => {
      if (
        navigation.dataset.open === "true"
        && !navigation.contains(event.target)
        && !navToggle.contains(event.target)
      ) {
        closeNavigation();
      }
    });

    window.addEventListener("resize", () => {
      if (window.matchMedia("(min-width: 50rem)").matches) {
        closeNavigation();
      }
    });
  }

  const dialogBackdrop = document.querySelector("[data-dialog-backdrop]");
  const dialog = document.querySelector("[data-inquiry-dialog]");
  const openButtons = document.querySelectorAll("[data-open-inquiry]");
  const closeButton = document.querySelector("[data-close-inquiry]");
  let dialogTrigger = null;

  if (dialogBackdrop && dialog && closeButton) {
    const focusableSelector = "button:not([disabled]), a[href], [tabindex]:not([tabindex='-1'])";

    const closeDialog = () => {
      dialogBackdrop.dataset.open = "false";
      dialogBackdrop.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      dialogTrigger?.focus();
    };

    const openDialog = (trigger) => {
      dialogTrigger = trigger;
      dialogBackdrop.dataset.open = "true";
      dialogBackdrop.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      closeButton.focus();
    };

    openButtons.forEach((button) => {
      button.addEventListener("click", () => openDialog(button));
    });

    closeButton.addEventListener("click", closeDialog);
    dialogBackdrop.addEventListener("click", (event) => {
      if (event.target === dialogBackdrop) {
        closeDialog();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && dialogBackdrop.dataset.open === "true") {
        closeDialog();
      }
      if (event.key === "Tab" && dialogBackdrop.dataset.open === "true") {
        const focusable = [...dialog.querySelectorAll(focusableSelector)];
        const first = focusable[0];
        const last = focusable.at(-1);
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last?.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first?.focus();
        }
      }
    });
  }
})();
