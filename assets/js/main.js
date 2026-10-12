(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    toggle.hidden = false;
    nav.dataset.enhanced = 'true';
    const setOpen = open => {
      toggle.setAttribute('aria-expanded', String(open));
      nav.dataset.open = String(open);
    };
    setOpen(false);
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false); toggle.focus();
      }
    });
    nav.addEventListener('click', event => { if (event.target.closest('a')) setOpen(false); });
    const wide = window.matchMedia('(min-width: 761px)');
    wide.addEventListener('change', () => setOpen(false));
  }
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = String(new Date().getFullYear()); });
  const email = window.WHN_CONFIG && window.WHN_CONFIG.contactEmail;
  const status = document.querySelector('[data-contact-status]');
  if (status && typeof email === 'string' && /^[A-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[A-Z0-9](?:[A-Z0-9-]*[A-Z0-9])?(?:\.[A-Z0-9](?:[A-Z0-9-]*[A-Z0-9])?)+$/i.test(email) && !email.includes('TO_CONFIGURE')) {
    const title = document.createElement('strong'); title.textContent = 'Contact Warm Home Notes';
    const para = document.createElement('p');
    const link = document.createElement('a'); link.href = 'mailto:' + encodeURIComponent(email); link.textContent = email;
    para.append(link); status.replaceChildren(title, para);
  }
})();
