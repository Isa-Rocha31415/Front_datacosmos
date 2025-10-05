<script lang="ts">
  import Main from "../components/Main.svelte";
  import NavButton from '../components/boton.svelte';
</script>

<Main></Main>

<div class="container">
  <NavButton 
    text="Ir a Inicio" 
    href="/inicio" 
    color="green"
  />

</div>

<style>
  .container {
    padding: 2rem;
    text-align: center;
  }
</style>
