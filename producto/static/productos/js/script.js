document.addEventListener('DOMContentLoaded', function() {
    // Inicializar funciones
    initializeSidebarToggle();
    initializeMobileSidebar();
    initializeThemeToggle();
    initializeFormToggles();
    initializeTableActions();
    initializeSearch();
    adjustSectionHeights();
});

// Función para manejar el toggle del sidebar
function initializeSidebarToggle() {
    const sidebar = document.querySelector('.sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            if (window.innerWidth <= 768) {
                sidebar.classList.toggle('mobile-open');
            }
        });
    }
}

// Función para manejar el comportamiento del sidebar en dispositivos móviles
function initializeMobileSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');

    function handleResize() {
        if (window.innerWidth <= 576) {
            sidebar.classList.add('collapsed');
            mainContent.classList.add('expanded');
        }
    }
    
    window.addEventListener('resize', handleResize);
    handleResize();
}

// Función para manejar el cambio de tema
function initializeThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    if (themeToggle) {
        const isDarkMode = localStorage.getItem('darkMode') === 'true';
        if (isDarkMode) {
            body.classList.add('dark-mode');
            themeToggle.textContent = '☀️';
        }

        themeToggle.addEventListener('click', function() {
            body.classList.toggle('dark-mode');
            const isDark = body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDark);
            themeToggle.textContent = isDark ? '☀️' : '🌙';
        });
    }
}

// Función para manejar el toggle de los formularios
function initializeFormToggles() {
    // Toggle de formulario de Categoría
    const toggleCategoriaForm = document.getElementById('toggleCategoriaForm');
    const categoriaFormContainer = document.getElementById('categoriaFormContainer');
    const cancelCategoriaForm = document.getElementById('cancelCategoriaForm');
    
    if (toggleCategoriaForm && categoriaFormContainer && cancelCategoriaForm) {
        toggleCategoriaForm.addEventListener('click', function() {
            categoriaFormContainer.style.display = 'block';
            categoriaFormContainer.classList.add('fade-in');
        });

        cancelCategoriaForm.addEventListener('click', function() {
            categoriaFormContainer.style.display = 'none';
        });
    }

    // Toggle de formulario de Producto
    const toggleProductoForm = document.getElementById('toggleProductoForm');
    const productoFormContainer = document.getElementById('productoFormContainer');
    const cancelProductoForm = document.getElementById('cancelProductoForm');
    
    if (toggleProductoForm && productoFormContainer && cancelProductoForm) {
        toggleProductoForm.addEventListener('click', function() {
            productoFormContainer.style.display = 'block';
            productoFormContainer.classList.add('fade-in');
        });

        cancelProductoForm.addEventListener('click', function() {
            productoFormContainer.style.display = 'none';
        });
    }
}

// Función para manejar las acciones en las filas de la tabla
function initializeTableActions() {
    const actionButtons = document.querySelectorAll('.btn-icon');
    
    actionButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.classList.contains('delete')) {
                e.preventDefault();
                const row = this.closest('tr');
                const name = row.querySelector('td:nth-child(2)').textContent;
                const form = this.closest('form'); // Obtén el formulario correspondiente
                if (confirm(`¿Estás seguro de que deseas eliminar "${name}"?`)) {
                    form.submit();  // Si el usuario confirma, envía el formulario
                }
            }
        });
    });
}


// Función para manejar la búsqueda en las tablas
function initializeSearch() {
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            filterTables(searchTerm);
        });
    }
}

// Función para filtrar las tablas basadas en el término de búsqueda
function filterTables(searchTerm) {
    const tables = document.querySelectorAll('.data-table');
    
    tables.forEach(table => {
        const rows = table.querySelectorAll('tbody tr');
        let hasVisibleRows = false;

        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                row.style.display = '';
                hasVisibleRows = true;
            } else {
                row.style.display = 'none';
            }
        });

        let emptyMessage = table.querySelector('.empty-search-message');
        if (!hasVisibleRows) {
            if (!emptyMessage) {
                const colspan = table.querySelectorAll('thead th').length;
                emptyMessage = document.createElement('tr');
                emptyMessage.className = 'empty-search-message';
                emptyMessage.innerHTML = `<td colspan="${colspan}" class="empty-message">No se encontraron resultados para "${searchTerm}"</td>`;
                table.querySelector('tbody').appendChild(emptyMessage);
            }
        } else if (emptyMessage) {
            emptyMessage.remove();
        }
    });
}

// Función para ajustar las alturas de las secciones
function adjustSectionHeights() {
    const categoriesCard = document.querySelector('.categories-card');
    const productsCard = document.querySelector('.products-card');
    
    if (categoriesCard && productsCard && window.innerWidth > 992) {
        const categoriesHeader = categoriesCard.querySelector('.card-header');
        const productsHeader = productsCard.querySelector('.card-header');
        
        if (categoriesHeader && productsHeader) {
            categoriesHeader.style.minHeight = '';
            productsHeader.style.minHeight = '';
            const headerHeight = Math.max(
                categoriesHeader.offsetHeight,
                productsHeader.offsetHeight
            );
            categoriesHeader.style.minHeight = headerHeight + 'px';
            productsHeader.style.minHeight = headerHeight + 'px';
        }
    }
}
// Este código escucha el envío del formulario
document.querySelectorAll('.delete-form').forEach(form => {
    form.addEventListener('submit', function(event) {
        if (!confirm('¿Estás seguro de que deseas eliminar este producto?')) {
            event.preventDefault();
        }
    });
});

