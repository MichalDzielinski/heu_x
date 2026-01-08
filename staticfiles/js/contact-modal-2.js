(function () {
        
    if (typeof window.closeContact !== 'function') {
      window.closeContact = function (selector) {
        const el = document.querySelector(selector);
        if (el) el.classList.add('hidden');
        const overlay = document.getElementById('contact-overlay');
        if (overlay) overlay.classList.add('hidden');
      };
    }
  
    const getEl = (id) => document.getElementById(id);
  
    function toggleSubmitting(form, isSubmitting) {
      const btn = form.querySelector('button[type="submit"]');
      const status = getEl('form-status');
      if (btn) {
        if (isSubmitting) {
          btn.disabled = true;
          btn.dataset.prev = btn.innerHTML;
          btn.innerHTML = 'Wysyłanie…';
        } else {
          btn.disabled = false;
          if (btn.dataset.prev) btn.innerHTML = btn.dataset.prev;
        }
      }
      if (status) status.classList.toggle('hidden', !isSubmitting);
    }
  
    
    document.body.addEventListener('htmx:beforeRequest', function (e) {
      if (e.detail.elt && e.detail.elt.id === 'contact-form') {
        const err = getEl('form-error');
        if (err) { err.textContent = ''; err.classList.add('hidden'); }
        toggleSubmitting(e.detail.elt, true);
      }
    });
  
    // Po udanym requestcie – pokaz komunikat, zamknij modal po 3s, potem reset formularza
    document.body.addEventListener('htmx:afterRequest', function (e) {
      if (e.detail.elt && e.detail.elt.id === 'contact-form') {
        toggleSubmitting(e.detail.elt, false);
  
        if (e.detail.successful) {
          const form = e.detail.elt;
          const wrapper = getEl('form-wrapper');
          const message = getEl('form-message');
  
          if (wrapper && message) {
            // pokaż komunikat, ukryj formularz
            wrapper.classList.add('hidden');
            message.classList.remove('hidden');
  
          
            setTimeout(function () {
              window.closeContact('#contact-modal');
  
             
              setTimeout(function () {
                form.reset();
                message.classList.add('hidden');
                wrapper.classList.remove('hidden');
              }, 3000);
  
            }, 7000);
          }
        }
      }
    });
  
   
    document.body.addEventListener('htmx:responseError', function (e) {
      if (e.detail.elt && e.detail.elt.id === 'contact-form') {
        toggleSubmitting(e.detail.elt, false);
        const err = getEl('form-error');
        let msg = 'Coś poszło nie tak. Spróbuj ponownie.';
  
        try {
          const json = JSON.parse(e.detail.xhr.responseText);
          if (json && json.errors) {
            msg = Object.values(json.errors).flat().join(' ');
          } else if (json && json.detail) {
            msg = json.detail;
          }
        } catch (_) { }
  
        if (err) { err.textContent = msg; err.classList.remove('hidden'); }
      }
    });
  })();
