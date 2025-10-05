<script>
  import icon from '$lib/assets/icon.png';
  import './header.css';
  import { onMount } from 'svelte';
  
  let isMenuOpen = false;
  let isScrolled = false;
  
  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
    document.body.style.overflow = isMenuOpen ? 'hidden' : 'auto';
  }
  
  function closeMenu() {
    isMenuOpen = false;
    document.body.style.overflow = 'auto';
  }
  
  function handleResize() {
    if (window.innerWidth > 768) closeMenu();
  }
  
  function handleScroll() {
    isScrolled = window.scrollY > 20;
  }
  
/**
 * @param {KeyboardEvent} event
 */
function handleKeydown(event) {
  if (event.key === 'Escape' && isMenuOpen) closeMenu();
}
  
  onMount(() => {
    return () => {
      document.body.style.overflow = 'auto';
    };
  });
</script>

<svelte:window 
  on:resize={handleResize} 
  on:scroll={handleScroll}
  on:keydown={handleKeydown}
/>

<header>
  <div class="header-container" class:scrolled={isScrolled}>
    <a href="/" class="logo" on:click={closeMenu}>
      <img src={icon} alt="Logo" style="height: 2rem; vertical-align: middle; margin-right: 0.5rem;" />
      LunaSearch
    </a>
    
    <nav class="nav">
      <ul class="nav-menu" class:active={isMenuOpen}>
        <li>
          <a href="/manual" on:click={closeMenu} aria-label="Ir a Documentación">
            Manual de usuario
          </a>
        </li>
        <li>
          <a href="/mapa" on:click={closeMenu} aria-label="Ir a mapa">
            Mapa
          </a>
        </li>
        <li>
          <a href="/acerca" on:click={closeMenu} aria-label="Ir a acerca de la luna">
            Acerca de la Luna
          </a>
        </li>
      </ul>
    </nav>
    
    <button
      class="hamburger"
      class:active={isMenuOpen}
      on:click={toggleMenu}
      aria-label={isMenuOpen ? 'Cerrar menú' : 'Abrir menú'}
      aria-expanded={isMenuOpen}
    >
      <span></span>
      <span></span>
      <span></span>
    </button>
  </div>
</header>