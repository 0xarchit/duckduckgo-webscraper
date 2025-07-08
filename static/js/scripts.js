// Add any custom JavaScript here if needed
console.log('Custom JS loaded');

// Loading overlay toggle function
function showLoading() {
  const overlay = document.getElementById('loading-overlay');
  if (overlay) overlay.classList.remove('hidden');
}

// Attach form submit to show loading overlay
const searchForm = document.querySelector('form');
if (searchForm) {
  searchForm.addEventListener('submit', showLoading);
}

// Show/hide custom proxy URL input based on selection
const proxySelect = document.getElementById('proxy_source');
const customContainer = document.getElementById('custom_proxy_container');
proxySelect && proxySelect.addEventListener('change', function() {
  if (this.value === 'custom') {
    customContainer.classList.remove('hidden');
  } else {
    customContainer.classList.add('hidden');
  }
});
