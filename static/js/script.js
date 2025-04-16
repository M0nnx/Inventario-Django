document.addEventListener('DOMContentLoaded', function() {
    // Sidebar Toggle
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            
            // En móviles, también añadimos la clase mobile-open
            if (window.innerWidth <= 768) {
                sidebar.classList.toggle('mobile-open');
            }
        });
    }
    
    // Mobile Sidebar
    function handleResize() {
        if (window.innerWidth <= 576) {
            sidebar.classList.add('collapsed');
            mainContent.classList.add('expanded');
        }
    }
    
    window.addEventListener('resize', handleResize);
    handleResize();
    
    // Theme Toggle
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    
    if (themeToggle) {
        // Comprobar si hay una preferencia guardada
        const isDarkMode = localStorage.getItem('darkMode') === 'true';
        
        // Aplicar el modo oscuro si está guardado
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
            themeToggle.textContent = '☀️';
        }
        
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            
            // Guardar preferencia
            const isDark = document.body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDark);
            
            // Cambiar icono
            themeToggle.textContent = isDark ? '☀️' : '🌙';
        });
    }
    
    // Form Toggles
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
    
    function calculateStats() {
        let totalValue = 0;
        const productos = document.querySelectorAll('.products-table tbody tr');
        
        productos.forEach(producto => {
            const cells = producto.querySelectorAll('td');
            if (cells.length >= 5) {
                const precio = parseFloat(cells[3].textContent.replace('$', '')) || 0;
                const stockElement = cells[4].querySelector('.stock-badge');
                const stock = stockElement ? parseInt(stockElement.textContent) : 0;
                totalValue += precio * stock;
            }
        });
        
        const inventoryValueElement = document.getElementById('inventoryValue');
        if (inventoryValueElement) {
            inventoryValueElement.textContent = '$' + totalValue.toFixed(0);
        }
        let lowStockCount = 0;
        productos.forEach(producto => {
            const cells = producto.querySelectorAll('td');
            if (cells.length >= 5) {
                const stockCell = cells[4].querySelector('.stock-badge');
                if (stockCell && stockCell.classList.contains('low')) {
                    lowStockCount++;
                }
            }
        });
        
        const lowStockElement = document.getElementById('lowStock');
        if (lowStockElement) {
            lowStockElement.textContent = lowStockCount;
        }
    }
    
    calculateStats();
    const actionButtons = document.querySelectorAll('.btn-icon');
    actionButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Solo prevenimos el comportamiento por defecto en el botón de eliminar
            if (this.classList.contains('delete')) {
                e.preventDefault();
                
                const row = this.closest('tr');
                const name = row.querySelector('td:nth-child(2)').textContent;
                
                if (confirm(`¿Estás seguro de que deseas eliminar "${name}"?`)) {
                    // Aquí normalmente harías una petición AJAX o una acción de eliminación
                    alert(`Elemento "${name}" eliminado correctamente.`);
                }
            } else {
                const action = this.classList.contains('view') ? 'ver' :
                               this.classList.contains('edit') ? 'editar' : '';
                const row = this.closest('tr');
                const id = row.querySelector('td:first-child').textContent;
                const name = row.querySelector('td:nth-child(2)').textContent;
            }
        });
    });
    
    // Cerrar sidebar al hacer clic fuera en móviles
    document.addEventListener('click', function(event) {
        if (window.innerWidth <= 768 && 
            sidebar && 
            sidebar.classList.contains('mobile-open') && 
            !sidebar.contains(event.target) && 
            event.target !== sidebarToggle) {
            sidebar.classList.remove('mobile-open');
        }
    });
    
    // Búsqueda en tablas
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            filterTables(searchTerm);
        });
    }
    
    // Ajustar altura de las secciones para mantener alineación
    function adjustSectionHeights() {
        const categoriesCard = document.querySelector('.categories-card');
        const productsCard = document.querySelector('.products-card');
        
        // Resetear alturas
        if (categoriesCard && productsCard && window.innerWidth > 992) {
            // En pantallas grandes, ajustamos para que tengan la misma altura
            const categoriesHeader = categoriesCard.querySelector('.card-header');
            const productsHeader = productsCard.querySelector('.card-header');
            
            if (categoriesHeader && productsHeader) {
                // Asegurar que los headers tengan la misma altura
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
    
    // Ejecutar al cargar y al cambiar tamaño de ventana
    adjustSectionHeights();
    window.addEventListener('resize', adjustSectionHeights);
});

// Función para filtrar tablas
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
        
        // Mostrar mensaje si no hay resultados
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