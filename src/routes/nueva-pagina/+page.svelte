<svelte:head>
  <title>Nueva Página</title>
</svelte:head>


<div class="container">
  <h1> Nueva Página</h1>
  
  <div class="button-group">
    <script>
      import NavButton from '../../components/boton.svelte';
    </script>
    <NavButton text="Ir a Inicio" href="/inicio" color="blue" />
  </div>
</div>