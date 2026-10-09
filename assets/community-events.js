/* The catalogue remains readable without JavaScript. Event days use the UTC date. */
(function () {
  'use strict';
  const form = document.getElementById('community-filters');
  if (!form) return;
  const cards = Array.from(document.querySelectorAll('.community-event'));
  const period = document.getElementById('community-period');
  const type = document.getElementById('community-type');
  const country = document.getElementById('community-country');
  const count = document.getElementById('community-count');
  const empty = document.getElementById('community-no-matches');
  Array.from(new Set(cards.map(card => card.dataset.country).filter(Boolean))).sort().forEach(value => {
    const option = document.createElement('option');
    option.value = value;
    option.textContent = value;
    country.appendChild(option);
  });
  function update() {
    const today = new Date().toISOString().slice(0, 10);
    let visible = 0;
    cards.forEach(card => {
      const past = card.dataset.end < today;
      const ongoing = card.dataset.start <= today && !past;
      const when = period.value === 'all' || (period.value === 'past' ? past : !past);
      const matches = when && (type.value === 'all' || type.value === card.dataset.type)
        && (country.value === 'all' || country.value === card.dataset.country);
      card.hidden = !matches;
      card.querySelector('.community-period-label').textContent = ongoing ? ' · Ongoing' : (past ? ' · Past' : '');
      if (matches) visible += 1;
    });
    count.textContent = visible + (visible === 1 ? ' event' : ' events');
    empty.hidden = visible !== 0;
  }
  form.hidden = false;
  count.hidden = false;
  form.addEventListener('change', update);
  form.addEventListener('submit', event => event.preventDefault());
  document.addEventListener('click', event => {
    const link = event.target.closest && event.target.closest('a[href^="#event-"]');
    if (!link) return;
    const target = document.getElementById(link.getAttribute('href').slice(1));
    if (target && target.hidden) {
      period.value = 'all';
      type.value = 'all';
      country.value = 'all';
      update();
    }
  });
  update();
  // Refresh after midnight even if this page remains open overnight.
  window.setInterval(update, 60000);
}());
