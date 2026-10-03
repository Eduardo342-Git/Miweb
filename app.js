// Simulación o integración del SDK de ConfigCat
// Se provee un cliente seguro por defecto en caso de no contar con el SDK global cargado
const configcatClient = window.configcatClient || {
    getValue: (key, defaultValue) => defaultValue
};

// El valor por defecto es false (apagado) para producción
const isDarkModeEnabled = configcatClient.getValue("dark_mode_enabled", false);

function setupThemeToggle() {
    // Si el Feature Flag está apagado, no inyectamos ni habilitamos la lógica
    if (!isDarkModeEnabled) {
        console.log("Feature Flag 'dark_mode_enabled' está OFF. Modo oscuro inactivo.");
        return;
    }

    // Lógica que se habilitará cuando el flag pase a ON (Ticket 2 y 3)
    const toggleButton = document.getElementById('theme-toggle-btn');
    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
            localStorage.setItem('theme_preference', currentTheme);
        });
    }
}

document.addEventListener('DOMContentLoaded', setupThemeToggle);
