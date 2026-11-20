(function () {
  function initializePublications() {
    const root = document.querySelector("[data-publication-list]");
    if (!root) return;

    const dialog = document.getElementById("publication-bibtex-dialog");
    if (!dialog || typeof dialog.showModal !== "function") return;

    const closeButton = dialog.querySelector("[data-bibtex-close]");
    const title = dialog.querySelector("[data-bibtex-title]");
    const content = dialog.querySelector("[data-bibtex-content]");
    const status = dialog.querySelector("[data-bibtex-status]");
    const copyButton = dialog.querySelector("[data-bibtex-copy]");
    const download = dialog.querySelector("[data-bibtex-download]");
    if (!closeButton || !title || !content || !status || !copyButton || !download) return;

    const copyLabel = copyButton.textContent;
    let opener = null;
    let dialogSession = 0;
    let bibtex = "";
    let copyTimer = null;

    function resetCopyFeedback() {
      window.clearTimeout(copyTimer);
      copyTimer = null;
      copyButton.textContent = copyLabel;
    }

    const citationPrefix = "data:application/x-bibtex;charset=utf-8,";

    root.querySelectorAll("a[data-bibtex-link]").forEach(function (link) {
      link.addEventListener("click", function (event) {
        if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey
            || event.shiftKey || event.altKey) return;
        const href = link.getAttribute("href");
        if (!href || !href.startsWith(citationPrefix)) return;

        let citation;
        try {
          citation = decodeURIComponent(href.slice(citationPrefix.length));
          if (!citation.trim()) return;
          if (!dialog.open) dialog.showModal();
        } catch (error) {
          return;
        }

        event.preventDefault();
        dialogSession += 1;
        resetCopyFeedback();
        opener = link;
        bibtex = citation;
        title.textContent = link.dataset.paperTitle || "BibTeX";
        content.textContent = citation;
        copyButton.disabled = false;
        status.textContent = "Ready to copy or download.";
        download.href = href;
        download.download = link.download;
      });
    });

    copyButton.addEventListener("click", async function () {
      if (!dialog.open || !bibtex || copyButton.disabled) return;
      const id = dialogSession;
      const text = bibtex;
      resetCopyFeedback();
      copyButton.disabled = true;
      try {
        if (!navigator.clipboard || typeof navigator.clipboard.writeText !== "function") {
          throw new Error("Clipboard access is unavailable.");
        }
        await navigator.clipboard.writeText(text);
        if (id !== dialogSession || !dialog.open) return;
        copyButton.textContent = "Copied";
        status.textContent = "BibTeX copied to clipboard.";
        copyTimer = window.setTimeout(function () {
          if (id === dialogSession) resetCopyFeedback();
        }, 2000);
      } catch (error) {
        if (id !== dialogSession || !dialog.open) return;
        try {
          content.tabIndex = 0;
          content.focus();
          const selection = window.getSelection();
          if (!selection) throw new Error("Text selection is unavailable.");
          const range = document.createRange();
          range.selectNodeContents(content);
          selection.removeAllRanges();
          selection.addRange(range);
          status.textContent = "Automatic copy is unavailable. BibTeX is selected; press Ctrl+C or Command+C to copy.";
        } catch (selectionError) {
          status.textContent = "Automatic copy is unavailable. Select the BibTeX text and copy it manually, or use Download.";
        }
      } finally {
        if (id === dialogSession && dialog.open) copyButton.disabled = false;
      }
    });

    closeButton.addEventListener("click", function () {
      dialog.close();
    });
    dialog.addEventListener("click", function (event) {
      if (event.target !== dialog) return;
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right
          || event.clientY < bounds.top || event.clientY > bounds.bottom) {
        dialog.close();
      }
    });
    // Native Escape handling closes the dialog and reaches this same cleanup.
    dialog.addEventListener("close", function () {
      if (dialog.open) return;
      dialogSession += 1;
      bibtex = "";
      copyButton.disabled = true;
      resetCopyFeedback();
      if (opener && opener.isConnected) opener.focus();
      opener = null;
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializePublications, { once: true });
  } else {
    initializePublications();
  }
})();
