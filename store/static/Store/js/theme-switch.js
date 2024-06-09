// JavaScript для обработки переключения темы
const themeSwitch = document.getElementById('theme-switch');
themeSwitch.addEventListener('change', function() {
    if(this.checked) {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.remove('dark-theme');
    }
});
