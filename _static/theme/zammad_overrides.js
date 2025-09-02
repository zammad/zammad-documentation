/* Custom overrides */
// No oversized <pre>, please - Thanks to @TJemxx
function collapseLongCodeBlocks() {
  const maxHeight = 250;

  document.querySelectorAll('pre').forEach((el, i) => {
    if (el.clientHeight <= maxHeight) return;

    el.classList.add('collapsing-code-block');
    if (el.querySelector(`.collapsing-code-toggle`)) return;

    const button = document.createElement('button');
    button.classList.add('collapsing-code-toggle');
    button.onclick = (event) => {
      console.debug('onclick', event.target)
      event.target.parentElement.querySelector('.collapsing-code-block').classList.toggle('collapsing-code-block--open')
    };
    el.parentElement.appendChild(button);
  });
}

window.addEventListener('load', () => {
  collapseLongCodeBlocks();

  // click any <a data-tab="..."></a> link
  // to manually re-compute if any code blocks need to be collapsed
  document.querySelectorAll('a').forEach((el) => {
    if ('tab' in el.dataset) el.onclick = collapseLongCodeBlocks;
  });
}, false);
