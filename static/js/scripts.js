
document.addEventListener('DOMContentLoaded', () => {
  // Attach form submit to show loading overlay
  const searchForm = document.querySelector('form');
  searchForm && searchForm.addEventListener('submit', showLoading);

  const proxySelect = document.getElementById('proxy_source');
  const customContainer = document.getElementById('custom_proxy_container');
  if (proxySelect && customContainer) {
    proxySelect.addEventListener('change', function() {
      if (this.value === 'custom') {
        customContainer.classList.remove('hidden');
      } else {
        customContainer.classList.add('hidden');
      }
    });
  }
});

function showLoading() {
  const overlay = document.getElementById('loading-overlay');
  overlay && overlay.classList.remove('hidden');
}
